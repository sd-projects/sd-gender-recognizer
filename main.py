from layouts.layout_main import Ui_MainRecognizerWindow

from scripts.audio_func import global_result

from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox

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

        self.ui.button_analyze.clicked.connect(self.evt_btn_anlz)

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
        if self.file_ch_res is None or self.path_ch_res is None:
            QMessageBox.critical(self, "Error", "Выберите аудиофайлы для анализа и путь сохранения резутата")
        else:
            n = len(self.file_ch_res)
            res = ["" for i in range(n)]

            for i in range(n):
                r1, r2, r3 = global_result(self.file_ch_res[i], 17, -3.021, 178.41533381607533)

                if int(r1) + int(r2) + int(r3) > 0:
                    p_res = "Male   - "
                else:
                    p_res = "Female - "

                if p_res[0].lower() == self.file_ch_res[i][self.file_ch_res[i].rfind("/") + 1]:
                    res[i] = p_res + self.file_ch_res[i] + "\n"
                else:
                    res[i] = p_res + "(err) - " + self.file_ch_res[i] + "\n"

                print(str(i + 1) + "/" + str(n))

            with open(self.path_ch_res + "/results.txt", mode="w", encoding="utf-8") as file:
                for i in range(n):
                    file.write(res[i])

            QMessageBox.information(self, "Completed",
                                    "Анализ аудиозаписей закончился, данные сохранены в файл 'results.txt'")


app = QApplication(sys.argv)
window_1 = MainRecognizerWindow()

window_1.show()

app.exec()
