#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl "\n"

#define range(it, start, end) for (auto it = start; it < end; it++)
#define vin(v) for(auto&x:v)cin>>x;

typedef vector<int> vi;

int MOD = 998244353;

long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}

int32_t main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n; cin >> n;
    vi a(n); vin(a);
    vi b(n); vin(b);

    int m; cin >> m;
    vi c(m); vin(c);
    vi d(m); vin(d);

    unordered_map<int, int> d1, d2;
    range(i, 0, n) d1[a[i]] = b[i];
    range(i, 0, m) d2[c[i]] = d[i];



    for (auto p: d2){
        if (d1.find(p.first) == d1.end()){
            cout << 0 << endl;
            return 0;
        }
        if ((d1[p.first] - d2[p.first]) < 0) {
            cout << 0 << endl;
            return 0;
        }
    }

    int ans = 0;
    for (auto p: d1) {
        if (d2.find(p.first) == d2.end()) {
            ans += 1;
        }
        else {
            if (d1[p.first] > d2[p.first]) ans += 1;
        }
    }
    cout << binpow(2, ans, MOD) << endl;

}