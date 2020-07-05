t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b' ,('ab', 'cd'))
#리스트는 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없음.

#indexing&slicing
print(t3[0])
print(t5[:2])

#calculation
print(t3 + t5)
print(t3 * 3)
print(len(t3))
