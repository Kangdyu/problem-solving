col, row = input()
x = ord(col) - ord('a') + 1
y = int(row)

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

results = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        results += 1

print(results)
