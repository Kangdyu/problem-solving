# set(집합) 이용
n = int(input())
my = set(map(int, input().split()))
m = int(input())
ask = list(map(int, input().split()))

for i in ask:
    if i in my:
        print("yes", end=" ")
    else:
        print("no", end=" ")
