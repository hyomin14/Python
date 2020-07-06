#열 번 찍어 안 넘어가는 나무 없다

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")
print("=" * 50)

#홀수 출력
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
