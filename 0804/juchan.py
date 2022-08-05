def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def intersections(x1, y1, x2, y2, r1, r2):
    dist = distance(x1, y1, x2, y2)

    diff = abs(r1 - r2)
    sum = r1 + r2

    if dist == 0:
        if diff == 0:
            return -1
        else:
            return 0
    else:
        if diff < dist and dist < sum:
            return 2
        elif dist == diff or dist == sum:
            return 1
        elif diff > dist or sum < dist:
            return 0


test_case = int(input())
results = []
for i in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    results.append(intersections(x1, y1, x2, y2, r1, r2))

for i in range(test_case):
    print(results[i])
