#include <bits/stdc++.h>

using namespace std;

#define int long long
#define endl '\n'

int bitwiseAND(int a, int b) {
    return a & b;
}
void buildSegmentTree(vector<int>& tree, const vector<int>& arr, int node, int start, int end) {
    if (start == end) {
        tree[node] = arr[start];
    } else {
        int mid = (start + end) / 2;
        buildSegmentTree(tree, arr, 2 * node + 1, start, mid);
        buildSegmentTree(tree, arr, 2 * node + 2, mid + 1, end);
        tree[node] = bitwiseAND(tree[2 * node + 1], tree[2 * node + 2]);
    }
}

int querySegmentTree(const vector<int>& tree, int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return -1; // You can return any suitable value here
    }
    if (left <= start && right >= end) {
        return tree[node];
    }
    int mid = (start + end) / 2;
    int leftResult = querySegmentTree(tree, 2 * node + 1, start, mid, left, right);
    int rightResult = querySegmentTree(tree, 2 * node + 2, mid + 1, end, left, right);
    if (leftResult == -1) return rightResult;
    if (rightResult == -1) return leftResult;
    return bitwiseAND(leftResult, rightResult);
}

int32_t main() {
    // fast io
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);

        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        // Build the segment tree
        vector<int> tree(4 * n); // Assuming a sufficiently large size for the segment tree
        buildSegmentTree(tree, arr, 0, 0, n - 1);

        int q;
        cin >> q;

        vector<int> ans;
        for (int i = 0; i < q; ++i) {
            int left, K;
            cin >> left >> K;
            left--;

            int lo = left, hi = n - 1;

            while (lo < hi) {
                int mid = (lo + hi + 1) / 2;
                if (querySegmentTree(tree, 0, 0, n - 1, left, mid) < K) {
                    hi = mid - 1;
                } else {
                    lo = mid;
                }
            }

            if (querySegmentTree(tree, 0, 0, n - 1, left, lo) >= K) {
                ans.push_back(lo + 1);
            } else {
                ans.push_back(-1);
            }
        }

        for (int i = 0; i < q; ++i) {
            cout << ans[i] << " ";
        }
        cout << endl;
    }

    return 0;
}
