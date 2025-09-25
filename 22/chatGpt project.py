import sys
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox
from common.styles import PUSH_BUTTON_STYLE

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # بدون إطار
        self.setStyleSheet("background-color: white; border-radius: 15px;")  # أطراف منحنية

        self.oldPos = self.pos()  # لتسهيل تحريك النافذة

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # --- Custom Title Bar ---
        title_bar = QHBoxLayout()
        self.title_label = QLabel("my project")
        self.title_label.setStyleSheet("color: #1E90FF; font-weight: bold; font-size: 15px;")
        title_bar.addWidget(self.title_label)
        title_bar.addStretch()

        minimize_btn = QPushButton("-")
        minimize_btn.setFixedSize(30, 30)
        minimize_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        minimize_btn.clicked.connect(self.showMinimized)
        title_bar.addWidget(minimize_btn)

        close_btn = QPushButton("x")
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("background-color: red; color: white; border-radius: 5px;")
        close_btn.clicked.connect(self.close)
        title_bar.addWidget(close_btn)

        layout.addLayout(title_bar)

        # --- Email ---
        emailLabel = QLabel("Email")
        layout.addWidget(emailLabel)
        layout.addWidget(QLineEdit())

        # --- Password ---
        passwordLabel = QLabel("Password")
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(passwordLabel)
        layout.addWidget(password_input)

        # --- CheckBox + Forget Password ---
        layout2 = QHBoxLayout()
        ch = QCheckBox("Remember me")
        layout2.addWidget(ch)
        FP = QLabel("Forget password?")
        layout2.addWidget(FP)
        layout.addLayout(layout2)

        # --- Login Button ---
        btn = QPushButton("Login")
        btn.setStyleSheet(PUSH_BUTTON_STYLE)
        layout.addWidget(btn)

        # --- Signup Label ---
        DontHave = QLabel("dont have account? signup")
        layout.addWidget(DontHave)

        self.setCentralWidget(widget)

    def __initUI__(self):
        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("Abd--Login")

    # --- لجعل النافذة قابلة للسحب ---
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()


if __name__ == "__main__":
    app = QApplication(sys.argv)

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
