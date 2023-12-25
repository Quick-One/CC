#include <bits/stdc++.h>

#define int long long
#define endl '\n'

using namespace std;

vector<vector<int>> graph;
vector<int> start, endp;
int timer = 0;


#define n_l '\n'
#define dbg(...) cout << "[" << #__VA_ARGS__ << "]: "; cout << to_string(__VA_ARGS__) << endl
template <typename T, size_t N> int SIZE(const T (&t)[N]){ return N; } template<typename T> int SIZE(const T &t){ return t.size(); } string to_string(const string s, int x1=0, int x2=1e9){ return '"' + ((x1 < s.size()) ? s.substr(x1, x2-x1+1) : "") + '"'; } string to_string(const char* s) { return to_string((string) s); } string to_string(const bool b) { return (b ? "true" : "false"); } string to_string(const char c){ return string({c}); } template<size_t N> string to_string(const bitset<N> &b, int x1=0, int x2=1e9){ string t = ""; for(int __iii__ = min(x1,SIZE(b)),  __jjj__ = min(x2, SIZE(b)-1); __iii__ <= __jjj__; ++__iii__){ t += b[__iii__] + '0'; } return '"' + t + '"'; } template <typename A, typename... C> string to_string(const A (&v), int x1=0, int x2=1e9, C... coords); int l_v_l_v_l = 0, t_a_b_s = 0; template <typename A, typename B> string to_string(const pair<A, B> &p) { l_v_l_v_l++; string res = "(" + to_string(p.first) + ", " + to_string(p.second) + ")"; l_v_l_v_l--; return res; } template <typename A, typename... C> string to_string(const A (&v), int x1, int x2, C... coords) { int rnk = rank<A>::value; string tab(t_a_b_s, ' '); string res = ""; bool first = true; if(l_v_l_v_l == 0) res += n_l; res += tab + "["; x1 = min(x1, SIZE(v)), x2 = min(x2, SIZE(v)); auto l = begin(v); advance(l, x1); auto r = l; advance(r, (x2-x1) + (x2 < SIZE(v))); for (auto e = l; e != r; e = next(e)) { if (!first) { res += ", "; } first = false; l_v_l_v_l++; if(e != l){ if(rnk > 1) { res += n_l; t_a_b_s = l_v_l_v_l; }; } else{ t_a_b_s = 0; } res += to_string(*e, coords...); l_v_l_v_l--; } res += "]"; if(l_v_l_v_l == 0) res += n_l; return res; } void dbgm(){;} template<typename Heads, typename... Tails> void dbgm(Heads H, Tails... T){ cout << to_string(H) << " | "; dbgm(T...); } 
#define dbgm(...) cout << "[" << #__VA_ARGS__ << "]: "; dbgm(__VA_ARGS__); cout << endl

void euler_tour(int at, int prev) {
	start[at] = timer++;
	for (int n : graph[at]) {
		if (n != prev) { euler_tour(n, at); }
	}
	endp[at] = timer;
}


struct Query{
    int l, r, x, id;
};

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
};


void solve(){
    int n, q;
    cin >> n >> q;

    graph.resize(n);
    start.resize(n);
    endp.resize(n);

    for (int i = 0; i < n-1; i++)
    {
        int u, v;
        cin >> u >> v;
        u--; v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        arr[i]--;
    }

    euler_tour(0, -1);

    vector<vector<int>> ans(q);
    vector<Query> queries;


    for (int i = 0; i < q; i++)
    {
        int l,r,x;
        cin >> l >> r >> x;
        l--; r--; x--;
        queries.push_back({l, r, start[x] - 1, i});
        queries.push_back({l, r, endp[x] - 1 , i});
    }

    sort(queries.begin(), queries.end(), [](Query a, Query b){
        return a.x < b.x;
    });
    

    FenwickTree ft(n);

    vector<pair<int, int>> temp;
    for (int i = 0; i < n; i++){
        temp.push_back({start[arr[i]], i});
    }
    sort(temp.begin(), temp.end());
    
    int pointer  = 0;

    for (auto que : queries){
        while (pointer < temp.size() && temp[pointer].first <= que.x){
            ft.add(temp[pointer].second, 1);
            pointer++;
        }
        ans[que.id].push_back(ft.sum(que.l, que.r));
    }
    for (auto a : ans){
        if (a[1] - a[0] > 0) cout << "YES" << endl;
        else cout << "NO" << endl;
    }

    graph.clear();
    start.clear();
    endp.clear();
    timer = 0;

}

int32_t main(void){
    // fast io
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t --){
        solve();
    }
    return 0;
    
}