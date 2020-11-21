n, m = map(int, input().split())
kinds = []
for i in range(n):
    kinds.append(int(input()))
kinds.sort()

d = [10001] * (m + 1)

d[0] = 0
for kind in kinds:
    for i in range(kind, m + 1):
        if d[i - kind] != 10001:
            d[i] = min(d[i], d[i - kind] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
