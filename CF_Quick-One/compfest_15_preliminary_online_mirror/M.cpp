#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl "\n"

#define range(it, start, end) for (auto it = start; it < end; it++)
#define vin(v) for (auto& x : v) cin >> x;

typedef vector<int> vi;
const int MOD = 998244353;

int n;
vi v, d;
int f[200005];
int sij[100][200005];


int binpow(int x, int e) {
    int ans = 1;
    while (e) {
        if (e & 1) ans = (ans * x) % MOD;
        x = (x * x) % MOD;
        e >>= 1;
    }
    return ans;
}

int modinv(int x) {
    return binpow(x, MOD - 2);
}

int32_t main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);



    cin >> n;
    v.resize(n); d.resize(100);
    vin(v);

    range(i, 0, 100) {
        d[i] = i * modinv(100);
        d[i] %= MOD;
    }

    range(x, 1, n + 1){
        int px = v[x-1];
        int fx_num = 1 + sij[px][x];
        int fx_den = (1  - d[px] + MOD) % MOD;
        fx_num %= MOD;
        fx_den %= MOD;
        f[x] = (fx_num * modinv(fx_den)) % MOD;


        range(i, 0, 100) {
            int term1 = (f[x] * d[i]) % MOD;
            term1 *= d[i];
            term1 %= MOD;

            int term2 = (d[i] * sij[i][x]) % MOD;
            sij[i][x+1] = (term1 + term2) % MOD;
        }

    }
    int ans = 0;
    range(x, 1, n + 1) {
        ans += f[x];
        ans %= MOD;
    }
    cout << ans << endl;

}
