from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)

tabs = QTabWidget()
tab1 = QWidget() 
tab2 = QWidget()
tabs.addTab(tab1 , "window")
tabs.addTab(tab2 , "test")
vbox = QVBoxLayout(tabs)
button1 = QPushButton("Start")
button2 = QPushButton("End")
vbox.addWidget(button1)
vbox.addWidget(button2)
tab1.setLayout(vbox)

tabs.show()
app.exec_()
