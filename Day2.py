lines = [line.strip() for line in open("input.txt", "r")]

def partOne():
    safe = 0
    nums = []
    for line in lines:
        nums = [int(num) for num in line.split()]
        safe += calcSafe(nums)
    print(safe)

def partTwo():
    nums = []
    safe = 0
    for line in lines:
        nums = [int(num) for num in line.split()]
        if calcSafe(nums):
            safe += 1  # Already safe
            continue
        for i in range(len(nums)):  # Try removing each element
            modified = nums[:i] + nums[i+1:]
            if calcSafe(modified):
                safe += 1
                break
    print(safe)

def calcSafe(nums:list):
    increasing = decreasing = False
    inRange = True
    for i in range(len(nums)-1):
        if not 1 <= abs(nums[i] - nums[i+1]) <= 3: inRange = False
        if nums[i] > nums[i+1]: decreasing = True
        if nums[i] < nums[i+1]: increasing = True
    if inRange and (increasing ^ decreasing): return 1
    return 0

partOne()
partTwo()