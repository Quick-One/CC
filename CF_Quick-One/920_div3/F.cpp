#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
#define int long long

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int N, Q;
        cin >> N >> Q;

        vector<int> Arr(N);
        for (int i = 0; i < N; ++i) {
            cin >> Arr[i];
        }

        int K = sqrt(N) + 1;

        // MAKE DP OF SIZE N X K
        long long dp[N][K];

        for (int k = 1; k < K; ++k) {
            for (int i = N - 1; i >= 0; --i) {
                if (i + k < N) {
                    dp[i][k] = dp[i + k][k] + Arr[i];
                } else {
                    dp[i][k] = Arr[i];
                }
            }
        }

        // making it a suffix
        for (int k = 1; k < K; ++k) {
            for (int i = N - 1; i >= 0; --i) {
                if (i + k < N) {
                    dp[i][k] += dp[i + k][k];
                }
            }
        }

        vector<long long> ANS;
        for (int q = 0; q < Q; ++q) {
            int s, delta, k;
            cin >> s >> delta >> k;
            s -= 1;

            if (delta < K) {
                long long temp = 0;
                temp += dp[s][delta];
                if (s + delta * k < N) {
                    temp -= dp[s + delta * k][delta];
                    long long x = dp[s + delta * k][delta];
                    if (s + delta * (k + 1) < N) {
                        x -= dp[s + delta * (k + 1)][delta];
                    }
                    temp -= k * x;
                }
                ANS.push_back(temp);
            } else {
                long long temp = 0;
                for (int i = 1; i <= k; ++i) {
                    temp += Arr[s + (i - 1) * delta] * i;
                }
                ANS.push_back(temp);
            }
        }

        for (long long ans : ANS) {
            cout << ans << " ";
        }
        cout << "\n";
    }

    return 0;
}