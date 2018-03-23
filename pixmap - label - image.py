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
'''
pixmap = QPixmap('Almahery.jpg').scaled(500,500)

label = QLabel(window)
label.setPixmap(pixmap)

window.resize(500,500)

'''

pixmap = QPixmap('Almahery.jpg')

label = QLabel(window)
label.setPixmap(pixmap)

window.resize(pixmap.width() , pixmap.height ())

window.show()
    
app.exec_()
