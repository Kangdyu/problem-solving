# counting sort 이용
n = int(input())
my = [0] * 1000001

for i in input().split():
    my[int(i)] = 1

m = int(input())
ask = list(map(int, input().split()))

for i in ask:
    if my[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
