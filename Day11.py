import math
from collections import defaultdict

with open("input11.txt", "r") as f:
    line = f.readline().strip()

def partOne(): #naive, could be made faster by using part2 code
    stones = line.split(" ")
    for _ in range(25):
        for i in range(len(stones)-1, -1, -1):
            if stones[i] == '0':
                stones[i] = '1'
            elif len(stones[i]) % 2 == 0:
                midpoint = len(stones[i])//2
                stone = stones[i]
                stones[i] = str(int(stone[midpoint:]))
                stones.insert(i, str(int(stone[:midpoint])))
            else:
                stones[i] = str(int(stones[i])*2024)
    print(len(stones))

def partTwo():
    stones = {int(stone) : 1 for stone in line.split(" ")}
    for _ in range(75):
        temp = defaultdict(int)
        for stone, num in stones.items():
            for newStone in blink(stone):
                temp[newStone] += num
        stones = temp
    
    print(sum(n for n in stones.values()))


def numLength(n):
    return int(math.log10(n)) + 1

def blink(n):
    if n == 0:
        return [1]
    elif numLength(n) % 2 == 0:
        # I copied this part from someone because I liked how they did it
        p = 10 ** (numLength(n) / 2)
        return [int(n / p) , int(n % p)]
    else:
        return [n * 2024]

partOne()
partTwo()