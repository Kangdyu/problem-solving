import sys


def binary_search(target, array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1

    return False


n = int(input())
my = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
ask = list(map(int, sys.stdin.readline().rstrip().split()))


my.sort()
for i in ask:
    if binary_search(i, my) is True:
        print("yes", end=" ")
    else:
        print("no", end=" ")
