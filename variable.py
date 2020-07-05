a = [1,2,3]
print(id(a))            #메모리의 주소

b = a
print(id(b))
#[1,2,3] 리스트를 참조하는 변수가 b변수가 추가되어 2개로 늘어났다.
#b 변수 생성할 때 a 변수 값 가져오면서 a와는 다른 주소를 가리키도록

# 1. [:] 이용
b = a[:]
a[1] = 4
print(a)
print(b)
#a리스트 값을 변화시켜도 b 리스트에는 영향 끼치지 않음.

# 2. copy 모듈 이용
from copy import copy
b = copy(a)
print(b is a)
print("\n")
#Fale를 돌려주므로 b와 a는 서로 다른 객체를 가리킴.

#두 변수의 값 서로 바꾸기
c = 3
d = 5
c, d = d, c
print(c)
print(d)
