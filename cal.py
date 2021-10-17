
import math
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from random import randint




class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('calculator.ui', None)
        self.ui.show()


        self.ui.btn_0.clicked.connect(partial(self.numbers,'0'))
        self.ui.btn_1.clicked.connect(partial(self.numbers,'1'))
        self.ui.btn_2.clicked.connect(partial(self.numbers, '2'))
        self.ui.btn_3.clicked.connect(partial(self.numbers, '3'))
        self.ui.btn_4.clicked.connect(partial(self.numbers, '4'))
        self.ui.btn_5.clicked.connect(partial(self.numbers, '5'))
        self.ui.btn_6.clicked.connect(partial(self.numbers, '6'))
        self.ui.btn_7.clicked.connect(partial(self.numbers, '7'))
        self.ui.btn_8.clicked.connect(partial(self.numbers, '8'))
        self.ui.btn_9.clicked.connect(partial(self.numbers, '9'))




        self.ui.btn_equal.clicked.connect(self.equal) 
        self.ui.btn_dot.clicked.connect(self.dot)
        
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_muti.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)

        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_ac.clicked.connect(self.ac)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.btn_present.clicked.connect(self.percent)
        
       
    
    def numbers(self,num):
        self.ui.textbox.setText(self.ui.textbox.text() + num)
            
    def sum(self):
        self.op = '+'
        self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText('')

    def sub (self):
        self.op = '-'
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')

    def mul(self):
        self.op = '*'
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')    

    def div(self):
        self.op = '/'
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def sin(self):
        self.op ='sin'
        self.ui.textbox.setText("sin ")

    def cos(self):
        self.op = "cos"
        self.ui.textbox.setText("cos ")

    def tan(self):
        self.op = "cot"
        self.ui.textbox.setText("tan ")

    def sqrt(self):
        self.op = "sqrt"
        self.ui.textbox.setText("√ ")

    def log(self):
        self.op = "log"
        self.ui.textbox.setText("log ")

    def cot(self):
        self.op = "cot"
        self.ui.textbox.setText("cot")

    def percent(self):
        self.op = "%"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText(" ")       
        self.ui.textbox.setText(str(self.num1/100))

    def sign(self):
        self.op = "+/-"
        self.num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(-1 * self.num))
    
    def dot(self):
        for i in self.ui.textbox.text():
            if "." in self.ui.textbox.text():
                break
            else:
                self.ui.textbox.setText(self.ui.textbox.text() + ".")


    def ac(self):
        self.ui.textbox.setText("")  

    def equal(self):
        if self.op == "+":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1+self.num2))

        if self.op == "-":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 - self.num2))

        if self.op == "*":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 * self.num2))

        if self.op == "/":
            self.num2 = float(self.ui.textbox.text())
            if self.num2 !=0:
                self.ui.textbox.setText(str(self.num1/self.num2))
            else:
                self.ui.textbox.setText("Can't divide by zero")
        
        if self.op == "sin":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.sin(math.radians(self.num1))))


        if self.op == "cos":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.cos(math.radians(self.num1))))

        if self.op == "tan":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.tan(math.radians(self.num1))))

        if self.op == "sqrt":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.sqrt(self.num1)))

        if self.op == "log":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.log(self.num1)))

        if self.op == "cot":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            if self.num1 != 0:
                sin_1 = math.sin(math.radians(self.num1))
                cos_1= math.cos(math.radians(self.num1))
                self.ui.textbox.setText(str(cos_1/sin_1))
            else:
                self.ui.textbox.setText("Cannot divide by zero")
      

app = QApplication([])
window = Calculator()
app.exec_()       
        
