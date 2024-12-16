# you're given a guide on page ordering
# X|Y
# X must be before Y
# dictionary of sets maybe? 
# dict = {X:{Y,Z,W}}
# as you are going through lines, A,B,C,D...
# make each line a list, and remove an element from it and add it to a seen set
# then check if any of those in the seen set are in set in the dictionary

lines = [line.strip() for line in open("input5.txt", "r")]
def partOne():
    order = {}
    for line in lines:
        if line == "": break
        x, y = line.split("|")
        x, y = int(x), int(y)
        if x not in order:
            order[x] = set()
        order[x].add(y)
    updates = [[int(x) for x in line.split(",")] for line in lines[lines.index("")+1:]]
    total = 0
    seen = set()
    valid = True
    for update in updates:
        for i in range(len(update)):
            seen.add(update[i])
            if update[i] not in order: continue
            if not seen.isdisjoint(order[update[i]]):
                valid = False
                break
        if valid: total+=update[len(update)//2]
        seen.clear()
        valid = True
    print(total)


partOne()