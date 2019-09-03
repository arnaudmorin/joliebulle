# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../joliebulle/mashEditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogMash(object):
    def setupUi(self, DialogMash):
        DialogMash.setObjectName("DialogMash")
        DialogMash.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(DialogMash)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DialogMash)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditName = QtWidgets.QLineEdit(DialogMash)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.label_2 = QtWidgets.QLabel(DialogMash)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBoxPh = QtWidgets.QDoubleSpinBox(DialogMash)
        self.doubleSpinBoxPh.setObjectName("doubleSpinBoxPh")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxPh)
        self.label_5 = QtWidgets.QLabel(DialogMash)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.doubleSpinBoxSpargeT = QtWidgets.QDoubleSpinBox(DialogMash)
        self.doubleSpinBoxSpargeT.setObjectName("doubleSpinBoxSpargeT")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxSpargeT)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogMash)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogMash)
        self.buttonBox.accepted.connect(DialogMash.accept)
        self.buttonBox.rejected.connect(DialogMash.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMash)

    def retranslateUi(self, DialogMash):
        _translate = QtCore.QCoreApplication.translate
        DialogMash.setWindowTitle(_translate("DialogMash", "Editeur de profils de brassage"))
        self.label.setText(_translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">Nom :</span></p></body></html>"))
        self.label_2.setText(_translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">pH :</span></p></body></html>"))
        self.label_5.setText(_translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">Température rinçage :</span></p></body></html>"))

