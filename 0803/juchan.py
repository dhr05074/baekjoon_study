import math


def probability(n, m, k):
    numerator = 0
    for i in range(k, m + 1):
        numerator += math.comb(n, i) * math.comb(n - i, m - i) * math.comb(n - m, m - i)
    denominator = math.comb(n, m) * math.comb(n, m)

    return numerator / denominator


inputs = input().split(" ")
n = int(inputs[0])
m = int(inputs[1])
k = int(inputs[2])

print(probability(n, m, k))
