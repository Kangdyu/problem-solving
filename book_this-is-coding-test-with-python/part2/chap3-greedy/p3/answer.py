n, k = map(int, input().split())

result = 0
while n != 1:
    if (n % k == 0):
        n //= k
    else:
        n -= 1
    result += 1

print(result)
