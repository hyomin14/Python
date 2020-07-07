#add and mul
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)                               #15

result = add_mul('mul', 1,2,3,4,5)
print(result)                               #120



#키워드 파라미터(입력값이 딕셔너리로 만들어져서 출력됨)
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)                         #{'a':1}
print_kwargs(name='foo', age = 3)           #{name:'foo','age':3}



#함수의 결괏값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)                   #result = (7, 12) --> 튜플 값
result1, result2 = add_and_mul(3,4)         #result1 = 7, result2 = 12



#매개변수에 초깃값 미리 설정(초기화 시키고 싶은 매개변수는 항상 뒤쪽에)
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27, False)
