def add(a,b):
    return a+b
def sub(a,b):
    return a-b

#import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어
#import mod1.py(X)        import mod1(O)
#from 모듈이름 import 모듈함수 --> 모듈이름 붙이지 않고 모듈 함수 사용 가능
#from mod1 import add, sub == from mod1 import *   (* --> 모든 것)

if __name__=="__main__":
    print(add(1,4))
    print(sub(4,2))

#직접 이 파일을 실행했을 때는 if문이 참이 되어 다음 문장 수행됨.
#대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 if문이 거짓이 되어 다음 문장 수행되지 않음.
    
