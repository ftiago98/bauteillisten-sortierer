import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QLabel, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from module.sort import sort

class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("mainWindow.ui",self)
        self.browse.clicked.connect(self.browsefiles)
        
    def browsefiles(self):
        filepath = QFileDialog.getOpenFileName(self, "Wähle die Bauteilliste","","Excel (*.xls *.xlsx)")
        savepath = QFileDialog.getExistingDirectory(self, "Wähle den Speicherort für die sortierte Datei", "")
        callback = sort(filepath[0], savepath)
        if callback == 'finish':
            msg = QMessageBox()
            msg.setWindowTitle("Fertig!")
            msg.setText("Die sortiere Datei wurde im ausgewählten Ordner abgespeichert. Du kannst die Anwendung schliessen.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Close)
            msg.buttonClicked.connect(self.close)
            msg.exec_()

app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(510)
widget.setFixedHeight(650)
widget.show()
sys.exit(app.exec_())