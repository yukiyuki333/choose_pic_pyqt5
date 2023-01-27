# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_file_path = QtWidgets.QTextEdit(self.centralwidget)
        self.show_file_path.setGeometry(QtCore.QRect(210, 600, 751, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        self.show_file_path.setFont(font)
        self.show_file_path.setObjectName("show_file_path")
        self.file_path_label = QtWidgets.QLabel(self.centralwidget)
        self.file_path_label.setGeometry(QtCore.QRect(100, 600, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.file_path_label.setFont(font)
        self.file_path_label.setObjectName("file_path_label")
        self.choose_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_label.setGeometry(QtCore.QRect(100, 680, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.choose_label.setFont(font)
        self.choose_label.setObjectName("choose_label")
        self.choose_button = QtWidgets.QPushButton(self.centralwidget)
        self.choose_button.setGeometry(QtCore.QRect(240, 680, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.choose_button.setFont(font)
        self.choose_button.setObjectName("choose_button")
        self.start_label = QtWidgets.QLabel(self.centralwidget)
        self.start_label.setGeometry(QtCore.QRect(460, 760, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_label.setFont(font)
        self.start_label.setObjectName("start_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(600, 760, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(240, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.image_label.setFont(font)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.style_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.style_label_2.setGeometry(QtCore.QRect(770, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.style_label_2.setFont(font)
        self.style_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.style_label_2.setObjectName("style_label_2")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setEnabled(True)
        self.image.setGeometry(QtCore.QRect(29, 90, 521, 471))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.image.setFont(font)
        self.image.setText("")
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.image_2 = QtWidgets.QLabel(self.centralwidget)
        self.image_2.setEnabled(True)
        self.image_2.setGeometry(QtCore.QRect(560, 90, 521, 471))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.image_2.setFont(font)
        self.image_2.setText("")
        self.image_2.setAlignment(QtCore.Qt.AlignCenter)
        self.image_2.setObjectName("image_2")
        self.style_label = QtWidgets.QLabel(self.centralwidget)
        self.style_label.setGeometry(QtCore.QRect(460, 680, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.style_label.setFont(font)
        self.style_label.setObjectName("style_label")
        self.style_button = QtWidgets.QPushButton(self.centralwidget)
        self.style_button.setGeometry(QtCore.QRect(600, 680, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.style_button.setFont(font)
        self.style_button.setObjectName("style_button")
        self.epoch_lineeditor = QtWidgets.QLineEdit(self.centralwidget)
        self.epoch_lineeditor.setGeometry(QtCore.QRect(230, 760, 113, 41))
        self.epoch_lineeditor.setObjectName("epoch_lineeditor")
        self.epoch_label = QtWidgets.QLabel(self.centralwidget)
        self.epoch_label.setGeometry(QtCore.QRect(100, 760, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.epoch_label.setFont(font)
        self.epoch_label.setObjectName("epoch_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_path_label.setText(_translate("MainWindow", "圖片路徑："))
        self.choose_label.setText(_translate("MainWindow", "請選擇圖片："))
        self.choose_button.setText(_translate("MainWindow", "Open file"))
        self.start_label.setText(_translate("MainWindow", "開始轉換："))
        self.start_button.setText(_translate("MainWindow", "start"))
        self.image_label.setText(_translate("MainWindow", "目前圖片"))
        self.style_label_2.setText(_translate("MainWindow", "<html><head/><body><p>轉換風格</p></body></html>"))
        self.style_label.setText(_translate("MainWindow", "請選擇風格："))
        self.style_button.setText(_translate("MainWindow", "Open file"))
        self.epoch_label.setText(_translate("MainWindow", "輸入epoch"))
