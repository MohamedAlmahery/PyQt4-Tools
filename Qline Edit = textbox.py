from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)

window = QWidget()
window.resize(400,350)
window.move(150,150)
window.setWindowTitle('Hello World')
window.setWindowIcon(QIcon('Almahery.jpg'))
window.setToolTip('The main program')

text_box = QLineEdit(window)
text_box.move(1,1)
text_box.resize(100,50)
text_box.setPlaceholderText('Enter Your name ')
text_box.setText('PyQt')
text_box.setEchoMode(QLineEdit.Password)

window.show()
    
app.exec_()
