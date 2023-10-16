#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl "\n"

#define range(it, start, end) for (auto it = start; it < end; it++)
#define vin(v) \
    for (auto& x : v) cin >> x;

typedef vector<int> vi;

int MOD = 998244353;

struct Node {
    int ones, zero, ans;

    Node merge(Node a, Node b) {
        if (b.ones == -1) return a;
        Node c;
        c.ones = (a.ones + b.ones) % MOD;
		c.zero = (a.zero + b.zero) % MOD;
		c.ans = ((a.ans + b.ans) % MOD + (a.ones * b.zero) % MOD) % MOD;
        return c;
    }
};

vector<vector<int>> graph;
int n;
vector<Node> v;
vector<bool> visited;

Node dfs(int num) {
    if (visited[num]) return v[num];
    visited[num] = true;

    if (graph[num].size() == 0) {
        Node x = {0,0,0};
        v[num] = x;
        return x;
    }

    vector<Node> children;
    for (auto edge : graph[num]) {
        int next = edge >> 1, color = edge & 1;
        children.push_back(Node{color, (1 ^ color), 0 });
        children.push_back(dfs(next));
    }

    Node ans = children[0];
    range(i, 1, children.size()) {
        ans = ans.merge(ans, children[i]);
    }
    v[num] = ans;
    return ans;
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    graph.resize(n);
    visited.resize(n, false);
    v.reserve(2e5);

    range(i, 0, n) {
        int x;
        cin >> x;
        range(j, 0, x) {
            int next, color;
            cin >> next >> color;
            next--;
            graph[i].push_back((next << 1) + color);
        }
    }
    cout << dfs(0).ans << endl;
}