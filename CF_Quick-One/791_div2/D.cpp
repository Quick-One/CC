#include<bits/stdc++.h>
using namespace std;
# define int long long

int N, E, K;
vector<int> arr;
vector<vector<int>> g;

vector<int> topological_sort(vector<vector<int>> g) {
    int n = g.size();
    vector<int> status(n);
    vector<int> order;
    for (int root = 0; root < n; root++) {
        if (status[root] == 0) {
            vector<int> stack = {root};
            while (!stack.empty()) {
                int node = stack.back();
                if (status[node] == 0) {
                    status[node] = 1;
                    for (int child : g[node]) {
                        int st_child = status[child];
                        if (st_child == 0) {
                            stack.push_back(child);
                        }
                        else if (st_child == 1) {
                            return {-1};
                        }
                    }
                }
                else {
                    status[node] = 2;
                    order.push_back(node);
                    stack.pop_back();
                }
            }
        }
    }
    reverse(order.begin(), order.end());
    return order;
}

int diameter(vector<int> topo_order, vector<vector<int>> g) {
    vector<int> dp(g.size(), -1);
    for (int i = topo_order.size()-1; i >= 0; i--) {
        int node = topo_order[i];
        if (g[node].empty()) {
            dp[node] = 1;
        }
        else {
            int val = -1;
            for (int child : g[node]) {
                val = max(val, dp[child]);
            }
            dp[node] = val + 1;
        }
    }
    return *max_element(dp.begin(), dp.end());
}

bool f(int x) {
    vector<int> remapping(N, -1);
    int index = 0;
    for (int i = 0; i < N; i++) {
        if (arr[i] <= x) {
            remapping[i] = index;
            index++;
        }
    }
    vector<vector<int>> g2(index);
    for (int i = 0; i < N; i++) {
        for (int j : g[i]) {
            if (remapping[i] != -1 && remapping[j] != -1) {
                g2[remapping[i]].push_back(remapping[j]);
            }
        }
    }
    vector<int> topo_order = topological_sort(g2);




    if (topo_order.size() == 1 && topo_order[0] == -1) {
        return true;
    }
    if (diameter(topo_order, g2) >= K) {
        return true;
    }
    return false;
}

signed main() {
    cin >> N >> E >> K;
    arr.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    g.resize(N);
    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        g[u].push_back(v);
    }
    // Make arr2 a copy of arr

    vector<int> arr2 = arr;
    sort(arr2.begin(), arr2.end());
    int l = 0, u = N-1;

    while (l < u) {
        int mid = (l + u) / 2;
        if (f(arr2[mid])) {
            u = mid;
        }
        else {
            l = mid + 1;
        }
    }
    if (f(arr2[l])) {
        cout << arr2[l] << endl;
    } else {
        cout << -1 << endl;
    }
    return 0;
}