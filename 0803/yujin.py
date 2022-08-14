import math

def nCm(n, m):
    return math.factorial(n) // math.factorial(m) // math.factorial(n-m)
    
nums = input().split()
N = int(nums[0])
M = int(nums[1])
K = int(nums[2])

p = 0
for i in range(K,M+1):
    p = p + nCm(M,i) * nCm(N-M, M-i)
print(p/nCm(N,M))