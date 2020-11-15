n, m, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

result = 0

biggest_index = 0
next_biggest_index = 0
for i in range(n):
    if nums[i] >= nums[biggest_index]:
        next_biggest_index = biggest_index
        biggest_index = i

for i in range(m):
    if (i + 1) % (k + 1) != 0:
        result += nums[biggest_index]
    else:
        result += nums[next_biggest_index]

print(result)
