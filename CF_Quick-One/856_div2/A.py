def solve():
    N = int(input())
    strings = input().strip().split()
    big_strings = []

    for s in strings:
        if len(s) == N-1:
            big_strings.append(s)

    cases = []
    
    s1 = big_strings[0]
    s2 = big_strings[1]

    if s1[1:] == s2[:-1]:
        cases.append(s1 + s2[-1] )
    
    if s1[:-1] == s2[1:]:
        cases.append(s2 + s1[-1])

    cases = set(cases)
    suff_pre = set(strings)

    if len(cases) == 0:
        print('NO')
        return
    
    for case_string in cases:
        suff_pre_set = set()
        s = ''
        for c in case_string[:-1]:
            s += c
            suff_pre_set.add(s)
        
        s = ''
        for c in reversed(case_string[1:]):
            s = c + s
            suff_pre_set.add(s)
        if suff_pre_set == suff_pre:
            if case_string == case_string[::-1]:
                print('YES')
                return
    
    print('NO')


def main():
    for _ in range(int(input())):
        solve()

main()