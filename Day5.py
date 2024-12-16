# you're given a guide on page ordering
# X|Y
# X must be before Y
# dictionary of sets maybe? 
# dict = {X:{Y,Z,W}}
# as you are going through lines, A,B,C,D...
# make each line a list, and remove an element from it and add it to a seen set
# then check if any of those in the seen set are in set in the dictionary

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
    # IDEA: need a way to find the middle of reorganized list
    # We can do that by seeing the relative order of the reorganized list
    # If you know how many numbers are supposed ot be behind a given number, it can be assigned that ranking
    # Then, you can just take the middle number
    """
    for example:
    [75,97,47,61,53]
    the ordering dictionary looks like this (this excludes all the numbers not in the list):
    {
    75:{53,47,61},
    97:{61,47,53,75},
    47:{53,61},
    61:{53}
    53:{}
    }
    Now we sort by how many terms are in the set, but reverse:
    [97,75,47,61,53]
    So we only need the median from the set lengths (or we can just sort and find the center term)!
    """
    # TODO: finish part 2
    total = 0
    for update in invalidUpdates:
        data = {} # l is a dict that will contain the length of the order set for each update[i]
        for i in range(len(update)):
            # update[i] is a term, I have to assign it a relative number
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