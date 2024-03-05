## Ex 3-2. 어플리케이션 아이콘 넣기

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DDoS Detection Program')
        self.setWindowIcon(QIcon('Detection.png')) # QIcon 객체 생성 후 파라미터에 보여질 이미지를 입력
        self.setGeometry(300, 300, 300, 200) # 창의 위치와 크기 설정(앞에 2개는 창의 x,y위치 / 뒤에 2개는 너비, 높이)
        # setGeometry()메서드는 move()와 resize()메서드를 하나로 합친 것과 같음
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())