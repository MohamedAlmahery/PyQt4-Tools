from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
app = QApplication(sys.argv)

table = QTableWidget()
table_item = QTableWidgetItem()
table.setWindowTitle('Table Title')

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
                          
table.show()
    
app.exec_()
