import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 기본적인 UI 구성요소를 제공하는 위젯은 PyQt5.QtWidgets모듈에 포함됨

# 기본적인 윈도우 창 생성
class MyApp(QWidget): # MyApp 객체 선언, QWidget클래스 상속받음
    def __init__(self): # self는 MyApp 객체를 말함
        super().__init__() # 부모 클래스의 생성자 호출
        self.initUI() # init메서드 호출

    def initUI(self):# 창의 제목 설정, 창의 위치 이동, 크기 조절, 화면에 표시
        self.setWindowTitle('My First Application') # 타이틀바에 나타는 창 제목 설정
        self.move(300, 300) # 위젯을 스크린의 x=300px, y=300px 위치로 이동시킴
        self.resize(400, 200) # 위젯의 크기를 너비 400px, 높이 200px로 조절
        self.show() # 위젯을 스크린에 보여줌

if __name__ == '__main__': # __name__은 현재 모듈의 이름이 저장되는 내장 변수
    app = QApplication(sys.argv) # 객체 생성
    ex = MyApp() # MyApp() 객체 생성 -> QWidget클래스 상속받음
    sys.exit(app.exec_()) # 애플리케이션이 정상적으로 종료하기 위해 호출
    # app.exec_()호출은 프로그램이 종료될 때까지 계속 실행