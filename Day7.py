lines = [line.strip() for line in open("input7.txt", "r")]

def partOne():
    print(sum(int(line.split(":")[0]) for line in lines if check(int(line.split(":")[0]), line.split(":")[1]) ))

def check(num, line):
    terms = [int(x) for x in line.strip().split(" ")]
    if recursive(terms, 0, 0, num): return True

def recursive(terms, index, current, target):
    if index == len(terms): return current == target
    return (recursive(terms, index+1, current + terms[index], target) or 
            recursive(terms, index + 1, current * terms[index], target))

partOne()