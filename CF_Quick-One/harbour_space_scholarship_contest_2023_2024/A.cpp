#include <bits/stdc++.h>

using namespace std;
#define int long long
#define endl '\n'

#define range(it, start, end) for (auto it = start; it < end; it++)
#define vin(v) for(auto&x:v)cin>>x;
#define print(v) for (auto x: v)cout<<x<<' ';cout<<endl;


void solve(){
    int x,y, n;
    cin >> x >> y >> n;
    vector<int> a(n);
    a[0] = x;
    a[n-1] = y;

    int diff = 1;
    for (int i = n-2; i > 0; i--)   
    {
        a[i] = a[i+1] - diff;
        diff++;
    }
    
    // print(a)
    if (a[1] - a[0] > a[2] - a[1]) {
        print(a);    
    }
    else {cout << -1 << endl;}
}

int32_t main(void){
    // fast io
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t; cin >> t;
    range(_, 0,  t) solve();

}