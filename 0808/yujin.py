N, K = map(int, input().split())
s = list(map(int, input().split()))

count = []
odd = []

for i in range(N):
    j = i
    count.append(0)
    odd.append(0)
    
    while (odd[i] <= K) and (j < N):
        if s[j] % 2 == 1:
            odd[i] = odd[i] + 1
        else:
            count[i] = count[i] + 1
        j = j + 1
        
print(max(count))