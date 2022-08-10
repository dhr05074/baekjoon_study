N = int(input())
A = list(map(int, input().split()))

max_length = []

for i in range(N):
    if i == 0:
        max_length.append(1)
    else:
        curr_max = 0
        for j in range(i):
            if A[i] > A[j] and max_length[j] > curr_max:
                curr_max = max_length[j]
        max_length.append(curr_max + 1)

print(max(max_length))
