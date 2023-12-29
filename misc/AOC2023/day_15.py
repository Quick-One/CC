from sys import stdin
def input(): return stdin.readline()[:-1]


def hashalgo(string):
    val = 0
    for i in string:
        val += ord(i)
        val *= 17
        val %= 256
    return val


class BOX:
    def __init__(self) -> None:
        self.lens = []
        self.focus = {}

def part1():
    ans = sum([hashalgo(i) for i in input().strip().split(',')])
    print(ans)


def part2():
    BOXES = [BOX() for _ in range(256)]
    string = input().strip().split(',')
    for command in string:
        if command[-1] == '-':
            label = command[:-1]
            idx = hashalgo(label)
            box = BOXES[idx]
            if label in box.lens:
                box.lens.remove(label)
                del box.focus[label]
        else:
            label = command[:-2]
            idx = hashalgo(label)
            box = BOXES[idx]
            if label not in box.lens:
                box.lens.append(label)
                box.focus[label] = int(command[-1])
            else:
                box.focus[label] = int(command[-1])
    ANS = 0
    for v, box in enumerate(BOXES, 1):
        for i, label in enumerate(box.lens, 1):
            ANS += i * box.focus[label] * v
    print(ANS)


def main():
    # part1()
    # part2()
    pass


if __name__ == '__main__':
    main()
