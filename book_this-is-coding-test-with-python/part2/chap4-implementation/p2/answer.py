n, m = map(int, input().split())
x, y, direction = map(int, input().split())
game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

game_map[x][y] = 2
visit_count = 1


def get_forward_coords(direction):
    nx = x
    ny = y

    if direction == 0:
        ny = y - 1
    elif direction == 1:
        nx = x + 1
    elif direction == 2:
        ny = y + 1
    elif direction == 3:
        nx = x - 1

    return nx, ny


def fix_direction(direction):
    if direction < 0:
        direction = 3
    elif direction > 3:
        direction = 0

    return direction


def turn_left():
    global direction
    direction = fix_direction(direction - 1)


def check_forward():
    nx, ny = get_forward_coords(direction)

    if ny < 0 or ny > m or nx < 0 or nx > n:
        return False

    if game_map[nx][ny] == 0:
        return True
    else:
        return False


def go_straight():
    global x, y, visit_count

    x, y = get_forward_coords(direction)
    game_map[x][y] = 2
    visit_count += 1


def check_back():
    nd = fix_direction(direction - 2)
    nx, ny = get_forward_coords(nd)

    if ny < 0 or ny > m or nx < 0 or nx > n:
        return False
    if game_map[nx][ny] == 1:
        return False
    else:
        return True


def go_back():
    global x, y, visit_count

    nd = fix_direction(direction - 2)
    x, y = get_forward_coords(nd)
    game_map[x][y] = 2
    visit_count += 1


turn_count = 0
while True:
    if turn_count == 3:
        if check_back() is True:
            go_back()
            turn_count = 0
        else:
            break
    turn_left()
    turn_count += 1
    if check_forward() is True:
        go_straight()
        turn_count = 0

print(visit_count)
