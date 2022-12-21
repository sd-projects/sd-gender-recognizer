from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(270, 217)
        MainWindow.setMinimumSize(QSize(260, 205))
        MainWindow.setMaximumSize(QSize(270, 220))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")
        font = QFont()
        font.setPointSize(10)
        self.pushButton_open.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_open)

        self.pushButton_open_2 = QPushButton(self.centralwidget)
        self.pushButton_open_2.setObjectName(u"pushButton_open_2")
        self.pushButton_open_2.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_open_2)

        self.label_em = QLabel(self.centralwidget)
        self.label_em.setObjectName(u"label_em")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_em.setFont(font1)
        self.label_em.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_em)

        self.label_txt = QLabel(self.centralwidget)
        self.label_txt.setObjectName(u"label_txt")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_txt.setFont(font2)
        self.label_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_txt)

        self.label_res = QLabel(self.centralwidget)
        self.label_res.setObjectName(u"label_res")
        self.label_res.setFont(font2)
        self.label_res.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_res)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_ok = QPushButton(self.centralwidget)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setMaximumSize(QSize(80, 16777215))
        self.pushButton_ok.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_ok)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label_em.raise_()
        self.pushButton_open.raise_()
        self.label_res.raise_()
        self.label_txt.raise_()
        self.pushButton_open_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GUI \u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.pushButton_open_2.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.label_em.setText("")
        self.label_txt.setText(QCoreApplication.translate("MainWindow", u"Result: ", None))
        self.label_res.setText("")
        self.pushButton_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
