#include <bits/stdc++.h>

using namespace std;
#define int long long
#define endl '\n'

#pragma GCC optimize "trapv"

inline int md(pair<int, int> a, pair<int, int> b) {
    return abs(b.first - a.first) + abs(b.second - a.second);
}

void solve() {
    int n, k, a, b;
    cin >> n >> k >> a >> b;

    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; i++) cin >> v[i].first >> v[i].second;

    vector<int> m;

    for (auto it : {a, b}) {
        if (it <= k) {
            m.push_back(it - 1);
            continue;
        }

        int mini = 0;
        for (int j = 1; j < k; j++) {
            if (md(v[it - 1], v[j]) < md(v[it - 1], v[mini])) {
                mini = j;
            }
        }
        m.push_back(mini);
    }

    int ans = min(md(v[a - 1], v[b - 1]), md(v[a - 1], v[m[0]]) + md(v[b - 1], v[m[1]]));
    cout << ans << endl;
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}