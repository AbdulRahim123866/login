import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLayout, QVBoxLayout, QHBoxLayout, \
    QGridLayout, QLabel, QTextEdit, QLineEdit, QTabWidget, QCheckBox

from common.styles import PUSH_BUTTON_STYLE
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QMouseEvent

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 👈 بدون إطار
        self.setStyleSheet("background-color: white; border-radius: 15px;")  # 👈 أطراف منحنية

        widget=QWidget()
        layout=QVBoxLayout()
        widget.setLayout(layout)


        self.oldPos = self.pos()  # لتسهيل تحريك النافذة

        #email
        emailLabel=QLabel("Email")
        emailLabel.setStyleSheet("color: #1E90FF;")
        layout.addWidget(emailLabel)
        layout.addWidget(QLineEdit())

        #password
        passwordLabel=QLabel("Password")
        passwordLabel.setStyleSheet("color: #1E90FF;")
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(passwordLabel)
        layout.addWidget(password_input)

        layout2=QHBoxLayout()
        layout.addLayout(layout2)


        #check box+remember me
        # widget.setLayout(layout2)
        ch=QCheckBox("Remember me")
        ch.setStyleSheet("color: #1E90FF;")
        layout2.addWidget(ch)

        FP=QLabel("Forget password?")
        FP.setStyleSheet("color: #1E90FF;")
        layout2.addWidget(FP)

        #Login button
        btn=QPushButton("Login")
        btn.setStyleSheet(PUSH_BUTTON_STYLE)
        layout.addWidget(btn)
        #dont have account
        DontHave=QLabel("dont have account? signup")
        DontHave.setStyleSheet("color: #1E90FF;")
        layout.addWidget(DontHave)



        self.setCentralWidget(widget)


    def __initUI__(self):
        self.setFixedSize(QSize(400, 240))

        self.setWindowTitle("Abd--Login")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 👇 هنا نضيف ستايل عام
    app.setStyleSheet("""
            QLabel {
                color: #1E90FF;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #1E90FF;
                color: white;
                padding: 8px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1565C0;
            }
            QLineEdit {
                border: 1px solid #1E90FF;
                padding: 5px;
            }
        """)
    l = Login()
    l.show()
    sys.exit(app.exec())