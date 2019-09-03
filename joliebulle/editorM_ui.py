# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../joliebulle/editorM.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 301)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonNouveau = QtWidgets.QPushButton(self.widget)
        self.pushButtonNouveau.setObjectName("pushButtonNouveau")
        self.horizontalLayout.addWidget(self.pushButtonNouveau)
        self.pushButtonEnlever = QtWidgets.QPushButton(self.widget)
        self.pushButtonEnlever.setObjectName("pushButtonEnlever")
        self.horizontalLayout.addWidget(self.pushButtonEnlever)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.listViewDivers = QtWidgets.QListView(self.widget)
        self.listViewDivers.setObjectName("listViewDivers")
        self.gridLayout.addWidget(self.listViewDivers, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 2, 2)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.formLayout = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditNom = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditNom.setObjectName("lineEditNom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNom)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBoxType = QtWidgets.QComboBox(self.widget_2)
        self.comboBoxType.setObjectName("comboBoxType")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxType)
        self.pushButtonAjouter = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonAjouter.setObjectName("pushButtonAjouter")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButtonAjouter)
        self.gridLayout_2.addWidget(self.widget_2, 0, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Editeur"))
        self.pushButtonNouveau.setText(_translate("Dialog", "Nouveau"))
        self.pushButtonEnlever.setText(_translate("Dialog", "Enlever"))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Nom</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Type</span></p></body></html>"))
        self.pushButtonAjouter.setText(_translate("Dialog", "Ajouter"))

