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

window.show()
    
app.exec_()
