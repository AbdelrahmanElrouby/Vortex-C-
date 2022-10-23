from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton , QLabel , QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        # Load the file
        uic.loadUi("Squad-asl_AbdelrahmanMohamed_GUI\Photo.ui",self)
        # Setting a title
        self.setWindowTitle("Photo Viewer")
        # Define the widgets
        self.button = self.findChild(QPushButton,"pushButton") 
        self.label = self.findChild(QLabel,"label")
        # Clear the label 
        self.label.setText("")
        # connecting button clicked function to the button
        self.button.clicked.connect(self.clicked)
        # Show the app
        self.show()
    def clicked(self):
        # Opening the file
        fname,_ = QFileDialog.getOpenFileName(self , "Open Photo" , "" , "All Files(*);;PNG Files(*.PNG);;JPG Files(*.JPG)")
        self.pixmap = QPixmap(fname)
        # Showing the photo
        self.label.setPixmap(self.pixmap)

app = QApplication(sys.argv)

UIwindow = UI()
app.exec()