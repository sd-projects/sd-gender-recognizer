from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Ui_DlgAlgLayout(object):
    def setupUi(self, DlgAlgLayout):
        if not DlgAlgLayout.objectName():
            DlgAlgLayout.setObjectName(u"DlgAlgLayout")
        DlgAlgLayout.resize(360, 110)
        DlgAlgLayout.setMinimumSize(QSize(350, 100))
        DlgAlgLayout.setMaximumSize(QSize(380, 125))
        self.centralwidget = QWidget(DlgAlgLayout)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.choose_label = QLabel(self.centralwidget)
        self.choose_label.setObjectName(u"choose_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_label.sizePolicy().hasHeightForWidth())
        self.choose_label.setSizePolicy(sizePolicy)
        self.choose_label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.choose_label.setFont(font)
        self.choose_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.choose_label)

        self.alg_open_pushButton = QPushButton(self.centralwidget)
        self.alg_open_pushButton.setObjectName(u"alg_open_pushButton")
        self.alg_open_pushButton.setFont(font)

        self.verticalLayout.addWidget(self.alg_open_pushButton)

        DlgAlgLayout.setCentralWidget(self.centralwidget)

        self.retranslateUi(DlgAlgLayout)

        QMetaObject.connectSlotsByName(DlgAlgLayout)


    def retranslateUi(self, DlgAlgLayout):
        DlgAlgLayout.setWindowTitle(QCoreApplication.translate("DlgAlgLayout", u"Open (*.py) file", None))
        self.choose_label.setText(QCoreApplication.translate("DlgAlgLayout", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0441 python3 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u043e\u043c", None))
        self.alg_open_pushButton.setText(QCoreApplication.translate("DlgAlgLayout", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
