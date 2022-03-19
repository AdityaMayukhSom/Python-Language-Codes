n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
total_marks = 0
for marks in range(3):
    total_marks = total_marks + student_marks[query_name][marks]
average_marks = total_marks / 3
print(format(average_marks, ".2f"))
