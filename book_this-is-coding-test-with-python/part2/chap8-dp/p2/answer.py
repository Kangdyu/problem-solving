# dp 풀이가 떠오르지 않음 ..
def attack(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array)
    if len(array) == 3:
        return max(array[0] + array[2], array[1])

    return max(array[0] + attack(array[2:]), array[1] + attack(array[3:]))


n = int(input())
array = list(map(int, input().split()))

print(attack(array))
