from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.buttons = self.findChildren(QPushButton)




if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()