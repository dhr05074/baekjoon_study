import math

n = int(input())

for i in range(n):
    nums = input().split()
    x1 = int(nums[0])
    y1 = int(nums[1])
    r1 = int(nums[2])
    x2 = int(nums[3])
    y2 = int(nums[4])
    r2 = int(nums[5])
    
    if (x1 == x2) and (y1 == y2) and (r1 == r2):
        print(-1)
    else:
        R = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
        if (R > r1) and (R > r2):
            r = r1 + r2
            if r > R:
                print(2)
            elif r == R:
                print(1)
            else:
                print(0)
        else:
            r = abs(r1 - r2)
            if r > R:
                print(0)
            elif r == R:
                print(1)
            else:
                print(2)