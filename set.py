s1 = set([1,2,3])
s2 = set("Hello")
print(s1)
print(s2)           #중복 허용 X, 순서 X

# indexing X
l1 = list(s1)
print(l1[0])
t1 = tuple(s1)
print(t1[0])

#교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))
print(s2.intersection(s1))

#합집합
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))

#차집합
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))

#function
s1.add(7)           #1개의 값만 추가
print(s1)           #{1,2,3,4,5,6,7}

s1.update([8,9])    #여러 개의 값 추가
print(s1)           #{1,2,3,4,5,6,7,8,9}

s1.remove(2)
print(s1)           #[1,3,4,5,6,7,8,9]
