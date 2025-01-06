
with open("input9.txt", "r") as f:
    line = f.readline().strip()

def partOne():
    disks = [int(line[i]) for i in range(len(line))]
    total = index = 0
    i, j = 0, len(disks) - 1
    while i <= j:
        if i%2 == 0:
            for _ in range(disks[i]):
                total += (i//2) * index
                index += 1
        else:
            for _ in range(disks[i]):
                total += (j//2) * index
                disks[j] -= 1
                if disks[j] == 0: j-=2
                index += 1
        disks[i] = 0
        i += 1
    print(total)

def partTwo():
    L=[[],[]]
    pos = 0
    for idx,length in enumerate(map(int, line)):
        L[idx%2].append((pos,length))                 #L[0]: data, L[1]: free space
        pos += length
    for i,(dpos,dlen) in list(enumerate(L[0]))[::-1]: # look at data starting right
        for j,(spos, slen) in enumerate(L[1]):        # look at free space starting left
            if spos < dpos and slen >= dlen:          # can move data to free space
                L[0][i] = (spos, dlen)
                L[1][j] = (spos + dlen, slen - dlen)  # may create 0-length free space block, but that's ok
                break
    print(sum(v*dlen*(2*dpos + dlen - 1) for v, (dpos, dlen) in enumerate(L[0]))//2)


partOne()
partTwo()