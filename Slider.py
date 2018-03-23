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

slider = QSlider(Qt.Horizontal , window)
slider.move(1 , 1)
slider.resize(200,20)
slider.setValue(30)

window.show()
    
app.exec_()
