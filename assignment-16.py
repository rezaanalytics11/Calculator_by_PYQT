import PySide6
import sys

from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import math

class Helloworld(QMainWindow):
    def __init__(self):
        super(). __init__()


        loader=QUiLoader()
        self.ui=loader.load('untitled.ui',None)
        self.ui.show()
        self.result=0
        self.sign=''
        self.signn=''
        self.ui.sum.clicked.connect(self.sum)
        self.ui.minus.clicked.connect(self.minus)
        self.ui.multiply.clicked.connect(self.multiply)
        self.ui.divide.clicked.connect(self.divide)
        self.ui.equal.clicked.connect(self.equal)
        self.ui.percent.clicked.connect(self.percent)
        self.ui.sin.clicked.connect(self.sin)
        self.ui.cos.clicked.connect(self.cos)
        self.ui.tan.clicked.connect(self.tan)
        self.ui.cot.clicked.connect(self.cot)
        self.ui.log.clicked.connect(self.log)
        self.ui.AC.clicked.connect(self.AC)
        self.ui.DEL.clicked.connect(self.DEL)
        self.ui.sqrt.clicked.connect(self.sqrt)

        self.ui.decimal.clicked.connect(self.function_num_decimal)
        self.ui.btn_1.clicked.connect(self.function_num_1)
        self.ui.btn_2.clicked.connect(self.function_num_2)
        self.ui.btn_3.clicked.connect(self.function_num_3)
        self.ui.btn_4.clicked.connect(self.function_num_4)
        self.ui.btn_5.clicked.connect(self.function_num_5)
        self.ui.btn_6.clicked.connect(self.function_num_6)
        self.ui.btn_7.clicked.connect(self.function_num_7)
        self.ui.btn_8.clicked.connect(self.function_num_8)
        self.ui.btn_9.clicked.connect(self.function_num_9)
        self.ui.btn_10.clicked.connect(self.function_num_0)
        #self.ui.btn_1.clicked.connect(self.function_num_1)




    def function_num_1(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'1'
        self.ui.textbox.setText(new_text)

    def function_num_2(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'2'
        self.ui.textbox.setText(new_text)

    def function_num_3(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'3'
        self.ui.textbox.setText(new_text)

    def function_num_4(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'4'
        self.ui.textbox.setText(new_text)

    def function_num_5(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'5'
        self.ui.textbox.setText(new_text)

    def function_num_6(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'6'
        self.ui.textbox.setText(new_text)


    def function_num_7(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'7'
        self.ui.textbox.setText(new_text)


    def function_num_8(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'8'
        self.ui.textbox.setText(new_text)

    def function_num_9(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'9'
        self.ui.textbox.setText(new_text)

    def function_num_0(self):
        old_text=self.ui.textbox.text()
        new_text=old_text+'0'
        self.ui.textbox.setText(new_text)

    def function_num_decimal(self):
            old_text = self.ui.textbox.text()
            new_text = old_text + '.'
            self.ui.textbox.setText(new_text)
            self.signn = '.'



    def multiply(self):
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '*'

    def divide(self):
        if self.signn=='.':
            self.num1 = float(self.ui.textbox.text())
        else:
             self.num1=int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '/'

    def sum(self):
        if self.signn=='.':
            self.num1 = float(self.ui.textbox.text())
        else:
             self.num1=int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign='+'


    def minus(self):
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign ='-'

    def percent(self):
            if self.signn == '.':
                self.num1 = float(self.ui.textbox.text())
            else:
                self.num1 = int(self.ui.textbox.text())
            self.ui.textbox.setText('%'+str(self.num1/100))

    def sin(self):
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText(str(math.sin(math.radians(self.num1))))


    def cos(self):
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText(str(math.cos(math.radians(self.num1))))


    def tan(self):
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText(str(math.tan(math.radians(self.num1))))

    def cot(self):
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText(str(math.cot(math.radians(self.num1))))


    def log(self):
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText(str(math.log(self.num1)))

    def equal(self):
        self.num2=int(self.ui.textbox.text())
        if self.sign=='+':
         result=self.num2+self.num1
         self.ui.textbox.setText(str(result))

        elif self.sign=='-':
         result=-1*(self.num2-self.num1)
         self.ui.textbox.setText(str(result))

        elif self.sign=='*':
         result=self.num2*self.num1
         self.ui.textbox.setText(str(result))

        elif self.sign=='/':
         result=self.num1/self.num2
         self.ui.textbox.setText(str(result))


    def AC(self):
        self.ui.textbox.setText(" ")



    def DEL(self):
        old_text = self.ui.textbox.text()
        for i in range(len(old_text)):
           new_text=old_text[:i-1]
           self.ui.textbox.setText(new_text)



    def sqrt(self):
        old_text = self.ui.textbox.text()
        if self.signn == '.':
            self.num1 = float(self.ui.textbox.text())
        else:
            self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText(str(math.sqrt(self.num1)))




app= QApplication([])
window=Helloworld()

app.exec()




