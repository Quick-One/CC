#include <bits/stdc++.h>

using namespace std;

#define int long long
#define endl '\n'

vector<vector<int>> graph;
vector<int> starttour, endtour;
int timer = 0;


struct FenwickTree {
    vector<int> bit;  // binary indexed tree
    int n;

    FenwickTree(int n) {
        this->n = n;
        bit.assign(n, 0);
    }

    FenwickTree(vector<int> const &a) : FenwickTree(a.size()) {
        for (size_t i = 0; i < a.size(); i++)
            add(i, a[i]);
    }

    int sum(int r) {
        int ret = 0;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret += bit[r];
        return ret;
    }

    int sum(int l, int r) {
        return sum(r) - sum(l - 1);
    }

    void add(int idx, int delta) {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] += delta;
    }

    void addRange(int l, int r, int x){
        add(l, x);
        add(r + 1, -x);
    }

    void setElement(int idx, int x){
        addRange(idx, idx, 0 - getElement(idx));
    }

    int getElement(int idx){
        return sum(idx);
    }

    void print(){
        // for (int i = 0; i < n; i++){
        //     cout << getElement(i) << " ";
        // }
        // cout << endl;
    }
};

void euler_tour(int at, int prev) {
    starttour[at] = timer++;
    for (int n : graph[at]) {
        if (n != prev) {
            euler_tour(n, at);
        }
    }
    endtour[at] = timer;
}

struct Query {
    int type, v1, v2;

    // void printQuery(){
    //     cout << type << " " << v1 << " " << v2 << endl;
    // }
};

void solve() {
    graph.clear();
    starttour.clear();
    endtour.clear();
    timer = 0;
    
    graph.push_back({});

    int q;
    cin >> q;
    vector<Query> queries(q);

    int nodes = 1;
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;

        if (type == 1) {
            int parent; cin >> parent; parent--;
            graph.push_back({});
            graph[parent].push_back(nodes);
            queries[i] = {type, parent, nodes};
            nodes++;
        } else {
            int v1, v2;
            cin >> v1 >> v2;
            queries[i] = {type, --v1, v2};


        }
    }
    // cout << "nodes: " << nodes << endl;
    starttour.resize(nodes, 0ll);
    endtour.resize(nodes, 0ll);
    euler_tour(0, -1);

    FenwickTree ft(nodes+1);
    for (auto q: queries){
        if (q.type == 1){
            ft.setElement(starttour[q.v2], 0);
            ft.print();
        } else {
            int l = starttour[q.v1], r = endtour[q.v1] - 1;
            ft.addRange(l, r, q.v2);
            // q.printQuery();
            // cout << q.v1 <<" -- " <<"l: " << l << " r: " << r << endl;
            ft.print();
        }
    }

    vector<int> ans;
    for (int i = 0; i < nodes; i++) {
        // cout << i << ": " << starttour[i] << " " << endtour[i] <<" " << ft.getElement(starttour[i]) << endl;
        ans.push_back(ft.getElement(starttour[i]));
    }
    for (int i = 0; i < nodes; i++) {
        cout << ans[i] << " ";
    }
    cout << endl;

}

int32_t main(void) {
    // fast io
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}