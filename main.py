from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import scipy.fftpack
import sounddevice as sd
import time
import threading

SAMPLE_FREQ = 48000
WINDOW_SIZE = 48000
WINDOW_STEP = 3000
NUM_HPS = 5
POWER_THRESH = 1e-6
CONCERT_PITCH = 440
WHITE_NOISE_THRESH = 0.2

WINDOW_T_LEN = WINDOW_SIZE / SAMPLE_FREQ
SAMPLE_T_LENGTH = 1 / SAMPLE_FREQ
DELTA_FREQ = SAMPLE_FREQ / WINDOW_SIZE
OCTAVE_BANDS = [50,100,200,400,800,1600,3200,6400,12800,25600]

NOTES = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

# GUI Designed with PyQt6
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(650, 650)
        MainWindow.setStyleSheet("background-color: #1e1e1e;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.upArrow = QtWidgets.QLabel(self.centralwidget)
        self.upArrow.setGeometry(QtCore.QRect(290, 170, 72, 59))
        self.upArrow.setText("↑")
        self.upArrow.setStyleSheet("color: white; background: transparent;")
        f = QtGui.QFont("Inter", 36)
        self.upArrow.setFont(f)
        self.upArrow.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.downArrow = QtWidgets.QLabel(self.centralwidget)
        self.downArrow.setGeometry(QtCore.QRect(290, 358, 72, 59))
        self.downArrow.setText("↓")
        self.downArrow.setStyleSheet("color: white; background: transparent;")
        self.downArrow.setFont(f)
        self.downArrow.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(50, 20, 550, 120))
        font = QtGui.QFont("Inter", 40)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: white; background: transparent;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setText("Python Guitar Tuner")

        self.noteText = QtWidgets.QLabel(self.centralwidget)
        self.noteText.setGeometry(QtCore.QRect(200, 220, 250, 160))
        f2 = QtGui.QFont("Inter", 60)
        f2.setBold(True)
        self.noteText.setFont(f2)
        self.noteText.setStyleSheet("color: #00ff41; background: transparent;")
        self.noteText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.noteText.setText("A")

        self.hzDisplay = QtWidgets.QLabel(self.centralwidget)
        self.hzDisplay.setGeometry(QtCore.QRect(150, 440, 350, 80))
        self.hzDisplay.setStyleSheet("color: white; background: transparent;")
        self.hzDisplay.setFont(QtGui.QFont("Inter", 18))
        self.hzDisplay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)

# Logic for tuner and GUI updates

class TunerSignals(QtCore.QObject):
    update = QtCore.pyqtSignal(str, float, float)

signals = TunerSignals()

def find_closest_note(pitch):
    i = int(np.round(np.log2(pitch/CONCERT_PITCH)*12))
    closest_note = NOTES[i%12] + str(4 + (i + 9) // 12)
    closest_pitch = CONCERT_PITCH * 2**(i/12)
    return closest_note, closest_pitch

HANN = np.hanning(WINDOW_SIZE)
window_samples = np.zeros(WINDOW_SIZE)
note_buffer = ["X", "Y"]

def tuner_callback(indata, frames, time_info, status):
    global window_samples, note_buffer

    window_samples = np.concatenate((window_samples, indata[:, 0]))
    window_samples = window_samples[len(indata):]

    power = np.sum(window_samples * window_samples) / len(window_samples)
    if power < POWER_THRESH:
        return

    hann_samples = window_samples * HANN
    mag = np.abs(scipy.fftpack.fft(hann_samples)[:WINDOW_SIZE//2])

    for i in range(int(62 / (SAMPLE_FREQ/WINDOW_SIZE))):
        mag[i] = 0

    # HPS interpolation
    mag_ipol = np.interp(
        np.arange(0, len(mag), 1/NUM_HPS),
        np.arange(0, len(mag)),
        mag
    )
    mag_ipol /= np.linalg.norm(mag_ipol)

    hps = mag_ipol.copy()
    for i in range(NUM_HPS):
        tmp = hps[:len(mag_ipol)//(i+1)] * mag_ipol[::(i+1)]
        if not np.any(tmp):
            break
        hps = tmp

    idx = np.argmax(hps)
    freq = idx * (SAMPLE_FREQ / WINDOW_SIZE) / NUM_HPS
    freq = round(freq, 1)

    note, target = find_closest_note(freq)
    target = round(target, 1)

    note_buffer.insert(0, note)
    note_buffer.pop()

    # Only stable notes
    if note_buffer.count(note_buffer[0]) == len(note_buffer):
        signals.update.emit(note, freq, target)

def tuner_thread():
    with sd.InputStream(
        channels=1,
        samplerate=SAMPLE_FREQ,
        blocksize=WINDOW_STEP,
        callback=tuner_callback
    ):
        while True:
            time.sleep(0.01)

def update_gui(note, detected, target):
    ui.noteText.setText(note)
    ui.hzDisplay.setText(f"{detected} Hz (target {target})")

    # turn note green if close
    cents = 1200 * np.log2(detected / target)
    if abs(cents) <= 10:
        ui.noteText.setStyleSheet("color: #00ff41; background: transparent;")
    else:
        ui.noteText.setStyleSheet("color: white; background: transparent;")

    # arrow logic
    if cents < -10:
        ui.upArrow.setStyleSheet("color: #00ff41; background: transparent;")
        ui.downArrow.setStyleSheet("color: white; background: transparent;")
    elif cents > 10:
        ui.downArrow.setStyleSheet("color: #00ff41; background: transparent;")
        ui.upArrow.setStyleSheet("color: white; background: transparent;")
    else:
        ui.upArrow.setStyleSheet("color: white; background: transparent;")
        ui.downArrow.setStyleSheet("color: white; background: transparent;")


# Main app

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

signals.update.connect(update_gui)

thread = threading.Thread(target=tuner_thread, daemon=True)
thread.start()

sys.exit(app.exec())
