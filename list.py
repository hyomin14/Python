#list = [element1, element2, ...]

a = [1, 2, 3, ['a', 'b', 'c']]

#indexing
print(a[-2])
print(a[3])
print(a[3][1])

#slicing
print(a[0:2])
print(a[3:])
print(a[3][0:2])

#calculation
b = [4, 5, 6]
print(a + b)
print(b * 3)
print(len(a), len(b))

a[2] = 4
del a[3:]
print(a)

#function
print("=" * 50)
a.append([5,6]) #append(x)에서 x에 어떤 자료형도 추가 가능
print(a)

c = [1, 4, 3, 2]

c.sort()
print(c)        #[1, 2, 3, 4]

c.reverse()
print(c)        #[4, 3, 2, 1]

print(c.index(1))   #3

c.insert(0,7)
print(c)        #[7, 4, 3, 2, 1]

c.remove(4)
print(c)        #[7, 3, 2, 1]

print(c.pop())  #마지막 요소를 돌려주고 그 요소 삭제, pop(x)는 x번째 요소 돌려주고 그 요소 삭제
print(c)        #[7, 3, 2]

print(c.count(7))   #1
c.extend([4, 5])    #extend(x)에서 x에는 리스트만 올 수 있음
print(c)        #[7, 3, 2, 4, 5]
