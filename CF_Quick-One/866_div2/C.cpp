#include <bits/stdc++.h>

using namespace std;

unordered_map<int, int> Counter(vector<int>& arr) {
    unordered_map<int, int> d;
    for (int i : arr) {
        if (d.find(i) == d.end()) {
            d[i] = 0;
        }
        d[i]++;
    }
    return d;
}

int MEX(unordered_map<int, int>& count) {
    int i = 0;
    while (true) {
        if (count.find(i) == count.end()) {
            return i;
        }
        i++;
    }
}

void solve() {
    int N;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    auto c = Counter(arr);
    int x = MEX(c);
    int new_MEX = x + 1;
    if (c.find(new_MEX) != c.end()) {
        vector<int> indices;
        for (int i = 0; i < N; i++) {
            if (arr[i] == new_MEX) {
                indices.push_back(i);
            }
        }
        int l = *min_element(indices.begin(), indices.end());
        int r = *max_element(indices.begin(), indices.end());
        for (int i = l; i <= r; i++) {
            arr[i] = x;
        }
        auto c2 = Counter(arr);
        if (MEX(c2) == new_MEX) {
            cout << "YES\n";
        }
        else {
            cout << "NO\n";
        }
    }
    else {
        for (auto p : c) {
            int i = p.first;
            int v = p.second;
            if ((i < x && v > 1) || (i > x)) {
                cout << "YES\n";
                return;
            }
        }
        cout << "NO\n";
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}