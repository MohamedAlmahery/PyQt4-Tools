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

result = QMessageBox.question(window,'message','Hi Brother do you want to Exit this program ?', QMessageBox.Yes | QMessageBox.No )
if result == QMessageBox.Yes :
    print('Exit') 
else:
    window.show()

app.exec_()
