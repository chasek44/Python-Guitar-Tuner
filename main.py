from PyQt6 import QtCore, QtGui, QtWidgets


# gui class
# designed with QTDesigner
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
        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(110, 430, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("""
        QPushButton {
                background: white;
                color: black;
                font-weight: bold;
                border-radius: 8px;
                padding: 6px;
        }
        QPushButton:checked {
        background: #00ff41;   /* bright green when active */
        color: black;
        }
        """)
        self.startButton.setObjectName("startButton")
        self.startButton.setCheckable(True)
        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(380, 430, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("""
        background: white;
        color: black;
        font-weight: bold;
        """)
        self.stopButton.setObjectName("stopButton")
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
        self.menuInput.addSeparator()
        self.menubar.addAction(self.menuInput.menuAction())

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
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))



if __name__ == "__main__":
    import sys
    import sounddevice as sd
    from PyQt6.QtGui import QAction

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # get inputs and fill menu
    ui.menuInput.clear()
    for i, device in enumerate(sd.query_devices()):
        if device['max_input_channels'] > 0:
            action = QAction(device['name'], MainWindow)
            action.triggered.connect(lambda checked, idx=i: print("Selected:", sd.query_devices(idx)['name']))
            ui.menuInput.addAction(action)

    # logic for stop and start recording buttons

    def on_start_toggled(state):
        if state:
            print("Recording started")
            # start recording here
        

    def on_stop_pressed():
        print("Recording stopped")
        # prevent infinite toggle loop
        ui.startButton.blockSignals(True)
        ui.startButton.setChecked(False)
        ui.startButton.blockSignals(False)
        # stop recording here

    # Prevent Start from un-toggling when clicked again
    def lock_start_if_unchecked(state):
        if not state:
            ui.startButton.setChecked(True)

    ui.startButton.toggled.connect(on_start_toggled)
    ui.stopButton.clicked.connect(on_stop_pressed)
    ui.startButton.toggled.connect(lock_start_if_unchecked)

    # Main logic for tuner

    def convToNote(freq):
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

        note_number = 12 * math.log2(freq / 440) + 49  
        note_number = round(note_number)
        
        note = (note_number - 1 ) % len(notes)
        note = notes[note]
    
        octave = (note_number + 8 ) // len(notes)
    
        return note, octave

    MainWindow.show()
    sys.exit(app.exec())
