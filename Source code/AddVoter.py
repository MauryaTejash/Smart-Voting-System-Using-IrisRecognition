from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import imagehash
from PIL import Image
from DBConnection import DBConnection
import sys, os

class Ui_AadharDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("AadharDialog")
        Dialog.resize(400, 200)
        self.label_aadhar = QtWidgets.QLabel(Dialog)
        self.label_aadhar.setGeometry(QtCore.QRect(270, 40, 271, 91))
        self.label_aadhar.setObjectName("label_aadhar")
        self.lineEdit_aadhar = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_aadhar.setGeometry(QtCore.QRect(110, 310, 191, 41))
        self.lineEdit_aadhar.setObjectName("lineEdit_aadhar")
        self.pushButton_submit_aadhar = QtWidgets.QPushButton(Dialog)
        self.pushButton_submit_aadhar.setGeometry(QtCore.QRect(240, 310, 271, 41))
        self.pushButton_submit_aadhar.setStyleSheet("font: 14pt \"Georgia\";\n"
                                                     "background-color: rgb(85, 85, 255);\n"
                                                     "color: rgb(255, 255, 255);")
        self.pushButton_submit_aadhar.setObjectName("pushButton_submit_aadhar")
        self.pushButton_submit_aadhar.setText("Submit")
        self.pushButton_submit_aadhar.clicked.connect(self.add_aadhar)

    def add_aadhar(self):
        aadhar_number = self.lineEdit_aadhar.text()
        # Add code to process Aadhar number
        print("Aadhar Number:", aadhar_number)


class Ui_AddVoter(object):
    def open_aadhar_dialog(self):
        self.aadhar_dialog = QtWidgets.QDialog()
        self.aadhar_ui = Ui_AadharDialog()
        self.aadhar_ui.setupUi(self.aadhar_dialog)
        self.aadhar_dialog.exec_()

    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.lineEdit.setText(fileName)

    def addvoter(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            fileName = self.lineEdit.text()
            vid = self.lineEdit_2.text()
            vnm = self.lineEdit_3.text()
            aadhar = self.lineEdit_4.text()

            if vid == "" or vid == "null" or vnm == "" or vnm == "null" or fileName == "" or fileName == "null" or aadhar == "" or aadhar == "null" :
                self.showMessageBox("Information", "Please fill out all fields")
            elif len(aadhar) != 12:
                self.showMessageBox("Information", "Please enter a valid 12-digit Aadhar Number")
            else:
                # Validate Aadhar and VNM from the database
                sql = "SELECT * FROM aadhar WHERE aadhar=%s AND vnm=%s"
                cursor.execute(sql, (aadhar, vnm))
                result = cursor.fetchone()
                if result:
                    # Aadhar and VNM found in the database
                    img = Image.open(fileName)
                    hash = imagehash.average_hash(img)
                    print(hash)
                    sql = "SELECT COUNT(*) FROM voter WHERE hash=%s"
                    cursor.execute(sql, (str(hash),))
                    res = cursor.fetchone()[0]
                    if res > 0:
                        self.showMessageBox("Information", "IRIS Image already exists..!")
                    else:
                        iris = self.read_file(fileName)
                        path, filename = os.path.split(fileName)  # get filename only from fullpath
                        query = "INSERT INTO voter VALUES (%s, %s, %s, %s, %s, %s)"
                        values = (vid, vnm, filename, str(hash), iris, aadhar)
                        cursor.execute(query, values)
                        database.commit()
                        self.showMessageBox("Message", "Voter added Successfully")
                        self.lineEdit_2.setText(str(randint(1000, 9999)))
                        self.lineEdit.setText("")
                        self.lineEdit_3.setText("")
                        self.lineEdit_4.setText("")
                else:
                    self.showMessageBox("Information", "Invalid Aadhar Number or Voter Name")

        except Exception as e:
            print("Error=" , e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def read_file(self, filename):
        with open(filename, 'rb') as f:
            img = f.read()
        return img

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(712, 531)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 40, 271, 91))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 335, 191, 100))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(240, 370, 271, 41))
        self.lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 370, 121, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 440, 131, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"Georgia\";\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.addvoter)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 150, 191, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 150, 271, 45))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(str(randint(1000, 9999)))

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 230, 191, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 230, 271, 41))
        self.lineEdit_3.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 300, 191, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 14pt \"Georgia\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 300, 271, 41))
        self.lineEdit_4.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Adding Voter"))
        self.label.setText(_translate("Dialog", "Adding Voter"))
        self.label_2.setText(_translate("Dialog", "IRIS Image"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Submit"))
        self.label_3.setText(_translate("Dialog", "Voter ID"))
        self.label_4.setText(_translate("Dialog", "Voter Name"))
        self.label_5.setText(_translate("Dialog", "Aadhar"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AddVoter()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
