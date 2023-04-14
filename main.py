from layout_main import Ui_MainRecognizerWindow

from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication

import sys


class MainRecognizerWindow(QMainWindow):

    def __init__(self):
        super(MainRecognizerWindow, self).__init__()
        self.file_ch_res = None
        self.path_ch_res = None
        self.ui = Ui_MainRecognizerWindow()
        self.ui.setupUi(self)

        self.ui.button_file_choose.clicked.connect(self.evt_btn_file_ch)

        self.ui.button_path_choose.clicked.connect(self.evt_btn_path_ch)

        self.ui.button_file_choose.clicked.connect(self.evt_btn_anlz)

    def evt_btn_file_ch(self):
        res = QFileDialog.getOpenFileNames(self, "Choose file(-s)", "/Users/", "Audio File (*.mp3;*.wav)")[0]
        if res != []:
            self.file_ch_res = res
            res_st = ""
            for i in range(len(res)):
                if i > 0:
                    res_st += ", "
                res_st += res[i][res[i].rfind("/") + 1:]
            if len(res_st) > 37:
                self.ui.label_file_choose.setText(u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 "
                                                  u"\u0444\u0430\u0439\u043b\u044b: " + res_st[:37] + "...")
            else:
                self.ui.label_file_choose.setText(u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 "
                                                  u"\u0444\u0430\u0439\u043b\u044b: " + res_st)

    def evt_btn_path_ch(self):
        res = ""
        res = QFileDialog.getExistingDirectory(self, "Choose path", "/Users/")
        if res != "":
            self.path_ch_res = res
            if len(res) > 42:
                self.ui.label_path_choose.setText(u"\u041f\u0443\u0442\u044c "
                                                  u"\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f: " +
                                                  res[:42] + "...")
            else:
                self.ui.label_path_choose.setText(u"\u041f\u0443\u0442\u044c "
                                                  u"\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f: " +
                                                  res)

    def evt_btn_anlz(self):
        if self.file_ch_res is not None and self.path_ch_res is not None:
            


app = QApplication(sys.argv)
window_1 = MainRecognizerWindow()

window_1.show()

app.exec_()
