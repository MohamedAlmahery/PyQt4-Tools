from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.resize(400,350)
window.move(150,150)
window.setWindowTitle('Hello World')
window.setWindowIcon(QIcon('Almahery.jpg'))
window.setToolTip('The main program')

#مثال على الطبع

btn = QPushButton(window)
btn.move(100,100)
btn.resize(80,80)

def printstr():
    print('slot')

btn.clicked.connect(printstr)


#مثال على الاسليدر

sl = QSlider(window)
sl.setValue(10)
sl.move(200,100)

def change():
    sl.setValue(50)
    
btn.clicked.connect(change)

#الربط بين السلايدر وال lcd

lcd = QLCDNumber(window)
lcd.move(80,80)
lcd.resize(80,50)
lcd.display(0)

sl = QSlider(window)
sl.move(200,80)

sl.valueChanged.connect(lcd.display)


#البرط بين ال Dail و السلايدر

d = QDial(window)
d.move(80,70)
d.resize(70,70)
d.setValue(0)

sl = QSlider(window)
sl.move(200,80)

sl.valueChanged.connect(d.setValue)

window.show()
app.exec_()
