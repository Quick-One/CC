#include <iostream>
#include <vector>

using namespace std;

// make print function for array
void print(vector<int> arr) {
    return;
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

void solve(int n, int k) {
    vector<int> initial(n);
    for (int i = 0; i < n; i++) {
        initial[n - i - 1] = i + 1;
    }
    print(initial);

    vector<int> result_partial(k);
    for (int i = 0; i < k; i++) {
        result_partial[i] = initial[n - 1 - i];
    }
    print(result_partial);

    vector<int> reversed_partial(k);
    for (int i = 0; i < k; i++) {
        reversed_partial[i] = result_partial[k - 1 - i];
    }
    reversed_partial = result_partial;
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        if (i < k) {
            result[i] = reversed_partial[i];
        } else {
            result[i] = initial[i - k];
        }
    }
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }
    
    cout << endl;
}

int main() {
    // fastio
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        solve(n, k);
    }
    return 0;
}