#문자열 슬라이싱
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print("=" * 50)

#a:b:c:d --> a#b#c#d    문자열의 replace 함수 사용
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
print("=" * 50)

#[1,3,5,4,2] --> [5,4,3,2,1]
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)
print("=" * 50)

#['Life', 'is', 'too', 'short'] --> Life is too short
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
print("=" * 50)

#(1,2,3) --> (1,2,3,4)
a = (1,2,3)
a = a + (4,)
print(a)
print("=" * 50)

#딕셔너리 a에서 'B'에 해당되는 값 추출      pop함수 사용
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(result)
print("=" * 50)

#a 리스트에서 중복 숫자 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)       #집합자료형으로 변환되면서 중복된 값들 사라짐.
b = list(aSet)
print(b)
