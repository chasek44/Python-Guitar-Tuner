from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #1e1e1e;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeText = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.welcomeText.setGeometry(QtCore.QRect(130, 50, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Inter")
        self.welcomeText.setFont(font)
        self.welcomeText.setStyleSheet("color: white;")
        self.welcomeText.setObjectName("welcomeText")
        self.upArrow = QtWidgets.QLabel(parent=self.centralwidget)
        self.upArrow.setGeometry(QtCore.QRect(270, 155, 72, 59))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(36)
        self.upArrow.setFont(font)
        self.upArrow.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.upArrow.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upArrow.setObjectName("upArrow")
        self.downArrow = QtWidgets.QLabel(parent=self.centralwidget)
        self.downArrow.setGeometry(QtCore.QRect(270, 343, 72, 59))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(36)
        self.downArrow.setFont(font)
        self.downArrow.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.downArrow.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.downArrow.setObjectName("downArrow")
        self.noteText = QtWidgets.QLabel(parent=self.centralwidget)
        self.noteText.setGeometry(QtCore.QRect(270, 220, 72, 117))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.noteText.setFont(font)
        self.noteText.setStyleSheet("color: white;\n"
"color: #00ff41;\n"
"background-color: transparent;")
        self.noteText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.noteText.setObjectName("noteText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setStyleSheet("color: white;")
        self.menubar.setObjectName("menubar")
        self.menuInput = QtWidgets.QMenu(parent=self.menubar)
        self.menuInput.setStyleSheet("color: white;")
        self.menuInput.setObjectName("menuInput")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInput.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Guitar Tuner"))
        self.welcomeText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Inter\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:600;\">Python Guitar Tuner</span></p></body></html>"))
        self.upArrow.setText(_translate("MainWindow", "↑"))
        self.downArrow.setText(_translate("MainWindow", "↓"))
        self.noteText.setText(_translate("MainWindow", "A"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())