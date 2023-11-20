from math import pow
from PySide6.QtGui import QKeyEvent, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from window import Ui_MainWindow
from utils import isNumberOrDot, ACCEPT_KEYS, numberEquation, onlyNumer, isSpecialKeys


class MainWindow(QMainWindow, Ui_MainWindow):
    '''MainWidow herdando do arquivo gerado pelo QtDesigner'''
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self) # Obrigatorio
        self._buttons = self.findChildren(QPushButton)# Pegando todos os botões existentes na janela
        # Todos os botões que são numeros ou '.' :
        self.numberButtonsList = [btn for btn in self._buttons if isNumberOrDot(btn.text())]
        self._leftNumber = 0
        self._rightNumber = 0
        self._operator = None
        self._result = None
        self._equation = None
        self._insertKeyPressed() # Validação para permetir apenas numeros e operadores pelo teclado
        self.connections_buttons() # Conetando o evento click aos botões

    def _insertBtnTextToDisplay(self, btn : QPushButton):
        '''Insere no display da calculadora o numero clicado ou a função dos botçoes especiais'''
        def inner(): # Função Interna para Adiar o Retorno da Função
            buttonText = btn.text() # Pegando o Texto do Botão
            # Texto já existente no display mais o do botão
            numberDisplay = self.display.text() + buttonText
            if isSpecialKeys(buttonText): # Verifica se é um botão especial
                if buttonText == 'C':
                    self.defaultResult() # Reseta todos os campos
                if buttonText == '=':
                    self._rightNumber = self.display.text() # Pegando o Texto do display
                    equation = f'{self._leftNumber} {self._operator} {self._rightNumber}'
                    self._equation = equation
                    result = self.equationResult(equation)
                    self.result.setText(f'{equation} = {result:.2f}')
                    self.display.setText('')
                    return self.nextEquation(result)
                if buttonText == '<':
                    return self.display.backspace() # Evento para apagar unico caractere no display

            if not isNumberOrDot(buttonText): # Verifica se não é um numero ou '.'
                self.insertResultText(numberDisplay) # Insere o caracter na Label: Result
                self.display.setText('') # Reseta o Texto do Display
            return self.display.insert(buttonText) # Insere o texto do botão númerico no display
        return inner

    def equationResult(self, equation):
        '''Resultado da equação iformada'''
        if self._operator == '^': # Se o caractere for ^faz a exponenciação
            equationResult = pow(float(self._leftNumber), float(self._rightNumber))
        else:
            equationResult = eval(equation) # Le um texto e executa como codigo
            # Após várias validações pode-se usar o eval
        return equationResult

    def insertResultText(self, string):
        '''Insere na (Label: Result) a equação imcompleta ou completa'''
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
        ''' Após a primeira equação, o resultado fica salvo para continuar do mesmo número'''
        self._result = equationResult
        self._leftNumber = equationResult
        self._rightNumber = 0

    def defaultResult(self):
        ''' Reseta todos os campos para uma nova equação'''
        self._result = None
        self._leftNumber = 0
        self._rightNumber = 0
        self._operator = None
        self.display.setText('')
        self.result.setText('Resultado')

    def connections_buttons(self):
        '''Conectando o evento de click aos botões'''
        btn : QPushButton
        for btn in self._buttons:
            buttonSlot = self._insertBtnTextToDisplay(btn)
            btn.clicked.connect(buttonSlot)


    def setNumbersEquation(self, string):
        '''Definindo os números para a equação'''
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
        ''' Evento de teclado no display '''
        keyPressed = event.text()
        if keyPressed == '\r':
            self.insertResultText(self.display.text())
            self.display.setText('')

    def _insertKeyPressed(self):
        ''' Fazendo uma validação no evento de teclado para que seja somente válido inserir numeros e operadores'''
        validator = QRegularExpressionValidator() # Adcionando a validação em regex
        validator.setRegularExpression(ACCEPT_KEYS)
        self.display.setValidator(validator)




if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
