n, m = map(int, input().split())
lengths = list(map(int, input().split()))
lengths.sort(reverse=True)

height = max(lengths) - 1

result = 0
length_sum = 0
for i in range(height, 0, -1):
    for length in lengths:
        if length > i:
            length_sum += length - i
        else:
            break
    if length_sum >= m:
        result = i
        break
    else:
        length_sum = 0

print(result)
