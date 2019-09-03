# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../joliebulle/preboil.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreEbullitionDialog(object):
    def setupUi(self, PreEbullitionDialog):
        PreEbullitionDialog.setObjectName("PreEbullitionDialog")
        PreEbullitionDialog.resize(412, 215)
        self.gridLayout = QtWidgets.QGridLayout(PreEbullitionDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(PreEbullitionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(25, -1, 25, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(PreEbullitionDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.doubleSpinBoxVolume = QtWidgets.QDoubleSpinBox(PreEbullitionDialog)
        self.doubleSpinBoxVolume.setMaximumSize(QtCore.QSize(100, 16777215))
        self.doubleSpinBoxVolume.setDecimals(1)
        self.doubleSpinBoxVolume.setMinimum(0.1)
        self.doubleSpinBoxVolume.setMaximum(1000.0)
        self.doubleSpinBoxVolume.setObjectName("doubleSpinBoxVolume")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxVolume)
        self.label_2 = QtWidgets.QLabel(PreEbullitionDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.labelGravity = QtWidgets.QLabel(PreEbullitionDialog)
        self.labelGravity.setObjectName("labelGravity")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelGravity)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)

        self.retranslateUi(PreEbullitionDialog)
        self.buttonBox.accepted.connect(PreEbullitionDialog.accept)
        self.buttonBox.rejected.connect(PreEbullitionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreEbullitionDialog)

    def retranslateUi(self, PreEbullitionDialog):
        _translate = QtCore.QCoreApplication.translate
        PreEbullitionDialog.setWindowTitle(_translate("PreEbullitionDialog", "Pré-Ebullition"))
        self.label.setText(_translate("PreEbullitionDialog", "Volume mesuré :"))
        self.label_2.setText(_translate("PreEbullitionDialog", "La densité devrait être :"))
        self.labelGravity.setText(_translate("PreEbullitionDialog", "1.000"))

