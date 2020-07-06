#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합 구하기
result = 0
i = 1
while i <=1000:
    if i % 3 == 0:
        result = result + i
    i = i + 1
print(result)
print("=" * 50)

#while문을 사용하여 별을 표시하는 프로그램
i = 0
while True:
    i += 1
    if i > 5:
        break
    print('*' * i)
print("=" * 50)

#for문을 사용해 1부터 100까지 출력
for i in range(1,101):
    print(i)
print("=" * 50)

#for문을 사용하여 A학급의 평균 점수 구하기
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score          #점수 합

average = total / len(A)    #평균
print(average)
print("=" * 50)

#리스트 중 홀수에만 2를 곱하여 저장
"""
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
"""
numbers = [1,2,3,4,5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)


