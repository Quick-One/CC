from functools import reduce
from operator import and_, or_

def oi():
    return int(input())


def ti():
    return map(int, input().split())


def mi():
    return list(map(int, input().split()))


def solve():
    n = int(input())
    a = mi()
    print(reduce(or_, a) - reduce(and_, a))


for _ in range(oi()):
    solve()
