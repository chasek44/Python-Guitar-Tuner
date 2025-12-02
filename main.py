from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 650)
        MainWindow.setStyleSheet("background-color: #1e1e1e;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.upArrow = QtWidgets.QLabel(parent=self.centralwidget)
        self.upArrow.setGeometry(QtCore.QRect(290, 170, 72, 59))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(36)
        self.upArrow.setFont(font)
        self.upArrow.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.upArrow.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upArrow.setObjectName("upArrow")
        self.downArrow = QtWidgets.QLabel(parent=self.centralwidget)
        self.downArrow.setGeometry(QtCore.QRect(290, 358, 72, 59))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(36)
        self.downArrow.setFont(font)
        self.downArrow.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.downArrow.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.downArrow.setObjectName("downArrow")
        self.noteText = QtWidgets.QLabel(parent=self.centralwidget)
        self.noteText.setGeometry(QtCore.QRect(290, 235, 72, 117))
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
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 591, 81))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: white;\n"
"background: transparent;")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.hzDisplay = QtWidgets.QLabel(parent=self.centralwidget)
        self.hzDisplay.setGeometry(QtCore.QRect(230, 440, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(18)
        self.hzDisplay.setFont(font)
        self.hzDisplay.setStyleSheet("color: white;\n"
"background: transparent;")
        self.hzDisplay.setText("")
        self.hzDisplay.setObjectName("hzDisplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setStyleSheet("color: white;")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Guitar Tuner"))
        self.upArrow.setText(_translate("MainWindow", "↑"))
        self.downArrow.setText(_translate("MainWindow", "↓"))
        self.noteText.setText(_translate("MainWindow", "A"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Inter\'; font-size:48pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:400;\">Python Guitar Tuner</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    from PyQt6 import QtCore, QtWidgets

    freq = 0

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    MainWindow.show()
    sys.exit(app.exec())


