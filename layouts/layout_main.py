from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)


class Ui_MainRecognizerWindow(object):
    def setupUi(self, MainRecognizerLayout):
        if not MainRecognizerLayout.objectName():
            MainRecognizerLayout.setObjectName(u"MainWindow")
        MainRecognizerLayout.resize(368, 331)
        MainRecognizerLayout.setMinimumSize(QSize(368, 0))
        MainRecognizerLayout.setMaximumSize(QSize(368, 16777215))
        self.centralwidget = QWidget(MainRecognizerLayout)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.text_manual = QTextBrowser(self.centralwidget)
        self.text_manual.setObjectName(u"text_manual")
        sizePolicy.setHeightForWidth(self.text_manual.sizePolicy().hasHeightForWidth())
        self.text_manual.setSizePolicy(sizePolicy)
        self.text_manual.setMinimumSize(QSize(350, 175))
        self.text_manual.setMaximumSize(QSize(350, 175))
        self.text_manual.setStyleSheet(u"background-color: rgba(230, 230, 230, 200);\n"
"border-radius: 4;")
        self.text_manual.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.text_manual.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout.addWidget(self.text_manual)

        self.layout_file_choose = QHBoxLayout()
        self.layout_file_choose.setObjectName(u"layout_file_choose")
        self.button_file_choose = QPushButton(self.centralwidget)
        self.button_file_choose.setObjectName(u"button_file_choose")
        self.button_file_choose.setMinimumSize(QSize(0, 0))
        self.button_file_choose.setMaximumSize(QSize(250, 16777215))

        self.layout_file_choose.addWidget(self.button_file_choose)


        self.verticalLayout.addLayout(self.layout_file_choose)

        self.label_file_choose = QLabel(self.centralwidget)
        self.label_file_choose.setObjectName(u"label_file_choose")
        self.label_file_choose.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"border-radius: 2;")

        self.verticalLayout.addWidget(self.label_file_choose)

        self.layout_path_choose = QHBoxLayout()
        self.layout_path_choose.setObjectName(u"layout_path_choose")
        self.button_path_choose = QPushButton(self.centralwidget)
        self.button_path_choose.setObjectName(u"button_path_choose")
        self.button_path_choose.setMaximumSize(QSize(250, 16777215))

        self.layout_path_choose.addWidget(self.button_path_choose)


        self.verticalLayout.addLayout(self.layout_path_choose)

        self.label_path_choose = QLabel(self.centralwidget)
        self.label_path_choose.setObjectName(u"label_path_choose")
        self.label_path_choose.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"border-radius: 2;")

        self.verticalLayout.addWidget(self.label_path_choose)

        self.button_analyze = QPushButton(self.centralwidget)
        self.button_analyze.setObjectName(u"button_analyze")

        self.verticalLayout.addWidget(self.button_analyze)

        MainRecognizerLayout.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainRecognizerLayout)

        QMetaObject.connectSlotsByName(MainRecognizerLayout)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_manual.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u043c \u0432\u0430\u0441 \u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u0434\u043b\u044f \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f \u043f\u043e\u043b\u0430 \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430, \u043f\u043e \u0430\u0443\u0434\u0438\u043e\u0437"
                        "\u0430\u043f\u0438\u0441\u0438 \u0435\u0433\u043e \u0433\u043e\u043b\u043e\u0441\u0430.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"><br />\u0414\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0430\u0443\u0434\u0438\u043e\u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0432\u0430\u043c \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b(-\u044b) \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0430\u0445 (*.mp3), (*.wav).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0440\u0430\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 (*.txt).</span></"
                        "p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0435 \u0430\u043d\u0430\u043b\u0438\u0437 \u0437\u0430\u043f\u0438\u0441\u0438(-\u0435\u0439) \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u043d\u043e\u043f\u043a\u0438 &quot;\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c&quot;.</span></p></body></html>", None))
        self.button_file_choose.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b\u044b \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u0430", None))
        self.label_file_choose.setText(QCoreApplication.translate("MainWindow", u" \u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b: ", None))
        self.button_path_choose.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430", None))
        self.label_path_choose.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f: ", None))
        self.button_analyze.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi
