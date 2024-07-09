from PyQt5 import QtCore, QtGui, QtWidgets
from hamming import *
from Voting import Ui_Voting
from DBConnection import DBConnection
import sys

class Ui_Voter(object):
    def __init__(self,Dialog):
        self.dialog=Dialog

    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.lineEdit.setText(fileName)


    def logincheck(self):
        try:
            iris = self.lineEdit.text()
            vid = self.lineEdit_2.text()
            if vid == "" or vid == "null" or iris == "" or iris == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                    database = DBConnection.getConnection()
                    cursor = database.cursor()
                    query = "select iris from voter where vid=%s"
                    values = (str(vid),)
                    cursor.execute(query, values)
                    imgdata = cursor.fetchone()[0]
                    self.write_file(imgdata,"testiris.bmp")
                    verify = same_person_eyes("testiris.bmp",iris)
                    if verify is True:
                        print('Authorized')
                        self.showMessageBox("Information", "Authorized")
                        try:
                            self.voter = QtWidgets.QDialog()
                            self.ui = Ui_Voting(self.voter,vid)
                            self.ui.setupUi(self.voter)
                            self.ui.nominelist()
                            self.voter.show()
                            self.dialog.hide()
                        except Exception as e:
                            print(e.args[0])
                            tb = sys.exc_info()[2]
                            print(tb.tb_lineno)
                        '''self.vtr = QtWidgets.QDialog()
                        self.ui = Ui_Voting(self.vtr,vid)
                        self.ui.setupUi(self.vtr)
                        self.ui.nominelist()
                        self.vtr.show()'''


                    else:
                        print('Not Authorized')
                        self.showMessageBox("Information", "Not Authorized")


        except Exception as e:
            print("Error=", e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def write_file(self,data, filename):
        with open(filename, 'wb') as f:
            f.write(data)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(712, 456)
        Dialog.setStyleSheet("background-color: rgb(204, 136, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 40, 271, 91))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 240, 191, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(240, 240, 271, 41))
        self.lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 240, 121, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 320, 131, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"Georgia\";\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.logincheck)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 150, 191, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 150, 271, 41))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Voter Login"))
        self.label.setText(_translate("Dialog", " Voter Login"))
        self.label_2.setText(_translate("Dialog", "IRIS Image"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "Voter ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Voter(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())