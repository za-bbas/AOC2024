from collections import Counter

left = []
right = []
for line in open("input.txt", "r"):
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

def partOne():
    left.sort()
    right.sort()
    print(sum(abs(left[i]-right[i]) for i in range(len(left))))

def partTwo():
    frequency = Counter(right)
    print(sum(num*frequency[num] for num in left))

partOne()
partTwo()