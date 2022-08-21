def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1

T = int(input())
for i in range(T):
    nums = input().split()
    N = int(nums[0])
    M = int(nums[1])
    b = fact(M)/(fact(N) * fact(M-N))
    print(int(b))