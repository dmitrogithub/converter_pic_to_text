# Form implementation generated from reading ui file 'converter_pic_to_text.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
import easyocr

class Ui_Main_converter(object):
    def setupUi(self, parent):
        parent.setObjectName("Main_converter")
        parent.resize(878, 571)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        parent.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=parent)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(330, 30, 221, 31))
        self.label_name.setObjectName("label_name")
        self.pushButton_sel_file = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_sel_file.setGeometry(QtCore.QRect(550, 60, 191, 31))
        self.pushButton_sel_file.setObjectName("pushButton_sel_file")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 441, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 210, 771, 321))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_realise_func = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_realise_func.setGeometry(QtCore.QRect(350, 130, 191, 31))
        self.pushButton_realise_func.setObjectName("pushButton_realise_func")
        self.pushButton_clean_file_wid = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_clean_file_wid.setGeometry(QtCore.QRect(550, 100, 191, 31))
        self.pushButton_clean_file_wid.setObjectName("pushButton_clean_file_wid")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 170, 441, 31))
        self.progressBar.setValue(0)

        parent.setCentralWidget(self.centralwidget)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, parent):
        _translate = QtCore.QCoreApplication.translate
        parent.setWindowTitle(_translate("Main_converter", "Converter image to text "))
        self.label_name.setText(_translate("Main_converter", "Converter image to text"))
        self.pushButton_sel_file.setText(_translate("Main_converter", "Select file"))
        self.pushButton_realise_func.setText(_translate("Main_converter", "Start"))
        self.pushButton_clean_file_wid.setText(_translate("Main_converter", "Clean"))
        self.progressBar.setFormat(_translate("Main_converter", "%p%"))
        self.funcs_select()

    def funcs_select(self):
        self.pushButton_sel_file.clicked.connect(self.write_file_path)
        self.pushButton_clean_file_wid.clicked.connect(self.funcs_clear)
        self.pushButton_realise_func.clicked.connect(self.funcs_realise)

    def write_file_path(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName()
        if file_path:
            self.lineEdit.setText(file_path)

    def funcs_clear(self):
        self.progressBar.setValue(0)
        self.lineEdit.clear()

    def funcs_realise(self):
        file_path = self.lineEdit.text()
        if QtCore.QFile.exists(file_path):
            self.progressBar.setValue(50)
            reader = easyocr.Reader(['en'])
            result = reader.readtext(file_path)
            text = "\n".join([line[1] for line in result])
            self.progressBar.setValue(75)
            self.textEdit.setText(text)
            self.progressBar.setValue(100)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_converter = QtWidgets.QMainWindow()
    ui = Ui_Main_converter()
    ui.setupUi(main_converter)
    main_converter.show()
    sys.exit(app.exec())