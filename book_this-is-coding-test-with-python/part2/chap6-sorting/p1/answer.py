n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(sorted(nums, reverse=True))
