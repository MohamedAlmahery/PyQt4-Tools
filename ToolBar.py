from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.resize(400,350)
window.move(150,150)
window.setWindowTitle('Hello World')
window.setWindowIcon(QIcon('Almahery.jpg'))
window.setToolTip('The main program')

menu = window.menuBar()
file_menu = menu.addMenu('file')
edit_main = menu.addMenu('Edit')
exit_button = QAction(QIcon('Almahery.jpg') , 'Exit' , window)
exit_button.setShortcut('ctrl+s')
exit_button.triggered.connect(window.close)
file_menu.addAction(exit_button)
sub_menu = QMenu("Save As")
sub_menu.addAction(QIcon('Almahery.jpg'),'.png')
sub_menu.addAction('.jpg')
sub_menu.addAction('.psd')
file_menu.addMenu(sub_menu)

window.toolBar = window.addToolBar('Exit')
window.toolBar.addAction(exit_button)

window.show()
    
app.exec_()
