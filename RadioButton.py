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

Radio = QRadioButton(window , text = 'IOS')
Radio.move(100,150)
Radio.setChecked(True)

window.show()

app.exec_()
