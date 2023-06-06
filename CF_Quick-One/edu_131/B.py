def answer(n : int):
    d = 2
    array = [False]*n
    ans = ''

    for num,b in enumerate(array, 1):
        if b: continue
        while num<=n:
            array[num-1] = True
            ans += str(num)+' '
            num *= d

    return ans.strip()


def main():
    for _ in range(int(input())):
        n = int(input())
        print(2)
        print(answer(n))

if __name__ == "__main__":
    main()