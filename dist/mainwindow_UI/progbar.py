# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 208)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.greenprogressBar = QtWidgets.QProgressBar(Form)
        self.greenprogressBar.setStyleSheet("#greenprogressBar{\n"
            "    min-height: 12px;\n"
            "    max-height: 12px;\n"
            "    border-radius: 6px;\n"
            "}\n"
            "#greenprogressBar::chunk{\n"
            "    border-radius: 6px;\n"
            "    background-color: #00ff00;\n"
            "}")
        self.greenprogressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.greenprogressBar.setMaximum(0)
        self.greenprogressBar.setProperty("value", -1)
        self.greenprogressBar.setObjectName("greenprogressBar")
        self.verticalLayout.addWidget(self.greenprogressBar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
        # self.label.setText

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
