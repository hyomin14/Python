#Constructor (생성자)

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
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

a = FourCal(4, 2)
#객체에 초깃값을 설정해야할 필요가 있을 때 setdata와 같은 메서드를 호출하는 것보다 생성자를 구현하는 것이 안전
print(a.add())              #6
print(a.div())              #2.0

#Inheritance(기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속 사용)
#a의 b제곱
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
b = MoreFourCal(4, 2)
print(b.pow())              #16

#Overriding, 덮어쓰기
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

c = SafeFourCal(4, 0)
print(c.div())

#클래스 변수
class Family:
    lastname = "김"          #클래스 변수

print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

print(Family.lastname)
print(id(a.lastname))
print(id(b.lastname))
#클래스 변수는 클래스로 만든 모든 객체에 공유된다.

        
