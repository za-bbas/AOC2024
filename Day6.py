lines = [list(line.strip()) for line in open("input6.txt","r")]
directions = [
    [-1, 0], # up
    [0, 1], # right
    [1, 0], # down
    [0, -1] # left
]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "^":
            point = (i,j)
            break
path = set()

def partOne():
    r, c = point
    d = 0
    path.add((r,c))
    while 0<=r<len(lines) and 0<=c<len(lines[0]):
        nextR, nextC= r+directions[d][0], c+directions[d][1]
        if not (0<=nextR<len(lines) and 0<=nextC<len(lines[0])): break
        if lines[nextR][nextC] == "#":
            d = (d + 1) % 4
        else:
            r = nextR
            c = nextC
        if (r,c) not in path:
            path.add((r,c))
    print(len(path))

def partTwo():
    visited = set()
    valid = set()
    d = 0 
    r, c = point
    for i, j in path:
        r, c = point
        d = 0  # Reset direction
        visited = set()  # Reset visited
        if i == r and j == c: continue
        while 0<=r<len(lines) and 0<=c<len(lines[0]):
            nextR, nextC= r+directions[d][0], c+directions[d][1]
            if not (0<=nextR<len(lines) and 0<=nextC<len(lines[0])): break
            if lines[nextR][nextC] == "#" or (nextR == i and nextC == j):
                d = (d + 1) % 4
            else:
                r = nextR
                c = nextC
            if (r,c,d) not in visited:
                visited.add((r,c,d))
            else:
                valid.add((i,j))
                visited.clear()
                break
    print(len(valid))

partOne()
partTwo() # cut down from 1 min to 10 seconds