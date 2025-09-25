import sys
import argparse

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLayout, QVBoxLayout, QHBoxLayout, \
    QGridLayout, QLabel, QTextEdit, QLineEdit, QTabWidget

from common.const import APP_NAME
from common.styles import PUSH_BUTTON_STYLE


# import calendar
# yy=2012
# mm=12
# print(calendar.month(yy,mm))

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(300,300,300,300)
        # self.setMaximumSize(600,600)
        # self.setMinimumSize(300,300)
        self.__initUI__()
        # btn=QPushButton("Login",)#self لتركيب الكبسسة عالفورم
        # self.setCentralWidget(btn)

        layout=QVBoxLayout()
        widget=QWidget()
        widget.setLayout(layout)
        btn = QPushButton("Login", )
        btn.setStyleSheet(PUSH_BUTTON_STYLE)
        layout.addWidget(btn)
        btn = QPushButton("Login", )
        layout.addWidget(btn)

        layout2=QHBoxLayout()
        layout.addLayout(layout2)
        layout2.addWidget(QPushButton("login"))
        layout2.addWidget(QPushButton("login"))
        layout2.addWidget(QPushButton("login"))
        layout2.addWidget(QPushButton("login"))
        layout3 = QGridLayout()
        layout.addLayout(layout3)
        layout3.addWidget(QPushButton("Login"),0,0)
        layout3.addWidget(QPushButton("Login"),1,2)
        layout3.addWidget(QPushButton("Login"),2,1)
        layout3.addWidget(QPushButton("Login"), 3, 2,1,2)

        layout.addWidget(QLabel("Hello"))
        layout.addWidget(QTextEdit())
        layout.addWidget(QLineEdit())

        wid=QTabWidget()
        wid.setTabPosition(QTabWidget.TabPosition.West)
        layout.addWidget(wid)
        # wid.addTab(QPushButton("1"),"Tap 1")
        # wid.addTab(QPushButton("2"),"Tap 2")
        wid.addTab(QTextEdit(), "Tap 1")
        wid.addTab(QTextEdit(), "Tap 2")


        self.setCentralWidget(widget)





    def __initUI__(self):
        # self.setFixedSize(QSize(500, 500))
        self.setWindowTitle(f"{APP_NAME}--Login")



def cli():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        '-n', '--integers',
        metavar='N',
        type=int,
        nargs="+",
        help='An integer for the accumulator'
    )
    parser.add_argument(
        '-c', '--config',
        type=str,
        default='config.ini',
        help='Path to config file (default: config.ini)'
    )
    return parser.parse_args()


def main(args):
    lst = [APP_NAME] + [f"{key}={value}" for key, value in vars(args).items() if value is not None]
    print(lst)

    app = QApplication(sys.argv)#Can be defined except one per application
    # window = QWidget()
    # window = QMainWindow()
    # window.setWindowTitle("My PyQt6 App")
    # window.show()
    #Login()
    form=Login()#هون ال referance تاعه جوا ال memoryفانت الك access عليها

    form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    args = cli()
    main(args)

