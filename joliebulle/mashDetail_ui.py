# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../joliebulle/mashDetail.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogMashDetail(object):
    def setupUi(self, DialogMashDetail):
        DialogMashDetail.setObjectName("DialogMashDetail")
        DialogMashDetail.resize(361, 281)
        self.gridLayout = QtWidgets.QGridLayout(DialogMashDetail)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelMashName = QtWidgets.QLabel(DialogMashDetail)
        self.labelMashName.setObjectName("labelMashName")
        self.verticalLayout.addWidget(self.labelMashName)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.labelPhValue = QtWidgets.QLabel(DialogMashDetail)
        self.labelPhValue.setObjectName("labelPhValue")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelPhValue)
        self.labelSparge = QtWidgets.QLabel(DialogMashDetail)
        self.labelSparge.setObjectName("labelSparge")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelSparge)
        self.labelSpargeValue = QtWidgets.QLabel(DialogMashDetail)
        self.labelSpargeValue.setObjectName("labelSpargeValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelSpargeValue)
        self.labelPh = QtWidgets.QLabel(DialogMashDetail)
        self.labelPh.setObjectName("labelPh")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelPh)
        self.verticalLayout.addLayout(self.formLayout)
        self.label = QtWidgets.QLabel(DialogMashDetail)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formSteps = QtWidgets.QFormLayout()
        self.formSteps.setObjectName("formSteps")
        self.verticalLayout.addLayout(self.formSteps)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogMashDetail)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogMashDetail)
        self.buttonBox.accepted.connect(DialogMashDetail.accept)
        self.buttonBox.rejected.connect(DialogMashDetail.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMashDetail)

    def retranslateUi(self, DialogMashDetail):
        _translate = QtCore.QCoreApplication.translate
        DialogMashDetail.setWindowTitle(_translate("DialogMashDetail", "Dialog"))
        self.labelMashName.setText(_translate("DialogMashDetail", "<html><head/><body><p align=\"center\">Profil</p></body></html>"))
        self.labelPhValue.setText(_translate("DialogMashDetail", "0"))
        self.labelSparge.setText(_translate("DialogMashDetail", "<html><head/><body><p><span style=\" font-weight:600;\">Rinçage :</span></p></body></html>"))
        self.labelSpargeValue.setText(_translate("DialogMashDetail", "0"))
        self.labelPh.setText(_translate("DialogMashDetail", "<html><head/><body><p><span style=\" font-weight:600;\">Ph : </span></p></body></html>"))
        self.label.setText(_translate("DialogMashDetail", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Etapes</span></p></body></html>"))

