#include <iostream>
#include <vector>
#include <unordered_map>
 
using namespace std;
 
const int MAXN = 2e5 + 5;
 
int N;
vector<pair<int, int>> g[MAXN];
bool visited[MAXN];
vector<int> edges_visited;
 
int compute(const vector<int>& arr) {
    int c = 0;
    for (int i = 0; i < arr.size() - 1; ++i) {
        if (arr[i + 1] < arr[i]) {
            c += 1;
        }
    }
    return c + 1;
}
 
int dfs(int u) {
    visited[u] = true;
 
    if (g[u].size() == 1 && u != 0) {
        return compute(edges_visited);
    }
 
    int ans = -1;
    for (auto [v, edge] : g[u]) {
        if (!visited[v]) {
            edges_visited.push_back(edge);
            ans = max(ans, dfs(v));
            edges_visited.pop_back();
        }
    }
    return ans;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int t;
    cin >> t;
 
    while (t--) {
        cin >> N;
 
        for (int i = 0; i < N; ++i) {
            g[i].clear();
            visited[i] = false;
        }
        edges_visited.clear();
 
        for (int i = 0; i < N - 1; ++i) {
            int u, v;
            cin >> u >> v;
            u -= 1;
            v -= 1;
            g[u].emplace_back(v, i + 1);
            g[v].emplace_back(u, i + 1);
        }
 
        int ans = dfs(0);
        cout << ans << "\n";
    }
 
    return 0;
}