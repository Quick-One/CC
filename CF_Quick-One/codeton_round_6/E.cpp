#include <bits/stdc++.h>

using namespace std;

// #define int long long
#define endl '\n'

#define forn(it, start, end) for (auto it = start; it < end; it++)
#define vin(v) \
    for (auto& x : v) cin >> x;

typedef vector<int> vi;

int MEX[5005][5005];
int dp[5005][5005];

void solve() {
    int n;
    cin >> n;
    vi a(n);
    vin(a);
    forn(l, 0, n) {
        vi state(n + 1, 0);
        int pointer = 0;
        forn(r, l, n) {
            state[a[r]]++;
            while (state[pointer] != 0) pointer++;
            MEX[l][r] = pointer;
        }
    }

    vector<pair<int, int>> intervals;
    forn(l, 0, n) {
        forn(r, l, n) {
            if ((r - l + 1) == 1) {
                intervals.push_back({l, r});
                continue;
            }
            if (MEX[l][r] == MEX[l][r - 1]) continue;
            if (MEX[l][r] == MEX[l + 1][r]) continue;
            intervals.push_back({l, r});
        }
    }

    // sort intervals by the second elemnent in reverse order
    sort(intervals.begin(), intervals.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.second > b.second;
    });

    dp[0][0] = 1;
    forn(r, 1, n + 1) {
        while (intervals.size() and (intervals.back().second == r - 1)) {
            int left, right;
            left = intervals.back().first;
            right = intervals.back().second;
            intervals.pop_back();

            forn(j, 0, n + 1) {
                if (dp[left][j] == 1) dp[r][j ^ MEX[left][right]] = 1;
            }
        }
        forn(j, 0, n + 1) {
            if (dp[r - 1][j] == 1) dp[r][j] = 1;
        }
    }

    int ans = 0;
    for (int i = n; i >= 0; i--){
        if (dp[n][i] == 1) {
            ans = i;
            break;
        }
    }
    cout << ans << endl;

    forn(i, 0, n + 1) {
        forn(j, 0, n + 1) {
            dp[i][j] = 0;
        }
    }

    forn(i, 0, n + 1) {
        forn(j, 0, n + 1) {
            MEX[i][j] = 0;
        }
    }
}

int32_t main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}