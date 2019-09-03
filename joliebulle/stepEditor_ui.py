# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../joliebulle/stepEditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 317)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEditStepName = QtWidgets.QLineEdit(Dialog)
        self.lineEditStepName.setObjectName("lineEditStepName")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditStepName)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comboBoxStepType = QtWidgets.QComboBox(Dialog)
        self.comboBoxStepType.setObjectName("comboBoxStepType")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxStepType)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.doubleSpinBoxStepTime = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxStepTime.setObjectName("doubleSpinBoxStepTime")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxStepTime)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.doubleSpinBoxStepTemp = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxStepTemp.setObjectName("doubleSpinBoxStepTemp")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxStepTemp)
        self.gridLayout.addLayout(self.formLayout_6, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Editeur de paliers"))
        self.label_9.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Nom :</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Type :</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Durée :</span></p></body></html>"))
        self.doubleSpinBoxStepTime.setSuffix(_translate("Dialog", " min"))
        self.label_12.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température :</span></p></body></html>"))
        self.doubleSpinBoxStepTemp.setSuffix(_translate("Dialog", " °C"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#909090;\">Le premier palier devrait toujours être de type Infusion.</span></p><p><span style=\" color:#909090;\">Pour les paliers par ajout d\'eau chaude choisir Infusion.</span></p><p><span style=\" color:#909090;\">Pour les paliers par chauffe directe choisir Température.</span></p></body></html>"))

