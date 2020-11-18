def binary_search(target, max_height, array):
    start = 0
    end = max_height

    result = 0

    while start <= end:
        mid = (start + end) // 2
        cut = 0
        for i in array:
            if i > mid:
                cut += i - mid
            else:
                break

        if (target == cut):
            return mid
        elif (target > cut):
            end = mid - 1
        elif (target < cut):
            result = mid
            start = mid + 1

    return result


n, m = map(int, input().split())
lengths = list(map(int, input().split()))
lengths.sort(reverse=True)

max_height = max(lengths) - 1

print(binary_search(m, max_height, lengths))
