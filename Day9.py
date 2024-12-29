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
    iterate over files backwards (rtl), for each file try to find leftmost big enough free span by iterating spans forward (ltr).

    possible optimizations:
    1. Observation: if we couldn't find free span for file span of size N - it means that it won't be possible in future too
    There are only 9 possible file sizes (1-9), so it makes sense to maintain simple array of flags per size. 
    If wee see in future file span of size N - we just skip it.
    2.follows from first one: if all nine possible file sizes are impossible to move, we are done with whole defragmentation and can bail out early.
    3. Small optimization: we can calculate checksum of file span immediatelly after processing it.
    """
    # TODO: implement above idea
    # files = [int(line[i]) for i in range(0, len(line), 2)]
    # spans = [int(line[i]) for i in range(1, len(line), 2)]
    # for i in range(len(files)-1, 0, -1):
    #     for j in range(len(spans)):
    #         if spans[i]>=files[i]:
    #             spans[i]-=files[i]
    #             final 
    # The above code wont work because it is neglecting that we can move files into a span that was already partially filled
    # A way to solve this could be to keep track of possible indices and values, so that we cna just sort it in the end


partOne()
partTwo()