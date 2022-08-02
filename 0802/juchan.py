import math

test_case = int(input())
results = []
for i in range(test_case):
    sites = input().split(" ")
    n = int(sites[0])
    m = int(sites[1])

    if n == 0 or m == 0:
        results.append(0)
        continue

    result = math.factorial(m) // math.factorial(m - n) // math.factorial(n)
    results.append(result)

for i in range(test_case):
    print(results[i])
