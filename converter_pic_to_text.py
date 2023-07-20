from PyQt6 import QtCore, QtGui, QtWidgets
import easyocr

class Ui_Main_converter(object):
    def setupUi(self, parent):
        parent.setObjectName("Main_converter")
        parent.resize(885, 865)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        parent.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=parent)
        self.centralwidget.setObjectName("centralwidget")
        # Label to display the name of the application
        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(345, 25, 221, 31))
        self.label_name.setObjectName("label_name")
        # Button to select a file
        self.pushButton_sel_file = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_sel_file.setGeometry(QtCore.QRect(550, 60, 191, 31))
        self.pushButton_sel_file.setObjectName("pushButton_sel_file")
        # LineEdit to display the selected file path
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 441, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        # Button to start the OCR process
        self.pushButton_realise_func = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_realise_func.setGeometry(QtCore.QRect(350, 130, 191, 31))
        self.pushButton_realise_func.setObjectName("pushButton_realise_func")
        # Button to clear the selected file path
        self.pushButton_clean_file_wid = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_clean_file_wid.setGeometry(QtCore.QRect(550, 100, 191, 31))
        self.pushButton_clean_file_wid.setObjectName("pushButton_clean_file_wid")
        # ListView to display the available languages for OCR
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(200, 170, 475, 75))
        self.listView.setObjectName("listView")
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        languages = {
            # Available languages for OCR
            "English": "en", "Russia": "ru", "Ukrainian": "uk", "French": "fr", "Spanish": "es",
            "German": "de", "Italian": "it", "Portuguese": "pt", "Dutch": "nl", "Polish": "pl",
            "Czech": "cs", "Slovak": "sk", "Slovenian": "sl", "Croatian": "hr", "Serbian": "sr",
            "Bosnian": "bs", "Macedonian": "mk", "Albanian": "sq", "Armenian": "hy", "Georgian": "ka",
            "Greek": "el", "Turkish": "tr", 
        }
        global model
        model = QtGui.QStandardItemModel()
        for language in languages:
            item = QtGui.QStandardItem(f"{language} - {languages[language]}")
            item.setCheckable(True)
            model.appendRow(item)
        self.listView.setModel(model)
        # ProgressBar to show the progress of OCR
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 254, 441, 31))
        # QTextEdit to display the extracted text from the image
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 294, 765, 500))
        self.textEdit.setObjectName("textEdit")
        self.progressBar.setValue(0)
        parent.setCentralWidget(self.centralwidget)
        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, parent):
        _translate = QtCore.QCoreApplication.translate
        parent.setWindowTitle(_translate("Main_converter", "Converter image to text "))
        # Set text for buttons and labels
        self.label_name.setText(_translate("Main_converter", "Converter image to text"))
        self.pushButton_sel_file.setText(_translate("Main_converter", "Select file"))
        self.pushButton_realise_func.setText(_translate("Main_converter", "Start"))
        self.pushButton_clean_file_wid.setText(_translate("Main_converter", "Clean"))
        self.progressBar.setFormat(_translate("Main_converter", "%p%"))
        # Connect buttons to their corresponding functions
        self.funcs_select()

    def funcs_select(self):
        # Connect buttons to their corresponding functions
        self.pushButton_sel_file.clicked.connect(self.write_file_path)
        self.pushButton_clean_file_wid.clicked.connect(self.funcs_clear)
        self.pushButton_realise_func.clicked.connect(self.funcs_realise)

    def write_file_path(self):
        # Function to open a file dialog and get the selected file path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName()
        if file_path:
            self.lineEdit.setText(file_path)

    def funcs_clear(self):
        # Function to clear the selected file path and reset the progress bar
        self.progressBar.setValue(0)
        self.lineEdit.clear()

    def funcs_realise(self):
        # Function to perform OCR on the selected file using the chosen languages
        try:
            file_path = self.lineEdit.text()
            if QtCore.QFile.exists(file_path):
                selected_languages = []
                for index in range(model.rowCount()):
                    item = model.item(index)
                    if item.checkState() == QtCore.Qt.CheckState.Checked:
                        selected_languages.append(item.text().split(" - ")[1])
                self.progressBar.setValue(25)
                if not selected_languages:
                    QtWidgets.QMessageBox.warning(
                        self.centralwidget, "No language selected", "Please select at least one language."
                    )
                    return
                reader = easyocr.Reader(selected_languages)
                self.progressBar.setValue(50)
                result = reader.readtext(file_path)
                text = "\n".join([line[1] for line in result])
                self.progressBar.setValue(75)
                self.textEdit.setText(text)
                self.progressBar.setValue(100)
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self.centralwidget, "Error", f"An error occurred: {str(e)}"
        )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_converter = QtWidgets.QMainWindow()
    ui = Ui_Main_converter()
    ui.setupUi(main_converter)
    main_converter.show()
    sys.exit(app.exec())

