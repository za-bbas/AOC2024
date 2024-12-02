from collections import Counter

left = []
right = []
for line in open("input.txt", "r"):
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

def partOne():
    sum = 0
    left.sort()
    right.sort()
    for i in range(len(left)):
        sum += abs(left[i]-right[i])
    print(sum)

def partTwo():
    similarity = 0
    frequency = Counter(right)
    for num in left:
        similarity += num * frequency[num]
    print(similarity)

partOne()
partTwo()