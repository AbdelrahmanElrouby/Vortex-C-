from PyQt5 import QtCore, QtGui, QtWidgets

n = True
class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(362, 567)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        self.Output.setFont(font)
        self.Output.setFrameShape(QtWidgets.QFrame.Box)
        self.Output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Output.setLineWidth(2)
        self.Output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Output.setObjectName("Output")
        self.modButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%") )
        self.modButton.setGeometry(QtCore.QRect(10, 120, 75, 75)) 
        font = QtGui.QFont()
        font.setPointSize(26)
        self.modButton.setFont(font)
        self.modButton.setObjectName("modButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget ,clicked = lambda: self.press_it("c"))
        self.cButton.setGeometry(QtCore.QRect(100, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.BackSpace = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.remove())
        self.BackSpace.setGeometry(QtCore.QRect(190, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.BackSpace.setFont(font)
        self.BackSpace.setObjectName("BackSpace")
        self.divButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("/"))
        self.divButton.setGeometry(QtCore.QRect(280, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divButton.setFont(font)
        self.divButton.setObjectName("divButton")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("7"))
        self.Button_7.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.mutButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("*"))
        self.mutButton.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.mutButton.setFont(font)
        self.mutButton.setObjectName("mutButton")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("8"))
        self.Button_8.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("9"))
        self.Button_9.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("4"))
        self.Button_4.setGeometry(QtCore.QRect(10, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.subButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("-"))
        self.subButton.setGeometry(QtCore.QRect(280, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.subButton.setFont(font)
        self.subButton.setObjectName("subButton")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("5"))
        self.Button_5.setGeometry(QtCore.QRect(100, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("6"))
        self.Button_6.setGeometry(QtCore.QRect(190, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("1"))
        self.Button_1.setGeometry(QtCore.QRect(10, 360, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.addButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(280, 360, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("2"))
        self.Button_2.setGeometry(QtCore.QRect(100, 360, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("3"))
        self.Button_3.setGeometry(QtCore.QRect(190, 360, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.equal())
        self.equalButton.setGeometry(QtCore.QRect(280, 440, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("0"))
        self.Button_0.setGeometry(QtCore.QRect(100, 440, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.negButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.neg())
        self.negButton.setGeometry(QtCore.QRect(10, 440, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.negButton.setFont(font)
        self.negButton.setObjectName("negButton")
        self.dpButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.dp())
        self.dpButton.setGeometry(QtCore.QRect(190, 440, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dpButton.setFont(font)
        self.dpButton.setObjectName("dpButton")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 26))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
    
    def equal(self) :
        out = self.Output.text()

        answer =eval(out)
        if str(answer) != str(out) :
            global n
            n = False
        self.Output.setText(str(answer))
    def neg(self) :
        out = self.Output.text()
        op = "+-%/*"
        x = -1
        i = 0
        while(i<=4) :
            if (op[i] in out) :
                x = max(x,out.rfind(op[i]))
            i+=1
        print (x)
        if out == "0" :
            pass
        else :
            if ( out.find("-") == 0 and (out.find("(") == 1) and (out.find(")") == (len(out)-1)) ):
                out = out.replace("(","")
                out = out.replace(")","",)
                out = out.replace("-","",1)
                self.Output.setText(f"{out}")
            elif x >0 or x == -1 :
                self.Output.setText(f"-({out})")
                pass
            else :
                out = out.replace("-","",1) 
                self.Output.setText(f"{out}")
    def remove(self) :
        out = self.Output.text()
        out = out[:-1]
        self.Output.setText(f"{out}")
    def dp(self) :
        out = self.Output.text()
        op = "+-%/*"
        x = -1
        i = 0
        while(i<=4) :
            if (op[i] in out) :
                x = max(x,out.rfind(op[i]))
            i+=1
        if x == -1 :
            if "." in out:
                pass
            else : 
                self.Output.setText(f"{out}.")
        else :
            if "." in out[x:] :
                pass
            else : 
                self.Output.setText(f"{out}.")
        x = -2
    def press_it(self,pressed) :
        out = self.Output.text()
        global n 
        if ( (not n) ) :
            if (pressed not in "+-%/*") :
                self.Output.setText("")
                n = True
        n = True
        if pressed == "c" :
            self.Output.setText("0")
        else :
            if self.Output.text() == "0" :
                self.Output.setText("")
            self.Output.setText(f"{self.Output.text()}{pressed}")
        return True
    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.Output.setText(_translate("Calculator", "0"))
        self.modButton.setText(_translate("Calculator", "%"))
        self.cButton.setText(_translate("Calculator", "C"))
        self.BackSpace.setText(_translate("Calculator", "B.S."))
        self.divButton.setText(_translate("Calculator", "/"))
        self.Button_7.setText(_translate("Calculator", "7"))
        self.mutButton.setText(_translate("Calculator", "x"))
        self.Button_8.setText(_translate("Calculator", "8"))
        self.Button_9.setText(_translate("Calculator", "9"))
        self.Button_4.setText(_translate("Calculator", "4"))
        self.subButton.setText(_translate("Calculator", "-"))
        self.Button_5.setText(_translate("Calculator", "5"))
        self.Button_6.setText(_translate("Calculator", "6"))
        self.Button_1.setText(_translate("Calculator", "1"))
        self.addButton.setText(_translate("Calculator", "+"))
        self.Button_2.setText(_translate("Calculator", "2"))
        self.Button_3.setText(_translate("Calculator", "3"))
        self.equalButton.setText(_translate("Calculator", "="))
        self.Button_0.setText(_translate("Calculator", "0"))
        self.negButton.setText(_translate("Calculator", "+/-"))
        self.dpButton.setText(_translate("Calculator", "."))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
