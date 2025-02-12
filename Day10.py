hikingMap = [line.strip() for line in open("input10.txt", "r")]
trailheads = [(i, j) for i in range(len(hikingMap)) 
              for j in range(len(hikingMap[0])) 
              if hikingMap[i][j] == "0"]
directions = [
    [-1, 0], # up
    [0, 1], # right
    [1, 0], # down
    [0, -1] # left
]
peaks = set()
part2Peaks = []

def partOneAndTwo():
    total = 0
    for trailhead in trailheads:
        dfs(trailhead)
        total += len(peaks)
        peaks.clear()
    print(total)
    print(len(part2Peaks))

def dfs(position):
    r, c = position
    if r < 0 or c < 0: return
    if r == len(hikingMap) or c == len(hikingMap[0]): return
    if hikingMap[r][c] == '9':
        peaks.add(position)
        part2Peaks.append(position)
        return
    for i in range(4):
        if r + directions[i][0] < 0 or r + directions[i][0] == len(hikingMap): continue
        if c + directions[i][1] < 0 or c + directions[i][1] == len(hikingMap[0]): continue
        if int(hikingMap[r][c]) == int(hikingMap[r + directions[i][0]][c + directions[i][1]]) - 1:
            dfs((r+directions[i][0],c+directions[i][1]))

partOneAndTwo()