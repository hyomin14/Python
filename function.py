#일반적인 함수
def add(a, b):           #a, b는 매개변수(함수에 입력으로 전달된 값을 받는 변수)
    return a + b

sum = add(3,4)           #3, 4는 인수(함수 호출할 때 전달하는 입력 값)
print(sum)

result = add(a=3,b=7)   #매개변수 지정하면 순서에 상관없이 사용가능.
print(result)



#입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)



#결괏값이 없는 함수(반환값은 오로지 return문에 의해서만 생성)
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3,4)
a = add(3,4)
print(a)                # None



#입력값, 결괏값 없는 함수
def say():
    print('Hi')

say()



#입력값 여러개
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10))
