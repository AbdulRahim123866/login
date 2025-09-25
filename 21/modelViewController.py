# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import  QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
#
# #Model
# class CounterModel:
#     def __init__(self):
#         self._value=0
#         # self._observers=[]
#
#     def get_value(self):
#         return self._value
#
#     def set_value(self,value):
#         self._value=value
#         # self.notify_observers()
#
#     def increment(self):
#         self._value +=1
#         # self.notify_observers()
#
#     # def attach(self,observer):
#     #     self._observers.append(observer)
#
#     # def notify_observers(self):
#     #     for observer in self._observers:
#     #         observer.model_updated()
#
#
# #View
# class CounterView(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("MVS Example - Counter")
#         self.label=QLabel("0",self)
#         self.increment_button=QPushButton("Increment",self)
#         self.input_field=QLineEdit(self)
#         self.set_button=QPushButton("Set Value", self)
#
#         layout=QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.increment_button)
#         layout.addWidget(self.input_field)
#         layout.addWidget(self.set_button)
#         self.setLayout(layout)
#
#
#     def set_counter(self,value):
#         self.label.setText(str(value))
#
#     def get_input(self):
#         return self.input_field.text()
#
#
# #Controler
# class CounterController:
#     def __init__(self,model:CounterModel,view:CounterView):
#         self.model=model
#         self.view=view
#         # self.model.attach(self)
#         self.view.increment_button.clicked.connect(self.handel_increment)
#         self.view.set_button.clicked.connect(self.handle_set_value)
#         self.model_updated()
#     def handel_increment(self):
#         self.model.increment()
#
#     def handle_set_value(self):
#         try:
#             value=int(self.view.get_input())
#             self.model.set_value(value)
#         except ValueError:
#             pass
#
#     def model_updated(self):
#         self.view.set_counter(self.model.get_value())
#
#
# if __name__=="__main__":
#     import sys
#     app=QApplication(sys.argv)
#     model=CounterModel()
#     view=CounterView()
#     controller=CounterController(model,view)
#     view.show()
#     sys.exit(app.exec())


from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit


# View
class CounterView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MVC Example - Counter")
        self.label = QLabel("0", self)
        self.increment_button = QPushButton("Increment", self)
        self.input_field = QLineEdit(self)
        self.set_button = QPushButton("Set Value", self)


        layout = QVBoxLayout()


        layout.addWidget(self.label)
        layout.addWidget(self.increment_button)
        layout.addWidget(self.input_field)
        layout.addWidget(self.set_button)
        self.setLayout(layout)

    def set_counter(self, value):
        self.label.setText(str(value))

    def get_input(self):
        return self.input_field.text()

# Model
class CounterModel:
    def __init__(self):
        self._value = 0
        self._observers = []

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        self.notify_observers()

    def increment(self):
        self._value += 1
        self.notify_observers()

    def attach(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.model_updated()


# Controller
class CounterController:
    def __init__(self, model: CounterModel, view: CounterView):
        self.model = model
        self.view = view
        self.model.attach(self)

        # ربط الأزرار
        self.view.increment_button.clicked.connect(self.handle_increment)
        self.view.set_button.clicked.connect(self.handle_set_value)

        # تحديث أولي
        self.model_updated()

    def handle_increment(self):
        self.model.increment()

    def handle_set_value(self):
        try:
            value = int(self.view.get_input())
            self.model.set_value(value)
        except ValueError:
            pass

    def model_updated(self):
        self.view.set_counter(self.model.get_value())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    model = CounterModel()
    view = CounterView()
    controller = CounterController(model, view)
    view.show()
    sys.exit(app.exec())
