#사칙연산 클래스

"""
class FourCal:
    def setdata(self, first, second):               #메서드의 매개변수(메서드란 클래스 안에 구현된 함수)
        self.first = first
        self.second = second

        
a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 7)
#setdata 메서드의 첫번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달됨

print(a.first)                          #4
print(b.first)                          #3
#클래스로 만든 객체의 객체변수는 다른 객체의 객체변수와 상관없이 독립적인 값 유지
"""
class FourCal:
    def setdata(self, first, second):               
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()

a.setdata(4,2)
b.setdata(3,8)

print(a.add())              #6
print(a.mul())              #8
print(a.sub())              #2
print(a.div())              #2
print(b.add())              #11
print(b.mul())              #24
print(b.sub())              #-5
print(b.div())              #0.375
