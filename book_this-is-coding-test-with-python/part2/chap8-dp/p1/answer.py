d = dict()


def find_min_count(x):
    if x == 1:
        d[x] = 0
        return 0

    if d.get(x):
        return d[x]

    calc_list = [find_min_count(x - 1)]
    if x % 2 == 0:
        calc_list.append(find_min_count(x / 2))
    if x % 3 == 0:
        calc_list.append(find_min_count(x / 3))
    if x % 5 == 0:
        calc_list.append(find_min_count(x / 5))

    d[x] = 1 + min(calc_list)
    return d[x]


x = int(input())

print(find_min_count(x))
