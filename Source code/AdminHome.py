
from PyQt5 import QtCore, QtGui, QtWidgets
from ViewNominee import Ui_ViewNominee
from ViewVoters import Ui_ViewVoters
from AddNominee import Ui_AddNominee
from AddVoter import Ui_AddVoter
from Results import Ui_Results
class Ui_AdminHome(object):

    def addnomine(self):
        try:
            self.adnm = QtWidgets.QDialog()
            self.ui1 = Ui_AddNominee()
            self.ui1.setupUi(self.adnm)
            self.adnm.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewnomine(self):
        try:
            self.viewnm = QtWidgets.QDialog()
            self.ui1 = Ui_ViewNominee()
            self.ui1.setupUi(self.viewnm)
            self.ui1.details()
            self.viewnm.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def addvoter(self):
        try:
            self.av = QtWidgets.QDialog()
            self.ui1 = Ui_AddVoter()
            self.ui1.setupUi(self.av)
            self.av.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewvoters(self):
        try:
            self.viewvtrs = QtWidgets.QDialog()
            self.ui1 = Ui_ViewVoters()
            self.ui1.setupUi(self.viewvtrs)
            self.ui1.voters()
            self.viewvtrs.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def results(self):
        try:
            self.view = QtWidgets.QDialog()
            self.ui1 = Ui_Results()
            self.ui1.setupUi(self.view)
            self.ui1.disp()
            self.view.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(746, 424)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 761, 491))
        self.label.setStyleSheet("background-image: url(./images/eye4.jpg);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 80, 251, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.viewnomine);
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 80, 251, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.addnomine);
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 170, 251, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 39, 58);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.addvoter);
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 170, 251, 41))
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 39, 58);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.viewvoters);
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 260, 421, 41))
        self.pushButton_6.setStyleSheet("background-color: rgb(53, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.results);

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Home"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_2.setText(_translate("Dialog", "View Nominees"))
        self.pushButton_3.setText(_translate("Dialog", "Add Nominee"))
        self.pushButton_4.setText(_translate("Dialog", "Add Voter"))
        self.pushButton_5.setText(_translate("Dialog", "View Voters"))
        self.pushButton_6.setText(_translate("Dialog", "Results"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
