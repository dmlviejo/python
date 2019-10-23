import sys
from PyQt5 import QtCore, QtWidgets
from Base import Ui_MainWindow
from PyQt5 import QtSql
import sqlite3
from pprint import pprint

class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        
        
        self.create_DB()

        self.ui.pushButton.clicked.connect(self.print_data)
        self.model = None
        self.ui.pushButton.clicked.connect(self.sql_tableview_model)
        self.ui.pushButton_2.clicked.connect(self.sql_add_row)
        self.ui.pushButton_3.clicked.connect(self.sql_delete_row)
       

        
        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
  
    def sql_delete_row(self):
        if self.model:
          
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            
        else:
            self.sql_tableview_model()
              
                

    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
          
        else:
            self.sql_tableview_model()
          


    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('oficina.db')
        
        tableview = self.ui.tableView
      
        
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        tableview.setModel(self.model)
        
        self.model.setTable('office')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "officeCode")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "city")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "phone")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "addressLine1")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "addressLine2")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "state")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "country")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "postalCode")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "territory")
        


    def print_data(self):
        sqlite_file = 'oficina.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'office' ORDER BY officeCode")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       
        conn.close()       
        

    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('oficina.db')
        db.open()
    
        query = QtSql.QSqlQuery()
        
        
        query.exec_("create table office(officeCode varchar(10) primary key, "
                    "city varchar(50), phone varchar(50), addressLine1 varchar(50), addressLine2 varchar(50),"
                    "state varchar(50), country varchar(50), postalCode varchar(15), territory varchar(10))")
        
        query.exec_("insert into office values('1000b', 'Phoenix', '4181125637', 'Lourdes Crack', 'No me la se', 'vivo', 'stars', '37800', 'mex')")
        

if __name__ == "__main__":
    MainWindow_EXEC()
