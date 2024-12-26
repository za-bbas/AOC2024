with open("input9.txt", "r") as f:
    line = f.readline().strip()
# check = [0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6]
# runningSum = [0]
# for i in range(1, len(check)):
#     runningSum.append(runningSum[i-1] + check[i]*i)
# print(runningSum)

def partOne():
    disks = [int(line[i]) for i in range(len(line))]
    total = 0
    index = 0
    i, j = 0, len(disks) - 1
    while i <= j:
        if i%2 == 0:
            for _ in range(disks[i]):
                total += ((i//2)) * index
                index += 1
        else:
            for _ in range(disks[i]):
                total += ((j//2)) * index
                disks[j] -= 1
                if disks[j] == 0: j-=2
                index += 1
        disks[i] = 0
        i += 1
    print(total)

partOne()