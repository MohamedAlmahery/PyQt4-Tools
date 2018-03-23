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

pb = QProgressBar(window)
pb.move(130,160)
pb.resize(200 , 30)
pb.setValue(40)
pb.setAlignment(Qt.AlignCenter)

window.show()

app.exec_()
