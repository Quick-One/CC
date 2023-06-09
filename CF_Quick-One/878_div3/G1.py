from sys import stdin
def input(): return stdin.readline()[:-1]

def clockwise(a):
    print('+ {}'.format(a), flush=True)
    return int(input())

def answer(a):
    print('! {}'.format(a), flush=True)

initial = int(input())

ele_index = dict()
ele_index[initial] = 0
last_index = 0
for i in range(999):
    new_ele = clockwise(1)
    if new_ele in ele_index:
        answer(len(ele_index))
        exit()
    last_index += 1
    ele_index[new_ele] = last_index

k = 0
while True:
    new_ele = clockwise(1000)
    k += 1
    if new_ele in ele_index:
        answer(last_index - ele_index[new_ele] + 1000 * k)
        exit()