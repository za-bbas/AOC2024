lines = [list(line.strip()) for line in open("input6.txt","r")]
directions = [
    [-1, 0], # up
    [0, 1], # right
    [1, 0], # down
    [0, -1] # left
]
def partOne():
    r = c = -1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "^":
                r = i
                c = j
                break
    d = 0
    visited = set()
    visited.add((r,c))
    while 0<=r<len(lines) and 0<=c<len(lines[0]):
        if not (0<=r+directions[d][0]<len(lines) and 0<=c+directions[d][1]<len(lines[0])): break
        if lines[r+directions[d][0]][c+directions[d][1]] == "#":
            d = (d + 1) % 4
        else:
            r += directions[d][0]
            c += directions[d][1]
        if (r,c) not in visited:
            visited.add((r,c))
    print(len(visited))

def partTwo():
    """
    IDEA: check every possible position on the board (ik...) and see if the guard ends in a loop
    Check for loops by seeing if the guard has previously been in this position going in the same direction
    """
    # TODO: Implement solution

partOne()
