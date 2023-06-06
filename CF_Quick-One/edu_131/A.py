def n_one(m):
    return sum(m[0])+ sum(m[1])

def main():
    for _ in range(int(input())):
        row1 = list(map(int,input().strip().split()))
        row2 = list(map(int,input().strip().split()))
        m = [row1, row2]
        ones = n_one(m)


        if ones == 0:
            print(0)
        elif ones == 4:
            print(2)
        else:
            print(1)

if __name__ == "__main__":
    main()