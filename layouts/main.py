from layout_main import Ui_MainRecognizerWindow

from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication

import sys


class MainRecognizerWindow(QMainWindow):

    def __init__(self):
        super(MainRecognizerWindow, self).__init__()
        self.ui = Ui_MainRecognizerWindow()
        self.ui.setupUi(self)

        self.ui.button_file_choose.clicked.connect(self.evt_btn_file_ch)

        self.ui.button_file_choose.clicked.connect(self.evt_btn_path_ch)

        #self.ui.button_file_choose.clicked.connect(self.evt_btn_anlz)

    def evt_btn_file_ch(self):
        file_ch_res = QFileDialog.getOpenFileNames(self, "Choose file(-s)", "/Users/", "Audio File (*.mp3;*.wav)")
        print(file_ch_res)

    def evt_btn_path_ch(self):
        path_ch_res = QFileDialog.getExistingDirectory(self, "Choose path", "/Users/")
        print(path_ch_res)




app = QApplication(sys.argv)
window_1 = MainRecognizerWindow()

window_1.show()

app.exec_()
