# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Table.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table(object):
    def setupUi(self, Table):
        Table.setObjectName("Table")
        Table.resize(1132, 834)
        self.gridLayout = QtWidgets.QGridLayout(Table)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.BG = QtWidgets.QFrame(Table)
        self.BG.setStyleSheet("background-color: rgb(56, 58, 89);\n"
"color: rgb(255, 255, 255);")
        self.BG.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BG.setObjectName("BG")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.BG)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleBar = QtWidgets.QFrame(self.BG)
        self.TitleBar.setMinimumSize(QtCore.QSize(0, 80))
        self.TitleBar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.TitleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBar.setObjectName("TitleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TitleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.TitleBar)
        self.frame_5.setMinimumSize(QtCore.QSize(80, 80))
        self.frame_5.setMaximumSize(QtCore.QSize(80, 80))
        self.frame_5.setStyleSheet("image: url(:/logo/Untitled-jhh1.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout.addWidget(self.frame_5)
        self.TeamName = QtWidgets.QLabel(self.TitleBar)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.TeamName.setFont(font)
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout.addWidget(self.TeamName)
        self.btn_minimize = QtWidgets.QPushButton(self.TitleBar)
        self.btn_minimize.setMinimumSize(QtCore.QSize(15, 15))
        self.btn_minimize.setMaximumSize(QtCore.QSize(15, 15))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 255, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 154, 0);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout.addWidget(self.btn_minimize)
        self.btn_restore = QtWidgets.QPushButton(self.TitleBar)
        self.btn_restore.setMinimumSize(QtCore.QSize(15, 15))
        self.btn_restore.setMaximumSize(QtCore.QSize(15, 15))
        self.btn_restore.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(208, 208, 0);\n"
"}")
        self.btn_restore.setText("")
        self.btn_restore.setObjectName("btn_restore")
        self.horizontalLayout.addWidget(self.btn_restore)
        self.btn_close = QtWidgets.QPushButton(self.TitleBar)
        self.btn_close.setMinimumSize(QtCore.QSize(15, 15))
        self.btn_close.setMaximumSize(QtCore.QSize(15, 15))
        self.btn_close.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(185, 0, 0);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout.addWidget(self.TitleBar)
        self.frame_4 = QtWidgets.QFrame(self.BG)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget.setStyleSheet("border-color: rgb(56, 58, 89);\n"
"border-right-color: rgb(56, 58, 89);\n"
"border-bottom-color: rgb(56, 58, 89);\n"
"gridline-color: rgb(56, 58, 89);\n"
"color: rgb(160, 10, 11);\n"
"font: 81 10pt \"JetBrains Mono\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CTable = QtWidgets.QTableWidget(self.tab)
        self.CTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CTable.setRowCount(0)
        self.CTable.setColumnCount(17)
        self.CTable.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTable.setHorizontalHeaderItem(16, item)
        self.gridLayout_4.addWidget(self.CTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.S1Table = QtWidgets.QTableWidget(self.tab_2)
        self.S1Table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.S1Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.S1Table.setRowCount(0)
        self.S1Table.setColumnCount(7)
        self.S1Table.setObjectName("tableWidget_4")
        item = QtWidgets.QTableWidgetItem()
        self.S1Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.S1Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.S1Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.S1Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.S1Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.S1Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.S1Table.setHorizontalHeaderItem(6, item)
        self.gridLayout_6.addWidget(self.S1Table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.S2Table = QtWidgets.QTableWidget(self.tab_3)
        self.S2Table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.S2Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.S2Table.setRowCount(0)
        self.S2Table.setColumnCount(7)
        self.S2Table.setObjectName("tableWidget_5")
        item = QtWidgets.QTableWidgetItem()
        self.S2Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.S2Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.S2Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.S2Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.S2Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.S2Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.S2Table.setHorizontalHeaderItem(6, item)
        self.gridLayout_5.addWidget(self.S2Table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.BG)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.copyright = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.copyright.setFont(font)
        self.copyright.setObjectName("copyright")
        self.gridLayout_2.addWidget(self.copyright, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.BG, 0, 0, 1, 1)

        self.retranslateUi(Table)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Table)

    def retranslateUi(self, Table):
        _translate = QtCore.QCoreApplication.translate
        Table.setWindowTitle(_translate("Table", "TABLE"))
        self.TeamName.setText(_translate("Table", "SPOROS#3751::TABLE"))
        item = self.CTable.horizontalHeaderItem(0)
        item.setText(_translate("Table", "TEAMID"))
        item = self.CTable.horizontalHeaderItem(1)
        item.setText(_translate("Table", "MISSION_TIME"))
        item = self.CTable.horizontalHeaderItem(2)
        item.setText(_translate("Table", "PACKET_COUNT"))
        item = self.CTable.horizontalHeaderItem(3)
        item.setText(_translate("Table", "PACKET_TYPE"))
        item = self.CTable.horizontalHeaderItem(4)
        item.setText(_translate("Table", "MODE"))
        item = self.CTable.horizontalHeaderItem(5)
        item.setText(_translate("Table", "SP1_R"))
        item = self.CTable.horizontalHeaderItem(6)
        item.setText(_translate("Table", "SP2_R"))
        item = self.CTable.horizontalHeaderItem(7)
        item.setText(_translate("Table", "ALTITUDE"))
        item = self.CTable.horizontalHeaderItem(8)
        item.setText(_translate("Table", "TEMP"))
        item = self.CTable.horizontalHeaderItem(9)
        item.setText(_translate("Table", "BATTERY"))
        item = self.CTable.horizontalHeaderItem(10)
        item.setText(_translate("Table", "GPS_LATITUDE"))
        item = self.CTable.horizontalHeaderItem(11)
        item.setText(_translate("Table", "GPS_LONGITUDE"))
        item = self.CTable.horizontalHeaderItem(12)
        item.setText(_translate("Table", "GPS_ALTITUDE"))
        item = self.CTable.horizontalHeaderItem(13)
        item.setText(_translate("Table", "GPS_SATS"))
        item = self.CTable.horizontalHeaderItem(14)
        item.setText(_translate("Table", "SW_STATE"))
        item = self.CTable.horizontalHeaderItem(15)
        item.setText(_translate("Table", "SP1_PACKET"))
        item = self.CTable.horizontalHeaderItem(16)
        item.setText(_translate("Table", "CMD_ECHO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Table", "CONTAINER"))
        item = self.S1Table.horizontalHeaderItem(0)
        item.setText(_translate("Table", "TEAMID"))
        item = self.S1Table.horizontalHeaderItem(1)
        item.setText(_translate("Table", "MISSION_TIME"))
        item = self.S1Table.horizontalHeaderItem(2)
        item.setText(_translate("Table", "PACKET_COUNT"))
        item = self.S1Table.horizontalHeaderItem(3)
        item.setText(_translate("Table", "PACKET_TYPE"))
        item = self.S1Table.horizontalHeaderItem(4)
        item.setText(_translate("Table", "ALTITUDE"))
        item = self.S1Table.horizontalHeaderItem(5)
        item.setText(_translate("Table", "TEMP"))
        item = self.S1Table.horizontalHeaderItem(6)
        item.setText(_translate("Table", "ROTATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Table", "PAYLOAD1"))
        item = self.S2Table.horizontalHeaderItem(0)
        item.setText(_translate("Table", "TEAMID"))
        item = self.S2Table.horizontalHeaderItem(1)
        item.setText(_translate("Table", "MISSION_TIME"))
        item = self.S2Table.horizontalHeaderItem(2)
        item.setText(_translate("Table", "PACKET_COUNT"))
        item = self.S2Table.horizontalHeaderItem(3)
        item.setText(_translate("Table", "PACKET_TYPE"))
        item = self.S2Table.horizontalHeaderItem(4)
        item.setText(_translate("Table", "ALTITUDE"))
        item = self.S2Table.horizontalHeaderItem(5)
        item.setText(_translate("Table", "TEMP"))
        item = self.S2Table.horizontalHeaderItem(6)
        item.setText(_translate("Table", "ROTATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Table", "PAYLOAD2"))
        self.copyright.setText(_translate("Table", "USA CANSAT 2021 GCS ver.2.0.1 Space AC : Team SPOROS by Pop"))
import resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Table = QtWidgets.QWidget()
    ui = Ui_Table()
    ui.setupUi(Table)
    Table.show()
    sys.exit(app.exec_())