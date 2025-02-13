#TODO: optimize this solution, maybe by iterating instead of recursion! :)
# One idea I have is to just add all the possible things to a list and then check if the target is in that list somewhere
# Although I think this seems to have holes I'd have to plug at implementation...
lines = [line.strip() for line in open("input7.txt", "r")]

def partOne():
    print(sum(int(line.split(":")[0]) for line in lines if check(int(line.split(":")[0]), line.split(":")[1])))

def check(num, line):
    terms = [int(x) for x in line.strip().split(" ")]
    return recursive(terms, 0, 0, num)

def recursive(terms, index, current, target):
    if index == len(terms): return current == target
    if current > target: return False # slight optimization by pruning
    return (recursive(terms, index+1, current + terms[index], target) or 
            recursive(terms, index + 1, current * terms[index], target))

def partTwo():
    print(sum(int(line.split(":")[0]) for line in lines if check2(int(line.split(":")[0]), line.split(":")[1])))

def check2(num, line):
    terms = line.strip().split(" ")
    return (recursive2(terms, 0, 0, num, "+") or 
            recursive2(terms, 0, 0, num, "*") or
            recursive2(terms, 0, 0, num, "||"))

def recursive2(terms, index, current, target, op):
    if index == len(terms): return current == target
    if current > target: return False # slight optimization by pruning
    if op == "+": current = current + int(terms[index])
    if op == "*": current = current * int(terms[index])
    if op == "||": current = int(str(current) + terms[index])
    return (recursive2(terms, index + 1, current, target, "+") or 
            recursive2(terms, index + 1, current, target, "*") or
            recursive2(terms, index + 1, current, target, "||"))

partOne() # O(2^n) :|
partTwo() # O(3^n) :(