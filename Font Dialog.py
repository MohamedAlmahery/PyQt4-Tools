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

def show_font():
    Font = QFontDialog.getFont()
btn = QPushButton(window , text = 'color')
btn.move(80,80)
btn.resize(100,60)
btn.clicked.connect(show_font)

window.show()
    
app.exec_()
