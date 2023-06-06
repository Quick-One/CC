# from sys import stdin
from collections import Counter, deque

# import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from sys import stdin
def input(): return stdin.readline()[:-1]


N = int(input())
graph = {}
edges = []
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
vals = list(map(int, input().split()))

# print(vals)
class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load]
                                for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))

    def mad(self):
        if len(self) == 0:
            return 0
        return self[-1]


def ons_side_bfs(s, no):
    val = [vals[s]]
    visited = set()
    visited.add(s)
    bfs_queue = deque()
    bfs_queue.append(s)

    while bfs_queue:
        node = bfs_queue.popleft()
        for child in graph[node]:
            if child not in visited and child != no:
                visited.add(child)
                val.append(vals[child])
                bfs_queue.append(child)
    return val

def two_side_bfs(s, no1, no2):
    val = [vals[s]]
    visited = set()
    visited.add(s)
    bfs_queue = deque()
    bfs_queue.append(s)

    while bfs_queue:
        node = bfs_queue.popleft()
        for child in graph[node]:
            if  child not in visited and child != no1 and child != no2:
                visited.add(child)
                val.append(vals[child])
                bfs_queue.append(child)
    return val


MAD = 0
c = Counter(vals)
for i, v in c.items():
    if v >= 2:
        MAD = max(MAD, i)

if MAD == 0:
    for _ in range(N-1):
        print(0)
elif c[MAD] > 2:
    for _ in range(N-1):
        print(MAD)
else:
    nodes = []
    for i in range(N):
        if vals[i] == MAD:
            nodes.append(i)
    n1, n2 = nodes

    visited = [False] * N
    visited[n1] = True
    parent = [-1] * N
    bfs_queue = deque()
    bfs_queue.append(n1)
    while bfs_queue:
        p = bfs_queue.popleft()

        if p == n2:
            break

        for child in graph[p]:
            if not visited[child]:
                visited[child] = True
                parent[child] = p
                bfs_queue.append(child)

    path = [n2]
    while path[-1] != n1:
        path.append(parent[path[-1]])


    left_side = ons_side_bfs(path[0], path[1])
    right_side = ons_side_bfs(path[1], path[0])
    left_side_c = Counter(left_side)
    right_side_c = Counter(right_side)
    l = SortedList()
    r = SortedList()

    for i, v in left_side_c.items():
        if v >= 2:
            l.add(i)
    for i, v in right_side_c.items():
        if v >= 2:
            r.add(i)

    OTHERS = {}
    OTHERS[(path[0], path[1])] = max(l.mad(), r.mad())
    for i in range(1, len(path)-1):
        a, b = path[i], path[i+1]
        valueeee = two_side_bfs(a, b, path[i-1])
        
        for valueee in valueeee:
            if left_side_c[valueee] == 1:
                l.add(valueee)
            left_side_c[valueee] += 1
            if right_side_c[valueee] == 2:
                r.remove(valueee)
            right_side_c[valueee] -= 1
        OTHERS[(a, b)] = max(l.mad(), r.mad())

    path = set(path)
    for e in edges:
        a, b = e
        if a in path and b in path:
            k = (max(OTHERS.get((a, b), -1), OTHERS.get((b, a), -1)))
            print(k)
        else:
            print(MAD)
