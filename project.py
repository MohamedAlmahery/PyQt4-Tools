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

'''
btn = QPushButton('Almahery' , window)
btn.resize(80,80)
btn.move(1,1)
btn.setToolTip('close')
btn.clicked.connect(exit)

result = QMessageBox.question(window,'message','Hi Brother do you want to open this program ?', QMessageBox.Yes | QMessageBox.No )
if result == QMessageBox.Yes :
    print('Exit') 
else:
    window.show()
    
text_box = QLineEdit(window)
text_box.move(90,10)
text_box.resize(100,50)
text_box.setPlaceholderText('Enter Your name ')
text_box.setText('PyQt')
text_box.setEchoMode(QLineEdit.Password)

check1 = QCheckBox(window , text ='IOS')
check1.move(10,90)
check1.setChecked(True)

combo = QComboBox(window)
combo.move(100,100)
combo.resize(280,40)
combo.addItems(['IOS' , 'Android' , 'windows8'])
combo.setCurrentIndex(2)

Radio = QRadioButton(window , text = 'IOS')
Radio.move(100,150)
Radio.setChecked(True)

open_file = QFileDialog.getOpenFileName(window , 'open File')
print(open_file)
with open(open_file , 'r') as f :
    print(f.read())

label = QLabel(window ,text = '<b> A <\b>')
label.move(90,90)

pb = QProgressBar(window)
pb.move(130,160)
pb.resize(200 , 30)
pb.setValue(40)
pb.setAlignment(Qt.AlignCenter)

slider = QSlider(Qt.Horizontal , window)
slider.move(200 , 100)
slider.resize(200,20)
slider.setValue(30)

def show_color():
    color = QColorDialog.getColor()
btn = QPushButton(window , text = 'color')
btn.move(80,80)
btn.resize(100,60)
btn.clicked.connect(show_color)

def show_font():
    Font = QFontDialog.getFont()
btn = QPushButton(window , text = 'color')
btn.move(80,80)
btn.resize(100,60)
btn.clicked.connect(show_font)

calen = QCalendarWidget(window)
data = calen.selectedDate()
label = QLabel(window)
label.move(250,250)
label.setText(data.toString())

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

table = QTableWidget(window)
table.resize(1000,1000)
table.setRowCount(6)
table.setColumnCount(5)
table.setItem(0,0 , QTableWidgetItem("A(1,1)"))
table.setHorizontalHeaderLabels(("D1 , D2, D3 , D4 , D5").split(','))
table.setVerticalHeaderLabels(("S1 , S2, S3 , S4 , S5 , S6").split(','))
table.horizontalHeader().setToolTip('colume')
table.horizontalHeaderItem(0).setToolTip('c1')
table.verticalHeader().setToolTip('s')
table.verticalHeaderItem(0).setToolTip('s1')
def click(row,col):
    print("click on : " + str(row) + "" + str(col))
table.cellClicked.connect(click)

#هنا التاب دى المفروض انها تملى شاشه 
tabs = QTabWidget()
tab1 = QWidget() 
tab2 = QWidget()
tabs.addTab(tab1 , "window")
tabs.addTab(tab2 , "test")
vbox = QVBoxLayout(tabs)
button1 = QPushButton("Start")
button2 = QPushButton("End")
vbox.addWidget(button1)
vbox.addWidget(button2)
tab1.setLayout(vbox)
tabs.show()

#تحديد حجم للصورة

pixmap = QPixmap('Almahery.jpg').scaled(500,500)

label = QLabel(window)
label.setPixmap(pixmap)

window.resize(500,500)

#هنا الحجم الطبييعى

pixmap = QPixmap('Almahery.jpg')

label = QLabel(window)
label.setPixmap(pixmap)

window.resize(pixmap.width() , pixmap.height ())


#مثال على الطبع

btn = QPushButton(window)
btn.move(100,100)
btn.resize(80,80)

def printstr():
    print('slot')

btn.clicked.connect(printstr)


#مثال على الاسليدر

sl = QSlider(window)
sl.setValue(10)
sl.move(200,100)

def change():
    sl.setValue(50)
    
btn.clicked.connect(change)


#الربط بين السلايدر وال lcd

lcd = QLCDNumber(window)
lcd.move(80,80)
lcd.resize(80,50)
lcd.display(0)

sl = QSlider(window)
sl.move(200,80)

sl.valueChanged.connect(lcd.display)


#البرط بين ال Dail و السلايدر

d = QDial(window)
d.move(80,70)
d.resize(70,70)
d.setValue(0)

sl = QSlider(window)
sl.move(200,80)

sl.valueChanged.connect(d.setValue)

'''

window.show()
app.exec_()
