# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../joliebulle/densimetre.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogDensimetre(object):
    def setupUi(self, DialogDensimetre):
        DialogDensimetre.setObjectName("DialogDensimetre")
        DialogDensimetre.resize(250, 178)
        self.gridLayout = QtWidgets.QGridLayout(DialogDensimetre)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DialogDensimetre)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(DialogDensimetre)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(DialogDensimetre)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBoxTempCalib = QtWidgets.QDoubleSpinBox(DialogDensimetre)
        self.doubleSpinBoxTempCalib.setProperty("value", 20.0)
        self.doubleSpinBoxTempCalib.setObjectName("doubleSpinBoxTempCalib")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxTempCalib)
        self.doubleSpinBoxTempEchan = QtWidgets.QDoubleSpinBox(DialogDensimetre)
        self.doubleSpinBoxTempEchan.setEnabled(True)
        self.doubleSpinBoxTempEchan.setProperty("value", 20.0)
        self.doubleSpinBoxTempEchan.setObjectName("doubleSpinBoxTempEchan")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxTempEchan)
        self.doubleSpinBoxDens = QtWidgets.QDoubleSpinBox(DialogDensimetre)
        self.doubleSpinBoxDens.setSuffix("")
        self.doubleSpinBoxDens.setDecimals(3)
        self.doubleSpinBoxDens.setMinimum(1.0)
        self.doubleSpinBoxDens.setMaximum(1.9)
        self.doubleSpinBoxDens.setSingleStep(0.001)
        self.doubleSpinBoxDens.setObjectName("doubleSpinBoxDens")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxDens)
        self.label_4 = QtWidgets.QLabel(DialogDensimetre)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelDensCorr = QtWidgets.QLabel(DialogDensimetre)
        self.labelDensCorr.setObjectName("labelDensCorr")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.labelDensCorr)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogDensimetre)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogDensimetre)
        self.buttonBox.accepted.connect(DialogDensimetre.accept)
        self.buttonBox.rejected.connect(DialogDensimetre.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDensimetre)

    def retranslateUi(self, DialogDensimetre):
        _translate = QtCore.QCoreApplication.translate
        DialogDensimetre.setWindowTitle(_translate("DialogDensimetre", "Densimetre"))
        self.label.setText(_translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité mesurée</span></p></body></html>"))
        self.label_2.setText(_translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température calibration</span></p></body></html>"))
        self.label_3.setText(_translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température échantillon</span></p></body></html>"))
        self.doubleSpinBoxTempCalib.setSuffix(_translate("DialogDensimetre", "°C"))
        self.doubleSpinBoxTempEchan.setSuffix(_translate("DialogDensimetre", "°C"))
        self.label_4.setText(_translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité corrigée :</span></p></body></html>"))
        self.labelDensCorr.setText(_translate("DialogDensimetre", "1.000"))

