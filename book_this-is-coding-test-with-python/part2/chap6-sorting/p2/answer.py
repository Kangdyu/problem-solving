n = int(input())

students = []
for i in range(n):
    name, score = input().split()
    students.append((name, int(score)))

res = sorted(students, key=lambda student: student[1])

for student in res:
    print(student[0], end=" ")
