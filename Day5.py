lines = [line.strip() for line in open("input5.txt", "r")]
order = {}
invalidUpdates = []
for line in lines:
    if line == "": break
    x, y = line.split("|")
    x, y = int(x), int(y)
    if x not in order:
        order[x] = set()
    order[x].add(y)

def partOne():
    updates = [[int(x) for x in line.split(",")] for line in lines[lines.index("")+1:]]
    total = 0
    seen = set()
    valid = True
    for update in updates:
        for i in range(len(update)):
            seen.add(update[i])
            if update[i] not in order: continue
            if not seen.isdisjoint(order[update[i]]):
                invalidUpdates.append(update)
                valid = False
                break
        if valid: total+=update[len(update)//2]
        seen.clear()
        valid = True
    print(total)

def partTwo():
    total = 0
    for update in invalidUpdates:
        data = {} # data is a dict that will contain the length of the order set for each update[i]
        for i in range(len(update)):
            if update[i] not in order: 
                data.update({0:update[i]})
                continue
            data.update({len(order[update[i]].intersection(set(update))):update[i]})
        l = sorted(data.keys())
        total += data[l[len(l)//2]]
        data.clear()
        l.clear()
    print(total)

partOne()
partTwo()