#함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):         #입력값을 전달받는 매개변수 a는 함수 안에서만 사용
    a = a + 1

vartest(a)
print(a)                #1

"""
def vartest(a):
    a = a + 1

vartest(3)
print(a)
#vartest 함수 안에서 a는 4가 되지만 함수 호출하고 난 뒤 print문장에서 입력받아야 하는 a라는 변수를 찾을 수 없기 때문에 오류 발생
함수 안에서 선언한 매개변수는 함수 안에서만 사용됨
"""

#함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)          #vartest 함수 안의 a와 함수 밖의 a는 다른 것
print(a)                #2

# 2. global 명령어 사용
a = 1
def vartest():
    global a            #함수 안에서 함수 밖의 a변수 사용하겠다는 뜻. 하지만 함수는 독립적으로 존재하는 것이 좋기 때문에 가급적 사용하지 말자
    a = a + 1

vartest()
print(a)                #2



#lambda(def와 동일한 역할) : 함수를 생성할 때 사용하는 예약어로 return 명령어가 없어도 결괏값을 돌려준다
#lambda 매개변수1, 매개변수2,...: 표현식
add = lambda a, b: a+b
print(add(3,4))

