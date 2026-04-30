#include<bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false),cin.tie(nullptr);
    long long w, l, m, n;
    cin >> w >> l >> m >> n;

    long long area = w * l;
    long long areabox = 0;
    vector<long long> size;

    for (long long i = m; i <= n; ++i) {
        long long w1 = w;
        long long l1 = l;
        
        while (w1 >= i) {
            areabox += i * l;
            w1 -= i;
        }

        while (l1 >= i) {
            areabox += i * w1;
            l1 -= i;
        }

        size.push_back(areabox);
        areabox = 0;
    }

    long long max_size = 0;
    if (!size.empty()) {
        max_size = *max_element(size.begin(), size.end());
    }

    cout << area - max_size << "\n";
    return 0;
}
    