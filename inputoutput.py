#input
#input()의 괄호 안에 질문을 입력하여 프롬프트 띄워줄 수 있음.
#input은 입력되는 모든 것을 문자열로 취급
"""
number = input("숫자를 입력하세요: ")
print(number)
"""

#output
#큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("life""is""too short")
print("life"+"is"+"too short")

#문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short")

#한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')           #end를 사용해 끝 문자 지정
