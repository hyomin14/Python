#range(a, b) --> a부터 b미만의 숫자
#marks3
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))
