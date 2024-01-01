import sys
from PyQt5.QtWidgets import *
from qtwidgets import PasswordEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMenu

mem=QApplication(sys.argv)
w=QMainWindow()

w.resize(400,200)
w.setWindowTitle("menu")
w.setStyleSheet("background-color:white;color:black")
w.show()
menubar=w.menuBar()
menubar.addMenu('menu1')
menubar.addMenu('menu2')
menubar.addMenu('menu3')
menubar.addMenu('menu4')


