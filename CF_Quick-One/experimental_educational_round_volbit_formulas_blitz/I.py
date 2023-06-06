n = int(input())
if n == 3:
    print(24)
else:
    a = 4 * 3 * pow(4, n - 3)
    a *= 2
    a += 3 * 3 * 4 * pow(4, n - 4) * (n - 3)
    print(a)