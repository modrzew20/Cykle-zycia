# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import DaoClient, DaoRoom
from Apartment import Apartment

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setStyleSheet("QDialogButtonBox > QPushButton{\n"
                                 "\n"
                                 "background-color: rgb(27, 3, 159);\n"
                                 "color:rgb(198, 140, 255);\n"
                                 "font-size:20px;\n"
                                 "font-family:Verdana,bold;\n"
                                 "}\n"
                                 """ QDialogButtonBox > QPushButton:hover{
                                 color:white;
                                 }
                                 """


                                 "\n"
                                 "#widget{\n"
                                 "background:url(./logo.svg)\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QDialogButtonBox > QPushButton:hover{\n"
                                 "background-color:rgb(19, 42, 255)\n"
                                 "}\n"
                                 "\n"
                                 "#groupBox {\n"
                                 "color:white;\n"
                                 "font-size:20px;\n"
                                 "}\n"
                                 "QRadioButton{\n"
                                 "color:white;\n"
                                 "font-size:25px;\n"
                                 "font:Verdana,bold;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#title , #title_2{\n"
                                 "    font-family: Georgia;\n"
                                 "font-size: 40px;"
                                 "}\n"
                                 "\n"
                                 "QLabel\n"
                                 "{\n"
                                 "    color : white;\n"
                                 "    font-size: 20px;		\n"
                                 "   font-family: Georgia, serif; \n"
                                 "}\n"
                                 "\n"
                                 "#page_exist,#page_newrent,#page_newroom,#page_main\n"
                                 "{\n"
                                 "    background: url(./tlo2.jpg);\n"
                                 "}\n"
                                 "\n"
                                 "#newrent,#newroom{\n"
                                 "    border-radius: 25px;\n"
                                 "    background: #1B1B1B\n"
                                 "}\n"
                                 "#top_frame {\n"
                                 "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,x3: 0, y3:2,    stop: 0 rgb(39, 20, 255),stop: 0.4 rgba(69,9,121,1) ,stop: 0.8 rgba(2,0,36,1));\n"
                                 "}\n"
                                 "\n"
                                 "#btn_frame {\n"
                                 "background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,x3: 2, y3:0,    stop: 0 rgb(39, 20, 255),"
                                 "stop: 0.4 rgba(69,9,121,1) ,stop: 0.8 rgba(11,11,11));\n "
                                 "}\n"
                                 "\n"
                                 "QTabWidget:pane {\n"
                                 "border: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "#tabWidget_2 > QTabBar::tab {\n"
                                 " padding: 10px;\n"
                                 "}\n"
                                 "#tabWidget_2 >QTabBar::tab:selected { \n"
                                 "  background: rgb(198, 140, 255); \n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTabBar::tab {\n"
                                 "  background: rgb(230, 230, 230); \n"
                                 "  border: 1px solid lightgray; \n"
                                 "  padding: 15px;\n"
                                 "  font-family:Verdana,bold;\n"
                                 "  font-size: 15px;\n"
                                 "} \n"
                                 "\n"
                                 "QTabBar::tab:selected { \n"
                                 "  background: rgb(170, 170, 255);\n"
                                 "  margin-bottom: -1px; \n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#tab,#tab_2,#tab_4{\n"
                                 "    background: rgb(170, 170, 255);\n"
                                 "    border:0px solid;\n"
                                 "}\n"
                                 "\n"
                                 "#tab_3,#tab_6,#tab_5 {\n"
                                 "    background: #1B1B1B;\n"
                                 "}\n"
                                 "\n"
                                 "#frame {\n"
                                 "    background:white;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{ \n"
                                 "background-color:rgb(198, 140, 255);\n"
                                 "border: 2px solid gray;\n"
                                 "border-radius: 10px;\n"
                                 "padding: 0 8px;\n"
                                 "selection-background-color: darkgray;\n"
                                 "font-size: 16px;\n"
                                 "}\n"
                                 "QSpinBox{\n"
                                 "background-color:rgb(198, 140, 255);\n"
                                 "border-radius: 10px;\n"
                                 "font-size: 16px;\n"
                                 "padding: 0 10px;\n"
                                 "}\n"
                                 """QSpinBox::down-button {
                                        width:30px;
                                        }
                                        
                                        QSpinBox::up-button {
                                        width:30px;
                                        }"""
                                 "QCheckBox {\n"
                                 "color:white;\n"
                                 "font-size: 20px;\n"
                                 "font:bold;\n"
                                 "}\n"
                                 "\n"
                                 "#btn_main_page,#btn_addreserv_page,#btn_actualreserv_page,#btn_addroom_page{\n"
                                 "  background-color: RoyalBlue;\n"
                                 "  border: none;\n"
                                 "  border-radius: 10px;\n"
                                 "  cursor: pointer;\n"
                                 "}\n"
                                 "\n"
                                 "#btn_main_page:hover,#btn_addreserv_page:hover,#btn_actualreserv_page:hover,#btn_addroom_page:hover{\n"                                 "  background-color: DodgerBlue;\n"
                                 "}")
        MainWindow.setWindowIcon(QtGui.QIcon("./logogorne.svg"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(0, 0, 1201, 701))
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.btn_frame = QtWidgets.QFrame(self.main)
        self.btn_frame.setGeometry(QtCore.QRect(0, 50, 71, 651))
        self.btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_frame.setObjectName("btn_frame")
        self.btn_main_page = QtWidgets.QPushButton(self.btn_frame)
        self.btn_main_page.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.btn_main_page.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_main_page.setIcon(icon)
        self.btn_main_page.setIconSize(QtCore.QSize(30, 30))
        self.btn_main_page.setObjectName("btn_main_page")
        self.btn_addreserv_page = QtWidgets.QPushButton(self.btn_frame)
        self.btn_addreserv_page.setGeometry(QtCore.QRect(10, 70, 51, 51))
        self.btn_addreserv_page.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addreserv_page.setIcon(icon1)
        self.btn_addreserv_page.setIconSize(QtCore.QSize(35, 35))
        self.btn_addreserv_page.setObjectName("btn_addreserv_page")
        self.btn_actualreserv_page = QtWidgets.QPushButton(self.btn_frame)
        self.btn_actualreserv_page.setGeometry(QtCore.QRect(10, 130, 51, 51))
        self.btn_actualreserv_page.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./reserv.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_actualreserv_page.setIcon(icon2)
        self.btn_actualreserv_page.setIconSize(QtCore.QSize(35, 35))
        self.btn_actualreserv_page.setObjectName("btn_actualreserv_page")
        self.btn_addroom_page = QtWidgets.QPushButton(self.btn_frame)
        self.btn_addroom_page.setGeometry(QtCore.QRect(10, 190, 51, 51))
        self.btn_addroom_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./addroom.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addroom_page.setIcon(icon3)
        self.btn_addroom_page.setIconSize(QtCore.QSize(35, 35))
        self.btn_addroom_page.setObjectName("btn_addroom_page")
        self.top_frame = QtWidgets.QFrame(self.main)
        self.top_frame.setGeometry(QtCore.QRect(0, 0, 1201, 51))
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.pages = QtWidgets.QFrame(self.main)
        self.pages.setGeometry(QtCore.QRect(49, 49, 1151, 651))
        self.pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pages.setObjectName("pages")
        self.stackedWidget = QtWidgets.QStackedWidget(self.pages)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 0, 1131, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.widget = QtWidgets.QWidget(self.page_main)
        self.widget.setGeometry(QtCore.QRect(150, 180, 860, 281))
        self.widget.setObjectName("widget")
        self.stackedWidget.addWidget(self.page_main)
        self.page_newrent = QtWidgets.QWidget()
        self.page_newrent.setObjectName("page_newrent")

        ############################     NEW RESERVATION    #################
        self.newrent = QtWidgets.QFrame(self.page_newrent)
        self.newrent.setGeometry(QtCore.QRect(360, 50, 651, 551))
        self.newrent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.newrent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newrent.setObjectName("newrent")
        self.title = QtWidgets.QLabel(self.newrent)
        self.title.setGeometry(QtCore.QRect(100, 20, 450, 41))
        self.title.setObjectName("title")
        self.name_2 = QtWidgets.QLabel(self.newrent)
        self.name_2.setGeometry(QtCore.QRect(190, 110, 51, 20))
        self.name_2.setObjectName("name_2")
        self.surname = QtWidgets.QLabel(self.newrent)
        self.surname.setGeometry(QtCore.QRect(130, 160, 111, 20))
        self.surname.setObjectName("surname")
        self.pesel = QtWidgets.QLabel(self.newrent)
        self.pesel.setGeometry(QtCore.QRect(170, 210, 71, 21))
        self.pesel.setObjectName("pesel")
        self.city = QtWidgets.QLabel(self.newrent)
        self.city.setGeometry(QtCore.QRect(155, 260, 80, 20))
        self.city.setObjectName("city")
        self.street = QtWidgets.QLabel(self.newrent)
        self.street.setGeometry(QtCore.QRect(170, 310, 61, 16))
        self.street.setObjectName("street")
        self.nFlat = QtWidgets.QLabel(self.newrent)
        self.nFlat.setGeometry(QtCore.QRect(22, 360, 220, 20))
        self.nFlat.setObjectName("nFlat")
        self.room = QtWidgets.QLabel(self.newrent)
        self.room.setGeometry(QtCore.QRect(65, 410, 161, 16))
        self.room.setObjectName("room")
        self.lName = QtWidgets.QLineEdit(self.newrent)
        self.lName.setGeometry(QtCore.QRect(270, 100, 291, 41))
        self.lName.setObjectName("lName")
        self.lSurname = QtWidgets.QLineEdit(self.newrent)
        self.lSurname.setGeometry(QtCore.QRect(270, 150, 291, 41))
        self.lSurname.setObjectName("lSurname")
        self.lPesel = QtWidgets.QLineEdit(self.newrent)
        self.lPesel.setGeometry(QtCore.QRect(270, 200, 291, 41))
        self.lPesel.setObjectName("lPesel")
        self.lCity = QtWidgets.QLineEdit(self.newrent)
        self.lCity.setGeometry(QtCore.QRect(270, 250, 291, 41))
        self.lCity.setObjectName("lCity")
        self.lStreet = QtWidgets.QLineEdit(self.newrent)
        self.lStreet.setGeometry(QtCore.QRect(270, 300, 291, 41))
        self.lStreet.setObjectName("lStreet")
        self.lNFlat = QtWidgets.QLineEdit(self.newrent)
        self.lNFlat.setGeometry(QtCore.QRect(270, 350, 161, 41))
        self.lNFlat.setObjectName("lNFlat")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.newrent)
        self.buttonBox.setGeometry(QtCore.QRect(230, 510, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(self.newrent)
        self.groupBox.setGeometry(QtCore.QRect(60, 440, 531, 61))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(110, 30, 140, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(265, 30, 140, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(400, 30, 140, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lRoom = QtWidgets.QSpinBox(self.newrent)
        self.lRoom.setGeometry(QtCore.QRect(270, 400, 81, 41))
        self.lRoom.setObjectName("lRoom")
        self.stackedWidget.addWidget(self.page_newrent)
        self.page_newroom = QtWidgets.QWidget()
        self.page_newroom.setObjectName("page_newroom")

        ##################################     NEW ROOM     #######################################################

        self.newroom = QtWidgets.QFrame(self.page_newroom)
        self.newroom.setGeometry(QtCore.QRect(360, 50, 651, 551))
        self.newroom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.newroom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newroom.setObjectName("newroom")
        self.label = QtWidgets.QLabel(self.newroom)
        self.label.setGeometry(QtCore.QRect(464, 150, 61, 21))
        self.label.setObjectName("label")
        self.title_2 = QtWidgets.QLabel(self.newroom)
        self.title_2.setGeometry(QtCore.QRect(50, 20, 550, 41))
        self.title_2.setObjectName("title_2")
        self.label_10 = QtWidgets.QLabel(self.newroom)
        self.label_10.setGeometry(QtCore.QRect(90, 100, 170, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.newroom)
        self.label_11.setGeometry(QtCore.QRect(200, 150, 65, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.newroom)
        self.lineEdit_9.setGeometry(QtCore.QRect(310, 90, 211, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.newroom)
        self.lineEdit_10.setGeometry(QtCore.QRect(310, 140, 141, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")

        ##################################     NEW APARTMENT     #######################################################
        self.tabWidget_2 = QtWidgets.QTabWidget(self.newroom)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 210, 611, 321))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(40, 40, 200, 20))
        self.label_13.setObjectName("label_13")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.tab_3)
        self.buttonBox_2.setGeometry(QtCore.QRect(190, 250, 193, 28))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(40, 110, 190, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(40, 180, 191, 20))
        self.label_15.setObjectName("label_15")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_3.setGeometry(QtCore.QRect(260, 30, 61, 41))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_4.setGeometry(QtCore.QRect(260, 170, 61, 41))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_5.setGeometry(QtCore.QRect(260, 100, 61, 41))
        self.spinBox_5.setObjectName("spinBox_5")
        self.tabWidget_2.addTab(self.tab_3, "")

        ##################################     NEW NORMALROOM     #######################################################
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_16 = QtWidgets.QLabel(self.tab_6)
        self.label_16.setGeometry(QtCore.QRect(20, 90, 220, 20))
        self.label_16.setObjectName("label_16")
        self.buttonBox_3 = QtWidgets.QDialogButtonBox(self.tab_6)
        self.buttonBox_3.setGeometry(QtCore.QRect(190, 250, 193, 28))
        self.buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_3.setObjectName("buttonBox_3")
        self.label_17 = QtWidgets.QLabel(self.tab_6)
        self.label_17.setGeometry(QtCore.QRect(20, 140, 220, 20))
        self.label_17.setObjectName("label_17")
        self.checkBox = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox.setGeometry(QtCore.QRect(260, 140, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox_2.setGeometry(QtCore.QRect(260, 80, 61, 41))
        self.spinBox_2.setObjectName("spinBox_2")
        self.tabWidget_2.addTab(self.tab_6, "")

        ##################################     NEW GUESTHOUSE     #######################################################
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(20, 50, 240, 20))
        self.label_18.setObjectName("label_18")
        self.spinBox = QtWidgets.QSpinBox(self.tab_5)
        self.spinBox.setGeometry(QtCore.QRect(250, 40, 61, 41))
        self.spinBox.setObjectName("spinBox")
        self.buttonBox_4 = QtWidgets.QDialogButtonBox(self.tab_5)
        self.buttonBox_4.setGeometry(QtCore.QRect(190, 250, 193, 28))
        self.buttonBox_4.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_4.setObjectName("buttonBox_4")
        self.label_20 = QtWidgets.QLabel(self.tab_5)
        self.label_20.setGeometry(QtCore.QRect(20, 120, 191, 20))
        self.label_20.setObjectName("label_20")
        self.label_19 = QtWidgets.QLabel(self.tab_5)
        self.label_19.setGeometry(QtCore.QRect(20, 190, 191, 20))
        self.label_19.setObjectName("label_19")
        self.spinBox_6 = QtWidgets.QSpinBox(self.tab_5)
        self.spinBox_6.setGeometry(QtCore.QRect(250, 110, 61, 41))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.tab_5)
        self.spinBox_7.setGeometry(QtCore.QRect(250, 180, 61, 41))
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setGeometry(QtCore.QRect(340, 120, 71, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setGeometry(QtCore.QRect(340, 190, 100, 20))
        self.label_22.setObjectName("label_22")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_2.setGeometry(QtCore.QRect(450, 120, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_3.setGeometry(QtCore.QRect(450, 190, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.tabWidget_2.addTab(self.tab_5, "")

        ##########################      DATA FROM BASE      ###############################

        self.stackedWidget.addWidget(self.page_newroom)
        self.page_exist = QtWidgets.QWidget()
        self.page_exist.setObjectName("page_exist")
        self.tabWidget = QtWidgets.QTabWidget(self.page_exist)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1111, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1091, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.gridLayoutWidget)
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.gridLayout.addWidget(self.verticalScrollBar_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1091, 561))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.gridLayoutWidget_2)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.gridLayout_2.addWidget(self.verticalScrollBar_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 1091, 561))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.gridLayoutWidget_3)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_3.addWidget(self.verticalScrollBar, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.stackedWidget.addWidget(self.page_exist)
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_main_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_main))
        self.btn_addreserv_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_newrent))
        self.btn_actualreserv_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_exist))
        self.btn_addroom_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_newroom))
        self.buttonBox_2.accepted.connect(self.create_newapartment)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M-Hotel"))
        self.title.setText(_translate("MainWindow", "NOWA REZERWACJA "))
        self.name_2.setText(_translate("MainWindow", "IMIE"))
        self.surname.setText(_translate("MainWindow", "NAZWISKO"))
        self.pesel.setText(_translate("MainWindow", "PESEL"))
        self.city.setText(_translate("MainWindow", "MIASTO"))
        self.street.setText(_translate("MainWindow", "ULICA"))
        self.nFlat.setText(_translate("MainWindow", "NUMER MIESZKANIA"))
        self.room.setText(_translate("MainWindow", "NUMER POKOJU"))
        self.lName.setPlaceholderText(_translate("MainWindow", "Imie"))
        self.lSurname.setPlaceholderText(_translate("MainWindow", "Nazwisko"))
        self.lPesel.setPlaceholderText(_translate("MainWindow", "Pesel"))
        self.lCity.setPlaceholderText(_translate("MainWindow", "Miasto"))
        self.lStreet.setPlaceholderText(_translate("MainWindow", "Ulica"))
        self.lNFlat.setPlaceholderText(_translate("MainWindow", "Numer mieszkania"))
        self.groupBox.setTitle(_translate("MainWindow", "Standard"))
        self.radioButton.setText(_translate("MainWindow", "Exclusive"))
        self.radioButton_2.setText(_translate("MainWindow", "Medium"))
        self.radioButton_3.setText(_translate("MainWindow", "Normal"))
        self.title_2.setText(_translate("MainWindow", "NOWE ZAKWATEROWANIE "))
        self.label_10.setText(_translate("MainWindow", "NUMER POKOJU"))
        self.label_11.setText(_translate("MainWindow", "CENA"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Numer pokoju"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Cena"))
        self.label_13.setText(_translate("MainWindow", "POJEDYŃCZE ŁÓŻKA"))
        self.label_14.setText(_translate("MainWindow", "PODWÓJNE ŁÓŻKA"))
        self.label_15.setText(_translate("MainWindow", "ILOŚĆ ŁAZIENEK"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "   APARTAMENT   "))
        self.label_16.setText(_translate("MainWindow", "POJEDYŃCZE ŁÓŻKA"))
        self.label_17.setText(_translate("MainWindow", "PRYWATNA ŁAZIENKA"))
        self.checkBox.setText(_translate("MainWindow", "TAK"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "  POKÓJ  "))
        self.label_18.setText(_translate("MainWindow", "POJEDYŃCZE ŁÓŻKA"))
        self.label_20.setText(_translate("MainWindow", "PODWÓJNE ŁÓŻKA"))
        self.label_19.setText(_translate("MainWindow", "ILOŚĆ ŁAZIENEK"))
        self.label_21.setText(_translate("MainWindow", "BASEN"))
        self.label_22.setText(_translate("MainWindow", "KUCHNIA"))
        self.checkBox_2.setText(_translate("MainWindow", "TAK"))
        self.checkBox_3.setText(_translate("MainWindow", "TAK"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5),
                                    _translate("MainWindow", "     DOMEK LETNISKOWY     "))
        self.label.setText(_translate("MainWindow", "ZŁ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "   REZERWACJE   "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "  POKOJE  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "  KLIENCI  "))

    def create_newapartment(self):
        flat_number = self.lineEdit_9
        price = self.lineEdit_10
        beds = self.spinBox_3.value()
        doublebeds = self.spinBox_4.value()
        bathroom = self.spinBox_5.value()
        nr = Apartment(flat_number, beds, price, doublebeds, bathroom)
        dbr.write(nr)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
