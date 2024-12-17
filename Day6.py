import time
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
def partOne():
    r, c = point
    d = 0
    visited = set()
    visited.add((r,c))
    while 0<=r<len(lines) and 0<=c<len(lines[0]):
        nextR, nextC= r+directions[d][0], c+directions[d][1]
        if not (0<=nextR<len(lines) and 0<=nextC<len(lines[0])): break
        if lines[nextR][nextC] == "#":
            d = (d + 1) % 4
        else:
            r = nextR
            c = nextC
        if (r,c) not in visited:
            visited.add((r,c))
    print(len(visited))

def partTwo():
    """
    IDEA: check every possible position on the board (ik...) and see if the guard ends in a loop
    Check for loops by seeing if the guard has previously been in this position going in the same direction
    """
    # TODO: Implement solution
    visited = set()
    valid = set()
    d = 0 
    r, c = point
    for i in range(len(lines)):
        for j in range(len(lines)):
            r, c = point
            d = 0  # Reset direction
            visited = set()  # Reset visited
            # we will pretend that there is an object there, not actually change the map
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
start_time = time.time()
partTwo()
end_time = time.time()  # Record the end time
elapsed_time = end_time - start_time  # Calculate elapsed time

print(f"Program executed in {elapsed_time:.4f} seconds.")