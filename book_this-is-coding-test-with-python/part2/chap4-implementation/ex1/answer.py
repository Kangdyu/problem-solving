n = int(input())
commands = input().split()

rx = ry = 1


def left():
    global rx
    if rx == 1:
        return
    rx -= 1


def right():
    global rx
    if rx == n:
        return
    rx += 1


def up():
    global ry
    if ry == 1:
        return
    ry -= 1


def down():
    global ry
    if ry == n:
        return
    ry += 1


for command in commands:
    if command == "L":
        left()
    elif command == "R":
        right()
    elif command == "U":
        up()
    elif command == "D":
        down()

print(rx, ry)
