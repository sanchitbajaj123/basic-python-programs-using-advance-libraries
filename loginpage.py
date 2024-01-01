import sys
from PyQt5.QtWidgets import *
from qtwidgets import PasswordEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *



    
def click():
        msg = QMessageBox(w)
        msg.setWindowTitle("welcome to my project")
        msg.setStyleSheet("background-color:white;color:RED")
        #msg.setIcon(QMessageBox.Warning)
        msg.setText("welcome to my projrct")
        o=msg.exec_()
        

        a=line.text()


    
    
mem=QApplication(sys.argv)
w=QWidget()
w.resize(400,200)
w.setWindowTitle("login page")
w.setStyleSheet("background-color:black;color:yellow")

vbox=QVBoxLayout(w)
lbl=QLabel()
lbl.setText("sign up")
lbl.setStyleSheet("QLabel{font-size: 30pt;}")
lbl.setAlignment(Qt.AlignCenter)
vbox.addWidget(lbl)


hbox=QHBoxLayout()
lbl1=QLabel()
lbl1.setText("user\t")
lbl1.setStyleSheet("border: 2px solid red;")
lbl1.setStyleSheet("QLabel{font-size: 20pt;}")

line=QLineEdit()
line.setFixedWidth(200)
#line.setFixedHeight(200)
hbox.addWidget(lbl1)
hbox.addWidget(line)
vbox.addLayout(hbox)
hbox1=QHBoxLayout()
lbl2=QLabel()
lbl2.setText("password")
lbl2.setStyleSheet("QLabel{font-size: 20pt;}")

p= PasswordEdit()
p.setFixedWidth(200)
#p.setFixedHeight(200)
hbox1.addWidget(lbl2)
hbox1.addWidget(p)
vbox.addLayout(hbox1)

hbox2=QHBoxLayout()
lbl2=QLabel()
lbl2.setText("mobile number")
lbl2.setStyleSheet("border: 2px solid red;")
lbl2.setStyleSheet("QLabel{font-size: 20pt;}")

line1=QLineEdit()
line1.setFixedWidth(200)
#line.setFixedHeight(200)
hbox2.addWidget(lbl2)
hbox2.addWidget(line1)
vbox.addLayout(hbox2)
hbox3=QHBoxLayout()

red = QRadioButton("male",w)
red.setChecked(False)
red.move(50, 50)
a='Male'
red.setFixedWidth(100)
hbox3.addWidget(red)
vbox.addLayout(hbox3)

hbox4=QHBoxLayout()

r= QRadioButton("female",w)
r.setChecked(False)
r.move(50, 50)
a='Female'
r.setFixedWidth(100)
hbox4.addWidget(r)
vbox.addLayout(hbox4)




btn=QPushButton("register")
btn.setStyleSheet("background-color:white;color:red;")
btn.setFont(QFont('Arial', 15))
btn.move(110,150)
vbox.addWidget(btn)
btn.clicked.connect(click)
b=line.text()

w.show()
