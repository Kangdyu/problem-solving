# dp 풀이가 떠오르지 않음 ..
n, m = map(int, input().split())
kinds = []
for i in range(n):
    kinds.append(int(input()))

kinds.sort(reverse=True)

count = 0
for kind in kinds:
    while m >= kind:
        m -= kind
        count += 1
    if m == 0:
        break

if m != 0:
    count = -1

print(count)
