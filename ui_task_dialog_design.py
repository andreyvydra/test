# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designs/task_dialog_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("designs\\../img/Без названия.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: #333333;\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.taskColorButton = QtWidgets.QPushButton(Dialog)
        self.taskColorButton.setStyleSheet("background-color: #777777;color: #ffffff;\n"
"")
        self.taskColorButton.setObjectName("taskColorButton")
        self.gridLayout.addWidget(self.taskColorButton, 3, 2, 1, 3)
        self.widgetColorText = QtWidgets.QWidget(Dialog)
        self.widgetColorText.setStyleSheet("background-color: #ffffff;")
        self.widgetColorText.setObjectName("widgetColorText")
        self.gridLayout.addWidget(self.widgetColorText, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("color: #ffffff;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("color: #ffffff;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("color: #ffffff;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("background-color: #777777;color: #ffffff;\n"
"")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("color: #ffffff;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.err_msg = QtWidgets.QLabel(Dialog)
        self.err_msg.setStyleSheet("color: #ffffff;")
        self.err_msg.setText("")
        self.err_msg.setObjectName("err_msg")
        self.gridLayout.addWidget(self.err_msg, 6, 0, 1, 5)
        self.textColorButton = QtWidgets.QPushButton(Dialog)
        self.textColorButton.setStyleSheet("background-color: #777777;\n"
"color: #ffffff;\n"
"")
        self.textColorButton.setObjectName("textColorButton")
        self.gridLayout.addWidget(self.textColorButton, 2, 2, 1, 3)
        self.header = QtWidgets.QLineEdit(Dialog)
        self.header.setStyleSheet("background-color: #555555;\n"
"color: #ffffff;\n"
"border: none;")
        self.header.setObjectName("header")
        self.gridLayout.addWidget(self.header, 0, 1, 1, 4)
        self.description = QtWidgets.QPlainTextEdit(Dialog)
        self.description.setStyleSheet("background-color: #555555;\n"
"color: #ffffff;")
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 1, 1, 1, 4)
        self.widgetColorTask = QtWidgets.QWidget(Dialog)
        self.widgetColorTask.setStyleSheet("background-color: #666666;")
        self.widgetColorTask.setObjectName("widgetColorTask")
        self.gridLayout.addWidget(self.widgetColorTask, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setStyleSheet("color: #ffffff;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.todoButton = QtWidgets.QRadioButton(Dialog)
        self.todoButton.setStyleSheet("color: #ffffff;")
        self.todoButton.setObjectName("todoButton")
        self.horizontalLayout_2.addWidget(self.todoButton)
        self.progressButton = QtWidgets.QRadioButton(Dialog)
        self.progressButton.setStyleSheet("color: #ffffff;")
        self.progressButton.setObjectName("progressButton")
        self.horizontalLayout_2.addWidget(self.progressButton)
        self.doneButton = QtWidgets.QRadioButton(Dialog)
        self.doneButton.setStyleSheet("color: #ffffff;")
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout_2.addWidget(self.doneButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 4)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Задача"))
        self.taskColorButton.setText(_translate("Dialog", "Выбрать цвет"))
        self.label_5.setText(_translate("Dialog", "Цвет задачи"))
        self.label_3.setText(_translate("Dialog", "Цвет текста"))
        self.label.setText(_translate("Dialog", "Заголовок"))
        self.label_2.setText(_translate("Dialog", "Описание"))
        self.textColorButton.setText(_translate("Dialog", "Выбрать цвет"))
        self.header.setText(_translate("Dialog", "Новая задача"))
        self.label_6.setText(_translate("Dialog", "Группа"))
        self.todoButton.setText(_translate("Dialog", "To do"))
        self.progressButton.setText(_translate("Dialog", "Progress"))
        self.doneButton.setText(_translate("Dialog", "Done"))
