from copy import deepcopy

class Map:
    def __init__(self, N, M, MAP) -> None:
        self.N = N
        self.M = M
        self.MAP = MAP

    @classmethod
    def read_map(cls):
        N, M = map(int, input().split())
        MAP = []
        for _ in range(N):
            MAP.append(list(input().strip()))
        return cls(N, M, MAP)
    
    def north_load(self):
        ANS = 0
        for i in range(self.N):
            for k in self.MAP[i]:
                if k == 'O':
                    ANS += self.N - i
        return ANS
    
    @staticmethod
    def shift_row_left(row):
        stone = []
        for i,e in enumerate(row):
            if e == 'O':
                stone.append(i)
        stone = stone[::-1]
        while stone:
            x = stone.pop()
            if x != 0 and row[x-1] == '.':
                row[x-1], row[x] = row[x], row[x-1]
                stone.append(x-1)
        return row
    
    def transpose(self):
        self.MAP = list(map(list, zip(*self.MAP)))
        self.N, self.M = self.M, self.N
        return self
    
    def flip_east_west(self):
        for i in range(self.N):
            self.MAP[i] = self.MAP[i][::-1]
        return self
    
    def west(self):
        for i in range(self.N):
            self.MAP[i] = self.shift_row_left(self.MAP[i])
        return self
    
    def east(self):
        self.flip_east_west()
        self.west()
        self.flip_east_west()
        return self
    
    def north(self):
        self.transpose()
        self.west()
        self.transpose()
        return self
    
    def south(self):
        self.transpose()
        self.east()
        self.transpose()
        return self
    
    def cycle(self, n = 1):
        for _ in range(n):
            self.north()
            self.west()
            self.south()
            self.east()
        return self
    
    def print_map(self):
        for row in self.MAP:
            print(''.join(row))
        print()
        return self
    
    def __str__(self) -> str:
        return "".join(["".join(row) for row in self.MAP])
    
    def copy(self):
        return deepcopy(self)

def part1():
    print(Map.read_map().north().north_load())
    
def part2(n):
    m = Map.read_map()
    start = m.copy()
    curr_state = str(m)
    d = {}
    d[curr_state] = 0 
    cycle_count = 0
    
    cycle_size = -1
    
    while True:
        m.cycle()
        cycle_count += 1
        
        curr_state = str(m)
        if curr_state in d:
            cycle_size = cycle_count - d[curr_state]
            break
        d[curr_state] = cycle_count
    
    
    cycle_start_number = d[curr_state]
    if n >= cycle_start_number:
        iterations = (n - cycle_start_number) % cycle_size
        for _ in range(iterations):
            m.cycle()
        print(m.north_load())
    else:
        for _ in range(n):
            start.cycle()
        print(start.north_load())
        
    

def main():
    # part1()
    # part2(1_000_000_000)
    pass
    
if __name__ == '__main__':
    main()    
