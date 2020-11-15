def uul(x, y):
    if (x - 1) < 97 or (y - 2) < 1:
        return 0
    else:
        return 1


def uur(x, y):
    if (x + 1) > 104 or (y - 2) < 1:
        return 0
    else:
        return 1


def ddl(x, y):
    if (x - 1) < 97 or (y + 2) > 8:
        return 0
    else:
        return 1


def ddr(x, y):
    if (x + 1) > 104 or (y + 2) > 8:
        return 0
    else:
        return 1


def llu(x, y):
    if (x - 2) < 97 or (y - 1) < 1:
        return 0
    else:
        return 1


def lld(x, y):
    if (x - 2) < 97 or (y + 1) > 8:
        return 0
    else:
        return 1


def rru(x, y):
    if (x + 2) > 104 or (y - 1) < 1:
        return 0
    else:
        return 1


def rrd(x, y):
    if (x + 2) > 104 or (y + 1) > 8:
        return 0
    else:
        return 1


col, row = input()
x = ord(col)
y = int(row)

print(uul(x, y) + uur(x, y) + ddl(x, y) + ddr(x, y) +
      llu(x, y) + lld(x, y) + rru(x, y) + rrd(x, y))
