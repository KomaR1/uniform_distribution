# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from included import *
from lcgLemer import *
from simple_lcg import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 700)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 601, 670))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 40, 431, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 120, 160, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(350, 120, 160, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(240, 170, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 229, 554, 408))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 531, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_4.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_4.addWidget(self.radioButton_5)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 80, 160, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(200, 80, 160, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 150, 131, 67))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(210, 150, 131, 67))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_8.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 181, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 130, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)

        self.label_3.setPixmap(pixmap.scaledToWidth(576))

    def click1(self):
        elements = int(self.lineEdit.text())
        intervals = int(self.lineEdit_2.text())
        if self.radioButton.isChecked():
            included(elements, intervals)
            self.load_image('мой график.png')
        elif self.radioButton_2.isChecked():
            simple_lcg(elements, intervals)
            self.load_image('мой график.png')
        elif self.radioButton_3.isChecked():
            lemer_lcg(elements, intervals)
            self.load_image('мой график.png')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Сыпачёв А. ИДБ-17-07"))
        self.radioButton.setText(_translate("Dialog", "Встроенная функция генерации случайных чисел на интервале [0;1]"))
        self.radioButton_2.setText(_translate("Dialog", "Метод простых конгруэнций"))
        self.radioButton_3.setText(_translate("Dialog", "Метод линейной конгруэнтной последовательности Лемера Д.Г."))
        self.label.setText(_translate("Dialog", "Количество элементов"))
        self.label_2.setText(_translate("Dialog", "Количество интервалов"))
        self.pushButton.setText(_translate("Dialog", "Генерировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Равномерное распределение"))
        self.radioButton_4.setText(_translate("Dialog", "Трапецеидальный закон распределения"))
        self.radioButton_5.setText(_translate("Dialog", "Треугольный закон распределения"))
        self.label_4.setText(_translate("Dialog", "Количество элементов"))
        self.label_5.setText(_translate("Dialog", "Количество интервалов"))
        self.label_6.setText(_translate("Dialog", "Ширина двух различных отрезков"))
        self.pushButton_2.setText(_translate("Dialog", "Генерировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Симпсона"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
