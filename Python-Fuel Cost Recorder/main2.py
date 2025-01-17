# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys
import MessageBox
import sqlite3
import gas_rc


class Ui_MainProgram(object):
    def setupUi(self, MainProgram):
        MainProgram.setObjectName("MainProgram")
        MainProgram.resize(800, 460)
        MainProgram.setMinimumSize(QtCore.QSize(800, 460))
        MainProgram.setMaximumSize(QtCore.QSize(800, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/FuelIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainProgram.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainProgram)
        self.centralwidget.setObjectName("centralwidget")
        self.GasStation = QtWidgets.QLabel(self.centralwidget)
        self.GasStation.setGeometry(QtCore.QRect(320, 140, 511, 421))
        self.GasStation.setStyleSheet("image: url(:/newPrefix/GasStation.png);")
        self.GasStation.setText("")
        self.GasStation.setObjectName("GasStation")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 400, 851, 41))
        self.graphicsView.setStyleSheet("background-color: rgb(113, 95, 116);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 361, 31))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 90, 101, 21))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 131, 21))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.InputExpense = QtWidgets.QLineEdit(self.centralwidget)
        self.InputExpense.setGeometry(QtCore.QRect(220, 180, 101, 20))
        self.InputExpense.setMinimumSize(QtCore.QSize(101, 20))
        self.InputExpense.setMaximumSize(QtCore.QSize(101, 20))
        self.InputExpense.setToolTip("")
        self.InputExpense.setObjectName("InputExpense")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 150, 121, 21))
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.InputTHBLitre = QtWidgets.QLineEdit(self.centralwidget)
        self.InputTHBLitre.setGeometry(QtCore.QRect(220, 150, 101, 20))
        self.InputTHBLitre.setMinimumSize(QtCore.QSize(101, 20))
        self.InputTHBLitre.setMaximumSize(QtCore.QSize(101, 20))
        self.InputTHBLitre.setToolTip("")
        self.InputTHBLitre.setObjectName("InputTHBLitre")
        self.StartKm = QtWidgets.QLineEdit(self.centralwidget)
        self.StartKm.setGeometry(QtCore.QRect(220, 210, 101, 20))
        self.StartKm.setMinimumSize(QtCore.QSize(101, 20))
        self.StartKm.setMaximumSize(QtCore.QSize(101, 20))
        self.StartKm.setToolTip("")
        self.StartKm.setObjectName("StartKm")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 210, 131, 21))
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 240, 161, 21))
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.RefillKm = QtWidgets.QLineEdit(self.centralwidget)
        self.RefillKm.setGeometry(QtCore.QRect(220, 240, 101, 20))
        self.RefillKm.setMinimumSize(QtCore.QSize(101, 20))
        self.RefillKm.setMaximumSize(QtCore.QSize(101, 20))
        self.RefillKm.setToolTip("")
        self.RefillKm.setObjectName("RefillKm")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(610, 210, 121, 51))
        self.ClearButton.setMinimumSize(QtCore.QSize(121, 51))
        self.ClearButton.setMaximumSize(QtCore.QSize(121, 51))
        self.ClearButton.setToolTip("")
        self.ClearButton.setObjectName("ClearButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 50, 121, 31))
        self.label_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(490, 100, 121, 31))
        self.label_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(490, 160, 121, 31))
        self.label_12.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 380, 801, 20))
        self.graphicsView_2.setStyleSheet("background-color: rgb(173, 213, 144);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(220, 60, 101, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 60, 101, 21))
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.DisplayKmL = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.DisplayKmL.setGeometry(QtCore.QRect(360, 90, 121, 51))
        self.DisplayKmL.setToolTip("")
        self.DisplayKmL.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);")
        self.DisplayKmL.setObjectName("DisplayKmL")
        self.Display100KmL = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Display100KmL.setGeometry(QtCore.QRect(360, 150, 121, 51))
        self.Display100KmL.setToolTip("")
        self.Display100KmL.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);")
        self.Display100KmL.setObjectName("Display100KmL")
        self.receivedText = QtWidgets.QLabel(self.centralwidget)
        self.receivedText.setGeometry(QtCore.QRect(600, 30, 181, 21))
        self.receivedText.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.receivedText.setObjectName("receivedText")
        self.BTNcalc = QtWidgets.QPushButton(self.centralwidget)
        self.BTNcalc.setGeometry(QtCore.QRect(330, 240, 21, 21))
        self.BTNcalc.setStyleSheet("")
        self.BTNcalc.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/CalcIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTNcalc.setIcon(icon1)
        self.BTNcalc.setObjectName("BTNcalc")
        self.distanceText = QtWidgets.QLabel(self.centralwidget)
        self.distanceText.setGeometry(QtCore.QRect(600, 60, 151, 21))
        self.distanceText.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.distanceText.setObjectName("distanceText")
        self.THBKm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.THBKm.setGeometry(QtCore.QRect(360, 210, 121, 51))
        self.THBKm.setToolTip("")
        self.THBKm.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);")
        self.THBKm.setObjectName("THBKm")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(490, 220, 121, 31))
        self.label_16.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.fuelType = QtWidgets.QComboBox(self.centralwidget)
        self.fuelType.setGeometry(QtCore.QRect(220, 90, 101, 22))
        self.fuelType.setObjectName("fuelType")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.fuelType.addItem("")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(610, 150, 121, 51))
        self.SaveButton.setMinimumSize(QtCore.QSize(121, 51))
        self.SaveButton.setMaximumSize(QtCore.QSize(121, 51))
        self.SaveButton.setToolTip("")
        self.SaveButton.setObjectName("SaveButton")
        self.DataButton = QtWidgets.QPushButton(self.centralwidget)
        self.DataButton.setGeometry(QtCore.QRect(610, 90, 121, 51))
        self.DataButton.setMinimumSize(QtCore.QSize(121, 51))
        self.DataButton.setMaximumSize(QtCore.QSize(121, 51))
        self.DataButton.setToolTip("")
        self.DataButton.setObjectName("DataButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-70, -30, 211, 121))
        self.label.setStyleSheet("image: url(:/newPrefix/icon/Nozzle.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 410, 361, 16))
        self.status.setStyleSheet("color: rgb(255, 255, 255);")
        self.status.setObjectName("status")
        self.fuelStation = QtWidgets.QComboBox(self.centralwidget)
        self.fuelStation.setGeometry(QtCore.QRect(220, 120, 101, 22))
        self.fuelStation.setObjectName("fuelStation")
        self.fuelStation.addItem("")
        self.fuelStation.addItem("")
        self.fuelStation.addItem("")
        self.fuelStation.addItem("")
        self.fuelStation.addItem("")
        self.fuelStation.addItem("")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(60, 120, 121, 21))
        self.label_13.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.GasStation.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.InputExpense.raise_()
        self.label_6.raise_()
        self.InputTHBLitre.raise_()
        self.StartKm.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.RefillKm.raise_()
        self.ClearButton.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.dateEdit.raise_()
        self.label_7.raise_()
        self.DisplayKmL.raise_()
        self.Display100KmL.raise_()
        self.receivedText.raise_()
        self.BTNcalc.raise_()
        self.distanceText.raise_()
        self.THBKm.raise_()
        self.label_16.raise_()
        self.fuelType.raise_()
        self.SaveButton.raise_()
        self.DataButton.raise_()
        self.label.raise_()
        self.status.raise_()
        self.fuelStation.raise_()
        self.label_13.raise_()
        MainProgram.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainProgram)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainProgram.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainProgram)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/AboutIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClear = QtWidgets.QAction(MainProgram)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/ClearIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon3)
        self.actionClear.setObjectName("actionClear")
        self.actionSave = QtWidgets.QAction(MainProgram)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/SaveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName("actionSave")
        self.actionTo_xlsx = QtWidgets.QAction(MainProgram)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/xlsxIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTo_xlsx.setIcon(icon5)
        self.actionTo_xlsx.setObjectName("actionTo_xlsx")
        self.actionSave_to_csv = QtWidgets.QAction(MainProgram)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/csvIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_to_csv.setIcon(icon6)
        self.actionSave_to_csv.setObjectName("actionSave_to_csv")
        self.actionExit = QtWidgets.QAction(MainProgram)
        self.actionExit.setObjectName("actionExit")
        self.actionNew = QtWidgets.QAction(MainProgram)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/NewIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon7)
        self.actionNew.setObjectName("actionNew")
        self.actionDataManager = QtWidgets.QAction(MainProgram)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/databaseIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDataManager.setIcon(icon8)
        self.actionDataManager.setObjectName("actionDataManager")
        self.actionOpen = QtWidgets.QAction(MainProgram)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon9)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRelease_Notes = QtWidgets.QAction(MainProgram)
        self.actionRelease_Notes.setIcon(icon7)
        self.actionRelease_Notes.setObjectName("actionRelease_Notes")
        self.actionCalculate = QtWidgets.QAction(MainProgram)
        self.actionCalculate.setIcon(icon1)
        self.actionCalculate.setObjectName("actionCalculate")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionRelease_Notes)
        self.menuEdit.addAction(self.actionClear)
        self.menuEdit.addAction(self.actionCalculate)
        self.menuEdit.addAction(self.actionDataManager)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainProgram)
        self.ClearButton.clicked.connect(self.RefillKm.clear)
        self.ClearButton.clicked.connect(self.StartKm.clear)
        self.ClearButton.clicked.connect(self.InputExpense.clear)
        self.ClearButton.clicked.connect(self.InputTHBLitre.clear)
        self.ClearButton.clicked.connect(self.Display100KmL.clear)
        self.ClearButton.clicked.connect(self.DisplayKmL.clear)
        self.ClearButton.clicked.connect(self.THBKm.clear)
        QtCore.QMetaObject.connectSlotsByName(MainProgram)

        #Clicked Clear Menubar
        self.actionClear.triggered.connect(self.RefillKm.clear)
        self.actionClear.triggered.connect(self.StartKm.clear)
        self.actionClear.triggered.connect(self.InputExpense.clear)
        self.actionClear.triggered.connect(self.InputTHBLitre.clear)
        self.actionClear.triggered.connect(self.Display100KmL.clear)
        self.actionClear.triggered.connect(self.DisplayKmL.clear)
        self.actionClear.triggered.connect(self.THBKm.clear)
        self.actionRelease_Notes.triggered.connect(self.releaseNote)
        #Clicked Save, About, Exit, New Menubar, DataManager, Open
        self.actionDataManager.triggered.connect(self.openDataManager) #DataManager
        self.actionAbout.triggered.connect(self.showAbout) #About
        self.actionExit.triggered.connect(self.showExit) #Exit
        self.actionSave.triggered.connect(self.appendTable) #Save
        self.actionCalculate.triggered.connect(self.calcKmL) #Calculate
        #Code วันที่
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        #คำสั่งปุ่ม Calculation
        self.BTNcalc.clicked.connect(self.calcKmL) #กำหนดปุ่มคำนวณน้ำมัน KmL
        #คำสั่งปุ่ม Data Manager, Save
        #Code From Youtube 'PyQt : Open Other Window When Button Clicked. Ssj6 Channel'
        self.DataButton.clicked.connect(self.openDataManager) #Clicked DataButton (open new Window)
        self.SaveButton.clicked.connect(self.appendTable) #Save DB

    def releaseNote(self):  #Open Release Notes
        from releasenote import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDataManager(self):  #Open DataManager
        from datamgr2 import Ui_DataWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DataWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        #Code วันที่
    def onDateChanged(self, qDate):
        print('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))

    def showAbout(self): #Help --> About Menubar
        MessageBox.showAbout()

    def showExit(self): #File --> Exit
        MessageBox.showExit()
        #END

    def retranslateUi(self, MainProgram):
        _translate = QtCore.QCoreApplication.translate
        MainProgram.setWindowTitle(_translate("MainProgram", "Fuel Management V1.01"))
        self.label_3.setText(_translate("MainProgram", "Fuel Management v1.01"))
        self.label_4.setText(_translate("MainProgram", "2. Fuel Type"))
        self.label_5.setText(_translate("MainProgram", "5. Expenses (THB)"))
        self.label_6.setText(_translate("MainProgram", "4. THB/Litre"))
        self.label_9.setText(_translate("MainProgram", "6. Start Trip (Km)"))
        self.label_10.setText(_translate("MainProgram", "7. End Trip (Km)"))
        self.ClearButton.setText(_translate("MainProgram", "Clear"))
        self.label_8.setText(_translate("MainProgram", "Consumption"))
        self.label_11.setText(_translate("MainProgram", "km/L"))
        self.label_12.setText(_translate("MainProgram", "L/100km"))
        self.label_7.setText(_translate("MainProgram", "1. Date"))
        self.receivedText.setToolTip(_translate("MainProgram", "<html><head/><body><p><span style=\" font-size:8pt;\">ปริมาณน้ำมันที่ได้รับ (ลิตร)</span></p></body></html>"))
        self.receivedText.setText(_translate("MainProgram", "    Received 0.00 Litre"))
        self.BTNcalc.setToolTip(_translate("MainProgram", "<html><head/><body><p>Calculate</p></body></html>"))
        self.distanceText.setToolTip(_translate("MainProgram", "<html><head/><body><p><span style=\" font-size:8pt;\">ระยะทางที่วิ่ง (กิโลเมตร)</span></p></body></html>"))
        self.distanceText.setText(_translate("MainProgram", "    Distance 0 Km"))
        self.label_16.setText(_translate("MainProgram", "THB/Km"))
        self.fuelType.setItemText(0, _translate("MainProgram", "Premium Diesel"))
        self.fuelType.setItemText(1, _translate("MainProgram", "Diesel B20"))
        self.fuelType.setItemText(2, _translate("MainProgram", "Diesel ฺB10"))
        self.fuelType.setItemText(3, _translate("MainProgram", "Diesel B7"))
        self.fuelType.setItemText(4, _translate("MainProgram", "Benzin 95"))
        self.fuelType.setItemText(5, _translate("MainProgram", "Gasohol 95"))
        self.fuelType.setItemText(6, _translate("MainProgram", "Gasohol 91"))
        self.fuelType.setItemText(7, _translate("MainProgram", "E20"))
        self.fuelType.setItemText(8, _translate("MainProgram", "E85"))
        self.SaveButton.setText(_translate("MainProgram", "Save"))
        self.DataButton.setText(_translate("MainProgram", "Data Manager"))
        self.status.setText(_translate("MainProgram", "Reading File :"))
        self.fuelStation.setItemText(0, _translate("MainProgram", "Caltex"))
        self.fuelStation.setItemText(1, _translate("MainProgram", "ESSO"))
        self.fuelStation.setItemText(2, _translate("MainProgram", "Shell"))
        self.fuelStation.setItemText(3, _translate("MainProgram", "PTT"))
        self.fuelStation.setItemText(4, _translate("MainProgram", "BCP"))
        self.fuelStation.setItemText(5, _translate("MainProgram", "PT"))
        self.label_13.setText(_translate("MainProgram", "3. Station"))
        self.menuFile.setTitle(_translate("MainProgram", "File"))
        self.menuHelp.setTitle(_translate("MainProgram", "Help"))
        self.menuEdit.setTitle(_translate("MainProgram", "Edit"))
        self.actionAbout.setText(_translate("MainProgram", "About"))
        self.actionClear.setText(_translate("MainProgram", "Clear"))
        self.actionSave.setText(_translate("MainProgram", "Save"))
        self.actionTo_xlsx.setText(_translate("MainProgram", "Export to .xlsx"))
        self.actionSave_to_csv.setText(_translate("MainProgram", "Export to .csv"))
        self.actionExit.setText(_translate("MainProgram", "Exit"))
        self.actionNew.setText(_translate("MainProgram", "New"))
        self.actionDataManager.setText(_translate("MainProgram", "Data Manager"))
        self.actionOpen.setText(_translate("MainProgram", "Open"))
        self.actionRelease_Notes.setText(_translate("MainProgram", "Release Notes"))
        self.actionCalculate.setText(_translate("MainProgram", "Calculate"))

    def appendTable(self):
        try:
            dated = self.dateEdit.text()
            FuelType = self.fuelType.currentText()
            FuelStation = self.fuelStation.currentText()
            THBLitre = self.InputTHBLitre.text()
            Expenses = self.InputExpense.text()
            StartKM =  self.StartKm.text()
            RefillKM = self.RefillKm.text()

            #Add FuelReceived และ Distance ลง db แบบทศนิยม 3 ตำแหน่ง
            start = self.StartKm.text()
            refill = self.RefillKm.text()
            THBLitre = self.InputTHBLitre.text()
            Expenses = self.InputExpense.text()
            FuelReceived_calc = int(Expenses)/float(THBLitre)
            FuelReceived = ("{:.3f}".format(FuelReceived_calc))
            Distance = int(refill)-int(start)

            #Add ส่วน Consumption
            KML = self.DisplayKmL.toPlainText()
            L100KM = self.Display100KmL.toPlainText()
            THBKM = self.THBKm.toPlainText()

            connection = sqlite3.connect("db/myDB.db")
            connection.cursor()
            data_insert = """INSERT INTO FuelManagement (Dated, FuelType, FuelStation, THBLitre, Expenses, StartKM, RefillKM, FuelReceived, Distance, KML, L100KM, THBKM)
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            data = (dated, FuelType, FuelStation, THBLitre, Expenses, StartKM, RefillKM, FuelReceived, Distance, KML, L100KM, THBKM)
            connection.execute(data_insert, data)
            connection.commit()
            connection.close()

            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("Data Added Sucessfully")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

            self.status.setText("Reading File : db/myDB.db")
                
        except Exception as e:
            print (e)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("ไม่สามารถเซฟได้ กรุณาตรวจสอบข้อมูล")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
            #END

    def calcKmL(self):
        start = self.StartKm.text()             #ช่องรับข้อมูล StartKm
        refill = self.RefillKm.text()           #ช่องรับข้อมูล Refill Km
        THBLitre = self.InputTHBLitre.text()    #ช่องรับข้อมูล THB/Litre
        Expenses = self.InputExpense.text()     #ช่องรับข้อมูล Expenses

        try:
            distance_result = int(refill)-int(start)            #คำนวณระยะทาง
            Received_result = int(Expenses)/float(THBLitre)     #คำนวณปริมาณน้ำมันที่เติม
            KmL = int(distance_result)/float(Received_result)   #คำนวณอัตราสิ้นเปลือง Km/L
            HundredKmL = 100/float(KmL)                         #คำนวณอัตราสิ้นเปลือง 100Km/L
            THBKm_result = float(THBLitre)/float(KmL)           #คำนวณอัตราสิ้นเปลือง THB/Km
            self.receivedText.setText("Received {:.3f}".format(Received_result) + " Litre")     #แสดงปริมาณน้ำมันที่เติม
            self.distanceText.setText("Distance " + str(distance_result) + " Km")               #แสดงผลคำนวณระยะทาง
        
        #กำหนดช่องแสดงผล Km/L
            self.DisplayKmL.setPlainText("")
            self.DisplayKmL.appendPlainText("{:.3f}".format(KmL))
        
        #กำหนดช่องแสดงผล 100Km/L
            self.Display100KmL.setPlainText("")
            self.Display100KmL.appendPlainText("{:.3f}".format(HundredKmL))

        #กำหนดช่องแสดงผล THB/Km
            self.THBKm.setPlainText("")
            self.THBKm.appendPlainText("{:.3f}".format(THBKm_result))

            #ส่วนเงื่อนไข ERROR พร้อมแสดง MessageBox
            if int(Expenses) < float(THBLitre):
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("เงินที่จ่าย (Expenses) น้อยกว่าราคาน้ำมัน (THB/Litre) กรุณาตรวจสอบอีกครั้ง")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

            if int(start) >= int(refill):
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("ระยะทางก่อนเติมมากกว่าหลังเติม กรุณาตรวจสอบอีกครั้ง")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

            if int(KmL) > 30 or int(KmL) < 5:
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("อัตราสิ้นเปลืองผิดปรกติ กรุณาตรวจสอบอีกครั้ง")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
                self.DisplayKmL.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n""color: rgb(255, 0, 0);")
                self.Display100KmL.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n""color: rgb(255, 0, 0);")
                self.THBKm.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n""color: rgb(255, 0, 0);")
            else:
                self.DisplayKmL.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n""color: rgb(0, 170, 0);")
                self.Display100KmL.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n""color: rgb(0, 170, 0);")
                self.THBKm.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n""color: rgb(0, 170, 0);")

        except Exception as e:
            print (e)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("กรุณาใส่ตัวเลขหรือกรอกข้อมูลให้ครบถ้วน")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
            #END

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainProgram = QtWidgets.QMainWindow()
    ui = Ui_MainProgram()
    ui.setupUi(MainProgram)
    MainProgram.show()
    sys.exit(app.exec_())
