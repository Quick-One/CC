#include <iostream>
#include <vector>
using namespace std;

void print_vector(vector<int> vec) {
    for (int i = 0; i < vec.size(); ++i) {
        cout << vec[i] << " ";
    }
    cout << '\n';
}

void solve_dig(int dig, const vector<int>& order, const vector<int>& parent, vector<int>& A, vector<long long>& ANS, int N, const vector<vector<int>>& graph, vector<vector<long long>>& dp1, vector<vector<long long>>& dp2, vector<int>& size1) {
    for (int i = order.size() - 1; i >= 0; --i) {
        int node = order[i];
        long long zero = 0;
        if (A[node] == 0) {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                zero += dp1[child][0];
            }
        } else {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                zero += dp1[child][1];
            }
            zero += size1[node];
        }

        long long one = 0;
        if (A[node] == 1) {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                one += dp1[child][1];
            }
        } else {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                one += dp1[child][0];
            }
            one += size1[node];
        }

        dp1[node][0] = zero;
        dp1[node][1] = one;
    }

    for (int node : order) {
        int papa = parent[node];
        if (papa == -1) continue;

        long long zero = 0;
        if (A[papa] == 0) {
            zero = dp1[papa][0] - dp1[node][0];
        } else if (A[papa] == 1) {
            zero = dp1[papa][0] - dp1[node][1] - size1[node];
        }

        long long one = 0;
        if (A[papa] == 1) {
            one = dp1[papa][1] - dp1[node][1];
        } else {
            one = dp1[papa][1] - dp1[node][0] - size1[node];
        }

        int grandparent = parent[papa];
        if (grandparent != -1) {
            if (A[papa] == 0) {
                zero += dp2[papa][0];
            } else {
                zero += dp2[papa][1] + (N - size1[papa]);
            }

            if (A[papa] == 1) {
                one += dp2[papa][1];
            } else {
                one += dp2[papa][0] + (N - size1[papa]);
            }
        }
        dp2[node][0] = zero;
        dp2[node][1] = one;
    }

    for (int node = 0; node < N; ++node) {
        long long zero = 0;
        if (A[node] == 0) {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                zero += dp1[child][0];
            }
            if (parent[node] != -1) {
                zero += dp2[node][0];
            }
        } else {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                zero += dp1[child][1];
            }
            if (parent[node] != -1) {
                zero += dp2[node][1];
            }
            zero += N;
        }

        long long one = 0;
        if (A[node] == 1) {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                one += dp1[child][1];
            }
            if (parent[node] != -1) {
                one += dp2[node][1];
            }
        } else {
            for (int child : graph[node]) {
                if (child == parent[node]) continue;
                one += dp1[child][0];
            }
            if (parent[node] != -1) {
                one += dp2[node][0];
            }
            one += N;
        }

        ANS[node] += min(zero, one) << dig;
    }
}

void solve() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<vector<int>> graph(N);
    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    vector<long long> ANS(N, 0);

    int root = 0;
    vector<bool> visited(N, false);
    vector<int> parent(N, -1);
    vector<int> order;

    vector<int> stack;
    stack.push_back(root);
    visited[root] = true;

    while (!stack.empty()) {
        int curr = stack.back();
        stack.pop_back();
        order.push_back(curr);
        visited[curr] = true;
        for (int child : graph[curr]) {
            if (!visited[child]) {
                stack.push_back(child);
                parent[child] = curr;
            }
        }
    }

    // nx2 dp
    vector<vector<long long>> dp1(N, vector<long long>(2, 0));
    vector<vector<long long>> dp2(N, vector<long long>(2, 0));

    vector<int> size1(N, 1);
    for (int i = order.size() - 1; i >= 0; --i) {
        int node = order[i];
        for (int child : graph[node]) {
            if (child == parent[node]) continue;
            size1[node] += size1[child];
        }
    }

    vector<int> small_A(N);
    for (int i = 0; i < 20; ++i) {
        for (int k = 0; k < N; k++)
        {
            small_A[k] = (A[k] >> i) & 1;
        }
        solve_dig(i, order, parent, small_A, ANS, N, graph, dp1, dp2, size1);
    }

    for (int i = 0; i < N; ++i) {
        cout << ANS[i] << " ";
    }
    cout << '\n';
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        solve();
    }
    return 0;
}
