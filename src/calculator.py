import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):              # Janela Principal 
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        
        self.show()
    def keypad(self):                       # Container Vazio
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Botões 
        result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Digitar')
        btn_clear = qtw.QPushButton('Limpar')
        btn_9 = qtw.QPushButton('9')
        btn_8 = qtw.QPushButton('8')
        btn_7 = qtw.QPushButton('7')
        btn_6 = qtw.QPushButton('6')
        btn_5 = qtw.QPushButton('5')
        btn_4 = qtw.QPushButton('4')
        btn_3 = qtw.QPushButton('3')
        btn_2 = qtw.QPushButton('2')
        btn_1 = qtw.QPushButton('1')
        btn_0 = qtw.QPushButton('0')
        btn_plus = qtw.QPushButton('+')
        btn_mins = qtw.QPushButton('-')
        btn_mult = qtw.QPushButton('*')
        btn_divid = qtw.QPushButton('/')

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()