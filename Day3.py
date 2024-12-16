import re

line = ''.join([line.strip() for line in open("input.txt","r")])
pattern = r"mul\((\d+),(\d+)\)"

def partOne():
    print(sum(int(a) * int(b) for a, b in re.findall(pattern, line)))

def partTwo():
    do = line.split("do()")
    mul = ""
    for op in do:
        mul+= op.split("don't()")[0]
    print(sum(int(a) * int(b) for a, b in re.findall(pattern, mul)))

partOne()
partTwo()