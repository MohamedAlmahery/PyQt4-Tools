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

combo = QComboBox(window)
combo.move(100,100)
combo.resize(280,40)
combo.addItems(['IOS' , 'Android' , 'windows8'])
combo.setCurrentIndex(2)

window.show()
    
app.exec_()
