from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class TableWidget(QTableWidget):
    def __init__(self, rows, columns, parent=None):
        super().__init__(rows, columns)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_V and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
            selection = self.selectedIndexes()

            if selection:
                row_anchor = selection[0].row()
                column_anchor = selection[0].column()
                clipboard = QApplication.clipboard()
                rows = clipboard.text().split('\n')
                for indx_row, row in enumerate(rows):
                    values = row.split('\t')
                    for indx_col, value in enumerate(values):
                        item = QTableWidgetItem(value)
                        self.setItem(row_anchor + indx_row, column_anchor + indx_col, item)
            super().keyPressEvent(event)

    def clearTableData(self):
        try:
            for row in range(self.rowCount()):
                tmp_col_txt=''
                for col in range(self.columnCount()):
                    self.setItem(row,col, QTableWidgetItem(''))
            return True
        except:
            return False

    def readTableData(self):
        tmp_all_txt=''
        try:
            for row in range(self.rowCount()):
                tmp_col_txt=''
                for col in range(self.columnCount()):
                    tmp_col_txt+=(self.item(row,col).text())+'\t'
                tmp_col_txt+='\n'
                #print(tmp_col_txt)
                if tmp_col_txt.replace('\t','').replace('\n','').strip()!='':
                    tmp_all_txt+=tmp_col_txt
        except:
            print("READ TABLE DATA FAIL!")
        print(tmp_all_txt)
        if tmp_all_txt!="":
            return tmp_all_txt
        else:
            return None