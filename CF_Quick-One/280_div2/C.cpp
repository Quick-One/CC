#include <bits/stdc++.h>

using namespace std;

#define int long long

int32_t main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, r, avg;
    cin >> n >> r >> avg;
    vector<pair<int, int>> v(n);
    int ans = 0;
    int goal = avg * n;

    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        goal -= a;
        v.push_back({b, r - a});
    }

    if (goal <= 0){
        cout << 0 << endl;
        return 0;
    }

    sort(v.begin(), v.end());
    for (auto& p: v){
        int freq = min(goal, p.second);
        goal -= freq;
        ans += freq * p.first;
    } 

    cout << ans << endl;
    return 0;
}