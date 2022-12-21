from layouts.dlg_alg_layout import Ui_DlgAlgLayout
from layouts import dlg_fl_layout, dlg_tfl_layout
from layouts import dlg_str_layout, dlg_tstr_layout

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

import sys

import importlib.util


zero_file = ('', '')

g1 = ""

g2 = ""


def glob1(gl1):
    global g1
    g1 = gl1


def zp1():
    with open(file="results.txt", mode="w",encoding="utf-8") as wfile:
        wfile.writelines(g1)



def import_check(file_adr):
    spec = importlib.util.spec_from_file_location("module.name", str(file_adr))
    global imp_alg
    imp_alg = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = imp_alg
    spec.loader.exec_module(imp_alg)
    okn_vzv()


class AlgDlg(QMainWindow):
    def __init__(self):
        super(AlgDlg, self).__init__()
        self.ui = Ui_DlgAlgLayout()
        self.ui.setupUi(self)

        self.ui.alg_open_pushButton.clicked.connect(self.evt_alg_btn)

    def evt_alg_btn(self):
        res = QFileDialog.getOpenFileName(self, "Open file", "/Users/", "Python file (*.py;*.py3)")
        if res != zero_file:
            window_1.close()
            import_check(res[0])


class DataDlgFl(QMainWindow):
    def __init__(self):
        super(DataDlgFl, self).__init__()
        self.ui = dlg_fl_layout.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_open.clicked.connect(self.evt_Fl1_btn)

        self.ui.pushButton_ok.clicked.connect(self.evt_Fl1_ok_btn())

    def evt_Fl1_btn(self):
        res1 = QFileDialog.getOpenFileName(self, "Open file", "/Users/", imp_alg.imp[1])
        with open(file="cache1.txt", mode="w", encoding="utf-8") as wfile:
            wfile.writelines(res1)

    def evt_Fl1_ok_btn(self):
        try:
            with open(file="cache1.txt", mode="r", encoding="utf-8") as wfile:
                zn1 = wfile.read()
                print(imp_alg.Algorithm(zn1))
        except:
            print("eror")


class DataDlgTFl(QMainWindow):
    def __init__(self):
        super(DataDlgTFl, self).__init__()
        self.ui = dlg_tfl_layout.Ui_MainWindow()
        self.ui.setupUi(self)


class DataDlgFls(QMainWindow):
    def __init__(self):
        super(DataDlgFls, self).__init__()
        self.ui = dlg_fl_layout.Ui_MainWindow()
        self.ui.setupUi(self)


class DataDlgSt(QMainWindow):
    def __init__(self):
        super(DataDlgSt, self).__init__()
        self.ui = dlg_str_layout.Ui_MainWindow()
        self.ui.setupUi(self)


class DataDlgTSt(QMainWindow):
    def __init__(self):
        super(DataDlgTSt, self).__init__()
        self.ui = dlg_tstr_layout.Ui_MainWindow()
        self.ui.setupUi(self)


class DataDlgInt(QMainWindow):
    def __init__(self):
        super(DataDlgInt, self).__init__()
        self.ui = dlg_str_layout.Ui_MainWindow()
        self.ui.setupUi(self)


class DataDlgTInt(QMainWindow):
    def __init__(self):
        super(DataDlgTInt, self).__init__()
        self.ui = dlg_tstr_layout.Ui_MainWindow()
        self.ui.setupUi(self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_1 = AlgDlg()
    window_1.show()
    window_2 = DataDlgFl()
    window_3 = DataDlgTFl()
    window_4 = DataDlgFls()
    window_5 = DataDlgSt()
    window_6 = DataDlgTSt()
    window_7 = DataDlgInt()
    window_8 = DataDlgTInt()


    def okn_vzv():
        if str(imp_alg.imp[0]).lower() == "file":
            window_2.show()
        elif str(imp_alg.imp[0]).lower() == "two_files":
            window_3.show()
        elif str(imp_alg.imp[0]).lower() == "files":
            window_4.show()
        elif str(imp_alg.imp[0]).lower() == "str":
            window_5.show()
        elif str(imp_alg.imp[0]).lower() == "two_str":
            window_6.show()
        elif str(imp_alg.imp[0]).lower() == "int":
            window_7.show()
        elif str(imp_alg.imp[0]).lower() == "two_int":
            window_8.show()


    sys.exit(app.exec_())
