#짝수, 홀수 판별 함수(is_odd)
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

#is_odd = lambda x: True if c % 2 == 1 else False

print(is_odd(3))                    #True
print(is_odd(4))                    #False


#입력으로 들어오는 모든 수의 평균
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2,3,4,5))       #3.0


#3과 6을 입력했을 때 9라는 결괏값을 출력하도록
input1 = input("첫번째 숫자를 입력하세요: ")
input2 = input("두번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)

