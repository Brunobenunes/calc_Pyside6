from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from window import Ui_MainWindow
from utils import isNumberOrDot

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.buttons = self.findChildren(QPushButton)
        self.number_buttons_list = [btn for btn in self.buttons if isNumberOrDot(btn.text())]
        self.connections_buttons()

    def _insertBtnTextToDisplay(self : Ui_MainWindow, btn):
            def inner():
                buttonText = btn.text()
                self.display.insert(buttonText)
            return inner

    def connections_buttons(self):
        for btn in self.number_buttons_list:
             button_slot = self._insertBtnTextToDisplay(btn)
             btn.clicked.connect(button_slot)
        


if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    print(mainWindow.number_buttons_list)
    mainWindow.show()
    app.exec()