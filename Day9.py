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
    """
    Basic idea is simple:
    iterate over file spans backwards (rtl), for each file span try to find leftmost big enough free span by iterating free spans forward (ltr).

    possible optimizations:
    1. Observation: if we couldn't find free span for file span of size N - it means that it won't be possible in future too
    There are only 9 possible file span sizes (1-9), so it makes sense to maintain simple array of flags per size. 
    If wee see in future file span of size N - we just skip it.
    2.follows from first one - if all nine possible file span sizes are impossible to move - we are done with whole defragmentation and can bail out early.
    3. Small optimization - we can calculate checksum of file span immediatelly after processing it.
    Ie we don't need another dedicated loop iterating over file spans again after defragmentation.
    """
    # TODO: implement above idea

partOne()
partTwo()