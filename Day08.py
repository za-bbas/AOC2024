from itertools import combinations
# not a particualry trimmed solution, but it works
lines = [line.strip() for line in open("input8.txt", "r")]
frequencies = {}
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == ".": continue
        if lines[i][j] not in frequencies:
            frequencies[lines[i][j]] = set()
        frequencies[lines[i][j]].add((i,j))

def partOne():
    antinodes = set()
    xMax, yMax = len(lines[0]), len(lines)
    for key in frequencies.keys():
        for (x1, y1), (x2, y2) in combinations(frequencies[key], 2):
            dx, dy = x2 - x1, y2 - y1
            a, c = x2 + dx, x1 - dx
            b, d = y2 + dy, y1 - dy
            if (0 <= a < xMax) and (0 <= b < yMax): antinodes.add((a, b))
            if (0 <= c < xMax) and (0 <= d < yMax): antinodes.add((c, d))
    print(len(antinodes))

def partTwo():
    antinodes = set()
    xMax, yMax = len(lines[0]), len(lines)
    for key in frequencies.keys():
        for (x1, y1), (x2, y2) in combinations(frequencies[key], 2):
            dx, dy = x2 - x1, y2 - y1
            a, b = x2, y2
            while (0 <= a < xMax) and (0 <= b < yMax):
                antinodes.add((a, b))
                a, b = a + dx, b + dy
            a, b = x1, y1
            while (0 <= a < xMax) and (0 <= b < yMax):
                antinodes.add((a, b))
                a, b = a - dx, b - dy
    print(len(antinodes))

partOne()
partTwo()