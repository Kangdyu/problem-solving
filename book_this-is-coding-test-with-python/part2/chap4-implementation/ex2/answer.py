n = int(input())

result = 0

for i in range(n + 1):
    if i == 3 or i == 13 or i == 23:
        result += 3600
        continue
    for j in range(60):
        if j == 3 or j == 13 or j == 23 or 39 >= j >= 30 or j == 43 or j == 53:
            result += 60
            continue
        for k in range(60):
            if k == 3 or k == 13 or k == 23 or 39 >= k >= 30 or k == 43 or k == 53:
                result += 1

print(result)
