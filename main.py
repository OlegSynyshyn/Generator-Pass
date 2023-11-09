# python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py

from ui import Ui_MainWindow
from PyQt5. QtWidgets import QMainWindow, QApplication
import random
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate)
        
    def generate(self):
        symbols = ""
        if self.ui.checkBox.isChecked():
            symbols += "0123456789"
        if self.ui.checkBox_2.isChecked():
            symbols += "qwertyuiopasdfghjklzxcvbnm"
        
        result = ""
        number = random.randint(8,20)
        if symbols == "":
            self.ui.label_2.setText("Помилка вибери вид пароля!")
        else:
            for i in range(number):
            
                result += random.choice(symbols)
            self.ui.label_2.setText("Результат: " + result)

app = QApplication([])
win=Main_Window()
win.show()
app.exec_()
