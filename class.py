# class

"""
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))          3
print(add1(4))          7
print(add2(3))          3
print(add2(7))          10
"""

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))      #3         
print(cal1.add(4))      #7    
print(cal2.add(3))      #3    
print(cal2.add(7))      #10

#클래스는 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도면 
#cal1은 객체, Calculator의 인스턴스
