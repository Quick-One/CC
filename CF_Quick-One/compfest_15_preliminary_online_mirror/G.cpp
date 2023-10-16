#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl "\n"

#define range(it, start, end) for (auto it = start; it < end; it++)
#define vin(v) for(auto&x:v)cin>>x;

typedef vector<int> vi;

vector<pair<int, pair<int, int>>> v;
int n;


void print_multiset(multiset<pair<int, int>> &s) {
	for (auto x : s) {
		cout << x.first << "," << x.second << ' ';
	}
	cout << endl;
}

bool check(int mid) {
	// make a multiset  which will contain pair of {end, x}. 

	
	// int pointer = 0;
	// priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	// range(i, 0, n) {
	// 	int total = mid;
	// 	while (pointer != n && v[pointer].first <= i) {
	// 		pq.push({v[pointer].second.first, v[pointer].second.second});
	// 		pointer++;
	// 	}

	// 	while (!pq.empty() && total > 0) {
	// 		auto x = pq.top();
	// 		pq.pop();
	// 		if (x.first < i) return false;
	// 		int val = min(total, x.second);
	// 		total -= val;
	// 		x.second -= val;
	// 		if (x.second > 0) pq.push(x);
	// 	}
	// }
	// if (pq.empty()) return true;
	// return false;
	// cout << "mid: " << mid << endl;
	multiset<pair<int, int>> s;
	int pointer = 0;
	range(i, 0, n) {
		int total = mid;
		// cout << i << ": ";
		while (pointer != n && v[pointer].first <= i) {
			s.insert({v[pointer].second.first, v[pointer].second.second});
			pointer++;
		}
		// print_multiset(s);
		while (!s.empty() && total > 0) {
			auto x = *s.begin();
			s.erase(s.begin());
			if (x.first < i) return false;
			int val = min(total, x.second);
			total -= val;
			x.second -= val;
			if (x.second > 0) s.insert(x);
		}
		// print_multiset(s);
	}
	if (s.empty()) return true;
	// cout << "mid: " << mid << endl;
	return false;

}

int32_t  main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;
	vi a(n); vin(a);
	vi d(n); vin(d);
	v.resize(n);
	range(i, 0, n){
		v[i] = {max(0ll, i - d[i]), {min(n, i + d[i]), a[i]}};
	}
	sort(v.begin(), v.end());

	int lo = 0, hi = *max_element(a.begin(), a.end());
	
	while (lo < hi) {
		int mid = lo + (hi - lo) / 2;
		if (check(mid)) {
			hi = mid;
		} else {
			lo = mid + 1;
		}
	}
	cout << lo << endl;
}