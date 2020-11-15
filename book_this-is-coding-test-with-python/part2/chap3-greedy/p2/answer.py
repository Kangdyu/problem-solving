n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

result = 0
for row in data:
    min_value = min(row)
    if (min_value > result):
        result = min_value

print(result)
