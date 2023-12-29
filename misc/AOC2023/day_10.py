from sys import stdin
def input(): return stdin.readline()[:-1]
from collections import Counter

from copy import deepcopy

def ceildiv(a, b):
    return -(a // -b)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, a): #return parent of a. a and b are in same set if they have same parent
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a: #path compression
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
    def union(self, a, b): #union a and b
        self.parent[self.find(b)] = self.find(a)

UP = ['|', 'L', 'J']
BOTTOM = ['|', '7', 'F']
LEFT = ['-', 'J', '7']
RIGHT = ['-', 'L', 'F']

class Map:
    def __init__(self, N, M, MAP) -> None:
        self.N = N
        self.M = M
        self.MAP = MAP
        self.uf = UnionFind(N * M)
        
        for i in range(N):
            for j in range(M):
                if MAP[i][j] == 'S':
                    self.start = (i, j)
    
    @classmethod
    def read_map(cls):
        N, M = map(int, input().split())
        MAP = [list(input().strip()) for _ in range(N)]
        return cls(N, M, MAP)

    def print_map(self, filename=None):
        if filename is not None:
            with open(filename, 'w', encoding= 'utf-8') as f:
                MAP = deepcopy(self.MAP)
                d = {
                    'F':'┏',
                    'L':'┗',
                    '|':'┃',
                    '7':'┓',
                    'J':'┛',
                    '.':' ',
                    '-':'━',
                    'S':'S',
                    
                }
                d2 = {
                    'F':'╔',
                    'L':'╚',
                    '|':'║',
                    '7':'╗',
                    'J':'╝',
                    '.':' ',
                    '-':'═',
                    'S':'S',
                    
                }
                d_prime = {
                    'F':'╭',
                    'L':'╰',
                    '|':'│',
                    '7':'╮',
                    'J':'╯',
                    '.':' ',
                    '-':'─',
                    'S':'S',
                    
                }
                    
                    
                for i in range(self.N):
                    for j in range(self.M):
                        MAP[i][j] = d_prime[MAP[i][j]]
                for row in MAP:
                    f.write(''.join(row) + '\n')
        else:
            for row in self.MAP:
                print("".join(row))
    
    def fcode(self, i, j):
        return i * self.M + j
            
    def group_pipes(self):
        for i in range(self.N):
            for j in range(self.M-1):
                if self.MAP[i][j] in RIGHT and self.MAP[i][j+1] in LEFT:
                    self.uf.union(self.fcode(i, j), self.fcode(i, j+1))
        for j in range(self.M):
            for i in range(self.N-1):
                if self.MAP[i][j] in BOTTOM and self.MAP[i+1][j] in UP:
                    self.uf.union(self.fcode(i, j), self.fcode(i+1, j))
        for i in range(self.N):
            for j in range(self.M):
                self.uf.find(self.fcode(i, j))
                
    def filer_main_pipe(self, group_no):
        for i in range(self.N):
            for j in range(self.M):
                if self.MAP[i][j] == 'S':
                    continue
                if self.uf.find(self.fcode(i, j)) != group_no:
                    self.MAP[i][j] = '.'
                    


def part1():
    m = Map.read_map()
    m.group_pipes()
    
    n = []
    sx, sy = m.start
    
    if 0 < sx and m.MAP[sx-1][sy] in BOTTOM:
        n.append(m.uf.find(m.fcode(sx-1, sy)))
    if sx < m.N-1 and m.MAP[sx+1][sy] in UP:
        n.append(m.uf.find(m.fcode(sx+1, sy)))
    if 0 < sy and m.MAP[sx][sy-1] in RIGHT:
        n.append(m.uf.find(m.fcode(sx, sy-1)))
    if sy < m.M-1 and m.MAP[sx][sy+1] in LEFT:
        n.append(m.uf.find(m.fcode(sx, sy+1)))
    
    
    c = Counter(n)
    for i, v in c.items():
        if v == 2:
            group_no = i
            break
    
    cnt = 0
    for i in range(m.N * m.M):
        if m.uf.find(i) == group_no:
            cnt += 1
    print(ceildiv(cnt, 2))
    m.filer_main_pipe(group_no)
    m.print_map('map.txt')

def part2():
    # TODO
    pass

def main():
    # part1()
    # part2()
    pass

if __name__ == "__main__":
    main()