#include <algorithm>
#include <iostream>
using namespace std;

#define int long long

void solve(int n, int f, int a, int b, int arr[]) {
    // print array
    // for (int i = 0; i < n; i++) cout << arr[i] << " ";

    int sum = 0;
    for (int i = 0; i < n - 1; i++) {
        int t = arr[i + 1] - arr[i];
        int e = a * t;
        sum += min(e, b);
    }

    sum += min(a*arr[0], b);
    // cout << sum << endl;

    if (sum < f)
        printf("Yes\n");
    else
        printf("No\n");
}

int32_t main() {
    // fast io
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        int n, f, a, b;
        cin >> n >> f >> a >> b;
        int arr[n];
        for (int i = 0; i < n; i++) cin >> arr[i];
        solve(n, f, a, b, arr);
    }
    return 0;
}