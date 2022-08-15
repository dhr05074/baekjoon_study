conditions = list(map(int, input().split()))
N = conditions[0]
K = conditions[1]

A = list(map(int, input().split()))

even = 0
odd = 0

max_len = 0
start = 0
end = 0

while start < N:
    while odd <= K and end < N:
        if A[end] % 2 == 0:
            even += 1
        else:
            odd += 1
        end += 1

    if max_len < even:
        max_len = even

    if A[start] % 2 == 0:
        even -= 1
    else:
        odd -= 1

    start += 1

print(max_len)
