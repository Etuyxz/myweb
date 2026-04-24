#include <WiFi.h>
#include <HTTPClient.h>
#include "time.h"

// ======================= ส่วนตั้งค่า (แก้ไขตรงนี้) =======================
const char* ssid     = "...";       // 📶 ใส่ชื่อ WiFi
const char* password = "...";        // 🔑 ใส่รหัสผ่าน
const char* discord_webhook = "..."; 
// ===================================================================

// --- กำหนดขา Pin (ESP32) ---
#define TRIG_PIN_1  13
#define ECHO_PIN_1  12
#define TRIG_PIN_2  14
#define ECHO_PIN_2  27

// --- ตั้งค่าเวลาอินเทอร์เน็ต (NTP) ---
const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = 25200; // เวลาประเทศไทย GMT+7 (7 * 3600)
const int   daylightOffset_sec = 0;

// --- ตั้งค่าการจับเวลา ---
unsigned long previousMillis = 0;
// ⏱️ เวลาส่งข้อมูล: 3600000 มิลลิวินาที = 1 ชั่วโมง
const long interval = 60000; 

void setup() {
  Serial.begin(115200);

  // ตั้งค่าโหมดของขา Pin เซนเซอร์
  pinMode(TRIG_PIN_1, OUTPUT); pinMode(ECHO_PIN_1, INPUT);
  pinMode(TRIG_PIN_2, OUTPUT); pinMode(ECHO_PIN_2, INPUT);

  // เริ่มเชื่อมต่อ WiFi
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ WiFi Connected!");

  // ซิงค์เวลาจากอินเทอร์เน็ต
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  
  // ให้ระบบรอโหลดเวลาแป๊บนึง
  delay(2000);

  // ส่งแจ้งเตือนว่าบอร์ดเริ่มทำงาน (เพื่อให้เรารู้ว่าไฟเข้าและเน็ตต่อติดแล้ว)
  sendBootMessage();
}

void loop() {
  unsigned long currentMillis = millis();

  // เช็คว่าครบ 1 ชั่วโมงหรือยัง
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    
    // ตรวจสอบเวลาปัจจุบัน
    struct tm timeinfo;
    if (getLocalTime(&timeinfo)) {
      int currentHour = timeinfo.tm_hour;
      Serial.print("เวลาปัจจุบัน: "); Serial.print(currentHour); Serial.println(" นาฬิกา");

      // 🌙 เงื่อนไขเวลา: ทำงานเฉพาะ 06:00 ถึง 19:59 น.
      if (currentHour >= 6 && currentHour < 20) {
        Serial.println("🌞 เวลากลางวัน: กำลังตรวจสอบและส่งสถานะ...");
        checkAndSendStatus();
      } else {
        Serial.println("💤 เวลากลางคืน: งดส่งข้อความรบกวน (Silent Mode)");
      }
    } else {
      Serial.println("❌ ไม่สามารถดึงเวลาได้ (ข้ามการส่งรอบนี้)");
    }
  }
}

// --- ฟังก์ชันวัดระยะทางของเซนเซอร์ ---
int getDistance(int trig, int echo) {
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10);
  digitalWrite(trig, LOW);
  long duration = pulseIn(echo, HIGH, 30000); 
  if (duration == 0) return -1; // ถ้าสายหลุดหรือเซนเซอร์มีปัญหา
  return duration * 0.034 / 2;
}

// --- ฟังก์ชันแปลงเวลาให้เป็นข้อความ ---
String getTimeString() {
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)) return "ไม่ทราบเวลา";
  char timeStringBuff[50];
  strftime(timeStringBuff, sizeof(timeStringBuff), "%H:%M น.", &timeinfo);
  return String(timeStringBuff);
}

// --- ฟังก์ชันหลัก: ตรวจสอบเซนเซอร์และเตรียมการ์ดข้อความ ---
void checkAndSendStatus() {
  int d1 = getDistance(TRIG_PIN_1, ECHO_PIN_1);
  delay(50); // พักแป๊บนึงกันคลื่นเสียงกวนกัน
  int d2 = getDistance(TRIG_PIN_2, ECHO_PIN_2);

  int queueCount = 0;
  // ถ้าระยะน้อยกว่า 20 ซม. ให้ถือว่ามีตะกร้าวางอยู่ (นับเป็น 1 คิว)
  if (d1 != -1 && d1 < 20) queueCount++;
  if (d2 != -1 && d2 < 20) queueCount++;

  long color;
  String title;
  String description;

  if (queueCount == 0) {
    color = 5763719; // 🟢 สีเขียว
    title = "✅ เครื่องว่าง (Available)";
    description = "\\n✨ **สถานะ:** เครื่องพร้อมใช้งานทันที\\n\\n💬 **รายละเอียด:** ไม่มีตะกร้ารอเลย ซักได้เลยครับ!\\n";
  } 
  else if (queueCount == 1) {
    color = 16776960; // 🟡 สีเหลือง
    title = "⚠️ มี 1 คิว (Busy)";
    description = "\\n🧺 **สถานะ:** มีตะกร้ารออยู่ 1 จุด\\n\\n⏳ **คำแนะนำ:** อาจต้องรอสักพัก\\n";
  } 
  else {
    color = 15548997; // 🔴 สีแดง
    title = "⛔ คิวเต็ม / มี 2 คิว (Full)";
    description = "\\n🔒 **สถานะ:** ไม่ว่าง! มีตะกร้าวางเต็ม 2 จุด\\n\\n❌ **คำแนะนำ:** กรุณามาใหม่ภายหลัง\\n";
  }

  sendEmbedToDiscord(title, description, color);
}

// --- ฟังก์ชันยิงข้อมูลขึ้น Discord (แบบการ์ด Embed) ---
void sendEmbedToDiscord(String title, String desc, long color) {
  if(WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(discord_webhook);
    http.addHeader("Content-Type", "application/json");

    String timeStr = getTimeString();

    String jsonPayload = "{";
    jsonPayload += "\"embeds\": [{";
    jsonPayload += "\"title\": \"" + title + "\",";
    jsonPayload += "\"description\": \"" + desc + "\",";
    jsonPayload += "\"color\": " + String(color) + ",";
    jsonPayload += "\"footer\": { \"text\": \"🕒 เวลาที่ตรวจวัด: " + timeStr + "\" }";
    jsonPayload += "}]";
    jsonPayload += "}";
    
    int httpResponseCode = http.POST(jsonPayload);
    
    if (httpResponseCode >= 200 && httpResponseCode < 300) {
      Serial.println("✅ แจ้งเตือนสถานะสำเร็จ!");
    } else {
      Serial.print("❌ ส่งข้อมูลล้มเหลว รหัส: "); Serial.println(httpResponseCode);
    }
    http.end();
  }
}

// --- ฟังก์ชันแจ้งเตือนตอนเสียบปลั๊ก ---
void sendBootMessage() {
  if(WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(discord_webhook);
    http.addHeader("Content-Type", "application/json");
    
    String jsonPayload = "{\"content\": \"🚀 **ระบบ Smart Laundry เชื่อมต่อสำเร็จ!**\\nเริ่มรายงานสถานะทุกๆ 1 ชั่วโมง (งดส่งช่วง 20:00 - 05:59 น.)\"}";
    http.POST(jsonPayload);
    http.end();
  }
}
