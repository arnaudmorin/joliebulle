# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../joliebulle/editorG.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(683, 312)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonNouveau = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonNouveau.setObjectName("pushButtonNouveau")
        self.horizontalLayout.addWidget(self.pushButtonNouveau)
        self.pushButtonEnlever = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonEnlever.setObjectName("pushButtonEnlever")
        self.horizontalLayout.addWidget(self.pushButtonEnlever)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.listViewGrains = QtWidgets.QListView(self.widget_2)
        self.listViewGrains.setObjectName("listViewGrains")
        self.gridLayout_2.addWidget(self.listViewGrains, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 2, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditNom = QtWidgets.QLineEdit(self.widget)
        self.lineEditNom.setObjectName("lineEditNom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNom)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBoxType = QtWidgets.QComboBox(self.widget)
        self.comboBoxType.setObjectName("comboBoxType")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxType)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBoxRendmt = QtWidgets.QSpinBox(self.widget)
        self.spinBoxRendmt.setObjectName("spinBoxRendmt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxRendmt)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBoxCouleur = QtWidgets.QDoubleSpinBox(self.widget)
        self.spinBoxCouleur.setDecimals(1)
        self.spinBoxCouleur.setMaximum(10000.0)
        self.spinBoxCouleur.setObjectName("spinBoxCouleur")
        self.horizontalLayout_2.addWidget(self.spinBoxCouleur)
        self.radioButtonSRM = QtWidgets.QRadioButton(self.widget)
        self.radioButtonSRM.setObjectName("radioButtonSRM")
        self.horizontalLayout_2.addWidget(self.radioButtonSRM)
        self.radioButtonEBC = QtWidgets.QRadioButton(self.widget)
        self.radioButtonEBC.setObjectName("radioButtonEBC")
        self.horizontalLayout_2.addWidget(self.radioButtonEBC)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBoxReco = QtWidgets.QComboBox(self.widget)
        self.comboBoxReco.setObjectName("comboBoxReco")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxReco)
        self.pushButtonAjouter = QtWidgets.QPushButton(self.widget)
        self.pushButtonAjouter.setObjectName("pushButtonAjouter")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButtonAjouter)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

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
        self.label_3.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Rendement</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Couleur</span></p></body></html>"))
        self.radioButtonSRM.setText(_translate("Dialog", "SRM"))
        self.radioButtonEBC.setText(_translate("Dialog", "EBC"))
        self.label_6.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Empâtage recommandé</span></p></body></html>"))
        self.pushButtonAjouter.setText(_translate("Dialog", "Ajouter"))

