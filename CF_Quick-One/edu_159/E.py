from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict

class Trie:
    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.freq = 0

    def __init__(self): 
        self.root = self.Node()

    def insert(self, word):
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = self.Node()
            curr = curr.children[index]
            curr.freq += 1

    def search(self, word):
        curr = self.root
        ans = 0
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                return ans
            curr = curr.children[index]
            ans += curr.freq
        return ans


N = int(input())
total_chars = 0
root = Trie()
strings = []

for _ in range(N):
    string = input().strip()
    strings.append(string)
    root.insert(string)
    total_chars += len(string)


ANS = 0
for i in range(N):
    rev_string = strings[i][::-1]
    ANS += (len(rev_string) * N) + total_chars - (2 * root.search(rev_string))
print(ANS)