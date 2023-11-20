from math import pow
from PySide6.QtGui import QKeyEvent, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from window import Ui_MainWindow
from utils import isNumberOrDot, ACCEPT_KEYS, numberEquation, onlyNumer, isSpecialKeys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._buttons = self.findChildren(QPushButton)
        self.numberButtonsList = [btn for btn in self._buttons if isNumberOrDot(btn.text())]
        self._leftNumber = 0
        self._rightNumber = 0
        self._operator = None
        self._result = None
        self._equation = None
        self._insertKeyPressed()
        self.connections_buttons()

    def _insertBtnTextToDisplay(self, btn : QPushButton):
        def inner():
            buttonText = btn.text()
            numberDisplay = self.display.text() + buttonText
            if isSpecialKeys(buttonText):
                if buttonText == 'C':
                    self.defaultResult()
                if buttonText == '=':
                    self._rightNumber = self.display.text()
                    equation = f'{self._leftNumber} {self._operator} {self._rightNumber}'
                    self._equation = equation
                    result = self.equationResult(equation)
                    self.result.setText(f'{equation} = {result:.2f}')
                    self.display.setText('')
                    return self.nextEquation(result)
                if buttonText == '<':
                    return self.display.backspace()

            if not isNumberOrDot(buttonText):
                self.insertResultText(numberDisplay)
                self.display.setText('')
            return self.display.insert(buttonText)
        return inner

    def equationResult(self, equation):
        if self._operator == '^':
            equationResult = pow(float(self._leftNumber), float(self._rightNumber))
        else:
            equationResult = eval(equation)
        return equationResult

    def insertResultText(self, string):
        self.setNumbersEquation(string)
        if self._rightNumber == None:
            self._rightNumber = '??'
        equation = f'{self._leftNumber} {self._operator} {self._rightNumber}'
        self._equation = equation
        if self._rightNumber != '??' and self._rightNumber is not None:
            equation_result = self.equationResult(equation)
            self.result.setText(f'{equation} = {equation_result:.2f}')
            return self.nextEquation(equation_result)
        self.result.setText(f'{equation} = ')

    def nextEquation(self, equationResult):
        self._result = equationResult
        self._leftNumber = equationResult
        self._rightNumber = 0

    def defaultResult(self):
        self._result = None
        self._leftNumber = 0
        self._rightNumber = 0
        self._operator = None
        self.display.setText('')
        self.result.setText('Resultado')

    def connections_buttons(self):
        btn : QPushButton
        for btn in self._buttons:
            buttonSlot = self._insertBtnTextToDisplay(btn)
            btn.clicked.connect(buttonSlot)


    def setNumbersEquation(self, string):
        if string == '':
            left_number = 0
            right_number = 0
            operator = self._operator

        else:
            left_number, operator, right_number = numberEquation(string)
        if self._result == self._leftNumber:
            right_number = left_number
            left_number = self._leftNumber
        if self._rightNumber == '??':
            self._rightNumber = onlyNumer(string)
            return None
        self._rightNumber = right_number
        self._leftNumber = left_number
        self._operator = operator


    def keyPressEvent(self, event: QKeyEvent) -> None:
        keyPressed = event.text()
        if keyPressed == '\r':
            self.insertResultText(self.display.text())
            self.display.setText('')

    def _insertKeyPressed(self):
        validator = QRegularExpressionValidator()
        validator.setRegularExpression(ACCEPT_KEYS)
        self.display.setValidator(validator)




if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
