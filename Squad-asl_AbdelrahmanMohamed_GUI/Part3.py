from ast import Not
from sqlite3 import Time
import subprocess
from subprocess import Popen, PIPE
from sys import stdout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from multiprocessing.connection import Listener
from multiprocessing import Process, current_process
import threading
from threading import Thread
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from functools import partial
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1229, 882)
        self.count = 0
        self.flag = False
        self.minutes = 0
        self.hours = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 730, 81, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/bckwrd-arrow.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 620, 81, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/frwrd-arrow.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 660, 41, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/right-arrow.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 660, 41, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icons/left-arrow.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 1231, 851))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icons/a.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 650, 101, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("icons/cwred.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 710, 101, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icons/ccwred.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 700, 51, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("icons/downward-arrowred.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 630, 51, 61))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("icons/upward-arrowred.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 500, 71, 101))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("icons/grapper-close.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 500, 101, 81))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("icons/grapper-close-horizontalpng.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(310, 520, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(650, 500, 101, 61))
        self.label_13.setObjectName("label_13")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(600, 500, 101, 61))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(550, 500, 101, 61))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(575, 500, 101, 61))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(630, 500, 101, 61))
        self.label_33.setObjectName("label_33")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 560, 71, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 560, 71, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 560, 71, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(480, 620, 91, 31))
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(480, 650, 151, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(480, 680, 151, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(480, 710, 151, 31))
        self.label_17.setObjectName("label_17")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(770, 560, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(940, 560, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(770, 610, 131, 31))
        self.label_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(770, 640, 250, 31))
        self.label_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_20.setObjectName("label_20")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 670, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(770, 700, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(770, 730, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(770, 760, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(70, 60, 491, 421))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(580, 60, 491, 421))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.comboBox.raise_()
        self.pushButton_4.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_18.raise_()
        self.label_21.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_4.clicked.connect(self.runScript)
        camThread = threading.Thread(target=self.cameraConn)
        camThread.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.addItem("Code 1")
        # self.comboBox.addItem("Code 2")
        # self.comboBox.addItem("Code 3")
        self.pushButton_5.clicked.connect(partial(self.pushed,self.pushButton_5.text() ))
        self.pushButton_6.clicked.connect(partial(self.pushed,self.pushButton_6.text() ))
        self.pushButton_7.clicked.connect(partial(self.pushed,self.pushButton_7.text() ))
        self.pushButton_8.clicked.connect(partial(self.pushed,self.pushButton_8.text() ))
        self.pushButton.clicked.connect(self.startTime)
        self.pushButton_2.clicked.connect(self.Pause)
        self.pushButton_3.clicked.connect(self.Re_set)
        MainWindow.closeEvent = self.closeEvent

    def closeEvent(self, event):
        self.conn.close()
        # self.conn.__exit__()
        event.accept()
    def pushed(self,text):
        self.label_20.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Current mode : {text}</span></p></body></html>")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Current speed:</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">00:00:00</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">00 :</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">00 :</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "start"))
        self.pushButton_2.setText(_translate("MainWindow", "stop"))
        self.pushButton_3.setText(_translate("MainWindow", "reset"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Depth:</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">X Acc:</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Y Acc:</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Z Acc:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Run"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Current Mode</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Current Mode:</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Autonomous"))
        self.pushButton_6.setText(_translate("MainWindow", "Depth hold"))
        self.pushButton_7.setText(_translate("MainWindow", "Stabilize"))
        self.pushButton_8.setText(_translate("MainWindow", "Manual"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">Camera 1</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">Camera 2</span></p></body></html>"))
    def showTime(self):
        if self.flag:
            self.count+= 1
        time = str(self.count / 10)
        self.label_13.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{time}</span></p></body></html>')
        self.label_30.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{self.minutes}</span></p></body></html>')
        self.label_31.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{self.hours}</span></p></body></html>')
        self.label_32.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">:</span></p></body></html>')
        self.label_33.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">:</span></p></body></html>')
        if time =="60.0":
                self.count = 0
                self.minutes += 1
                self.label_13.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{time}</span></p></body></html>')
                self.label_30.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{self.minutes} : </span></p></body></html>')
        if self.minutes == 60:
            self.count = 0
            self.minutes = 0
            self.hours += 1
            self.label_13.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{time}</span></p></body></html>')
            self.label_30.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{self.minutes} : </span></p></body></html>')
            self.label_31.setText(f'<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{self.hours} : </span></p></body></html>')


    def startTime(self):
        self.flag = True
    def Pause(self):
        self.flag = False
    def Re_set(self):
        self.flag = False
        self.count = 0
        self.minutes = 0
        self.label_13.setText(str(self.count))
        self.label_30.setText(str(self.minutes))
    
    
    def runScript(self) :
        if(self.comboBox.currentIndex()==0) :
            args=["python",'client.py']
            subprocess.Popen(args, stdout=subprocess.PIPE)
    def convertTopix(self,msg) :
        height ,width , channel = msg.shape
        bytesPerLine = 3*width
        img = QtGui.QImage(msg.data,width,height,bytesPerLine, QImage.Format.Format_RGB888).rgbSwapped()
        pix = QtGui.QPixmap(img)
        return pix
    def cameraInit(self) :
        address = ('localhost', 6000)
        listener = Listener(address,authkey=b'secret password')
        self.conn=listener.accept()
        print(f'connection accepted from {listener.last_accepted}')
    def cameraConn(self) :
        self.cameraInit()
        while True :
            msg = self.conn.recv()
            self.label_21.setPixmap(self.convertTopix(msg))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
