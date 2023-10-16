#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl "\n"

#define range(it, start, end) for (auto it = start; it < end; it++)
#define vin(v) for(auto&x:v)cin>>x;

typedef vector<int> vi;

int INF = 1e18;

int32_t main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n; cin >> n;
    vi v(n); vin(v);

    int ans = INF;
    for (auto x: v) {
        int a = abs(x);
        ans = min(ans, a);
    }
    cout << ans << endl;
}