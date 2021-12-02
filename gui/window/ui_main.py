# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import gui.icons.icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(856, 666)
        MainWindow.setMinimumSize(QSize(856, 480))
        MainWindow.setStyleSheet(u"background-color: rgb(9, 65, 82);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"		color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 50)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 15, 9, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(39, 40, 34);\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align: left;		\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	\n"
"	border-radius: 5px;		\n"
"	background-color: rgb(47, 164, 210);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(47, 164, 210);\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 81, 471))
        self.page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_add = QPushButton(self.page)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(0, 30))
        self.btn_add.setSizeIncrement(QSize(0, 0))
        self.btn_add.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_add)

        self.btn_contacts = QPushButton(self.page)
        self.btn_contacts.setObjectName(u"btn_contacts")
        self.btn_contacts.setMinimumSize(QSize(0, 30))
        self.btn_contacts.setSizeIncrement(QSize(0, 0))
        self.btn_contacts.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_contacts)

        self.btn_about = QPushButton(self.page)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(0, 30))
        self.btn_about.setSizeIncrement(QSize(0, 0))
        self.btn_about.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_about)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 99, 471))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 9, 10)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 4, -1, 1)
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/icons/D:/UFAL/Projeto de Software/Projeto-de-Software/gui/icons/icons/mymenu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.lbl_payroll = QLabel(self.top_frame)
        self.lbl_payroll.setObjectName(u"lbl_payroll")

        self.horizontalLayout_2.addWidget(self.lbl_payroll)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(39, 40, 34);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_7.addWidget(self.logo)

        self.pages.addWidget(self.pg_home)
        self.pg_add = QWidget()
        self.pg_add.setObjectName(u"pg_add")
        self.verticalLayout_8 = QVBoxLayout(self.pg_add)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_add)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setStyleSheet(u"")
        self.tab_add = QWidget()
        self.tab_add.setObjectName(u"tab_add")
        self.verticalLayout_11 = QVBoxLayout(self.tab_add)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_4 = QFrame(self.tab_add)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(47, 164, 210);\n"
"	border-radius: 2px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"\n"
"\n"
" ")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_name = QLineEdit(self.frame_4)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_name, 1, 0, 1, 1)

        self.txt_adress = QLineEdit(self.frame_4)
        self.txt_adress.setObjectName(u"txt_adress")
        self.txt_adress.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_adress, 2, 0, 1, 1)

        self.txt_type = QLineEdit(self.frame_4)
        self.txt_type.setObjectName(u"txt_type")
        self.txt_type.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_type, 3, 0, 1, 1)

        self.txt_Id = QLineEdit(self.frame_4)
        self.txt_Id.setObjectName(u"txt_Id")
        self.txt_Id.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_Id, 4, 0, 1, 1)

        self.lbl_employee = QLabel(self.frame_4)
        self.lbl_employee.setObjectName(u"lbl_employee")
        self.lbl_employee.setStyleSheet(u"color: rgb(47, 164, 210)\n"
"")

        self.gridLayout.addWidget(self.lbl_employee, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.btn_ok = QPushButton(self.tab_add)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(100, 30))
        self.btn_ok.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(47, 164, 210);\n"
"	border-radius: 15px;\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"		border-radius: 15px;\n"
"	background-color: rgb(9, 65, 82);\n"
"}\n"
"\n"
"")

        self.verticalLayout_11.addWidget(self.btn_ok, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_add, "")
        self.tab_employees = QWidget()
        self.tab_employees.setObjectName(u"tab_employees")
        self.verticalLayout_10 = QVBoxLayout(self.tab_employees)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.tab_employees)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(47, 164, 210)\n"
"")

        self.verticalLayout_10.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.tab_employees)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(47, 164, 210);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(47, 164, 210);\n"
"}")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_employees)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(9, 65, 82);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(47, 164, 210);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(70, 30))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(47, 164, 210);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excel)

        self.bnt_edit = QPushButton(self.frame_3)
        self.bnt_edit.setObjectName(u"bnt_edit")
        self.bnt_edit.setMinimumSize(QSize(70, 30))
        self.bnt_edit.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(47, 164, 210);\n"
"}")

        self.verticalLayout_9.addWidget(self.bnt_edit)

        self.btn_delete = QPushButton(self.frame_3)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(70, 30))
        self.btn_delete.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(47, 164, 210);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_delete)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_employees, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_add)
        self.pg_contats = QWidget()
        self.pg_contats.setObjectName(u"pg_contats")
        self.verticalLayout_13 = QVBoxLayout(self.pg_contats)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.pg_contats)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)

        self.label = QLabel(self.pg_contats)
        self.label.setObjectName(u"label")

        self.verticalLayout_13.addWidget(self.label)

        self.pages.addWidget(self.pg_contats)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.verticalLayout_12 = QVBoxLayout(self.pg_about)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lbl_about = QLabel(self.pg_about)
        self.lbl_about.setObjectName(u"lbl_about")
        self.lbl_about.setStyleSheet(u"color: rgb(47, 164, 210)\n"
"")

        self.verticalLayout_12.addWidget(self.lbl_about)

        self.lbl_projsoft = QLabel(self.pg_about)
        self.lbl_projsoft.setObjectName(u"lbl_projsoft")
        self.lbl_projsoft.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.lbl_projsoft)

        self.pages.addWidget(self.pg_about)

        self.verticalLayout_6.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 7, -1, 5)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">MENU</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contacts.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Projeto de Sofware</p><p align=\"center\">2021.1</p><p align=\"center\">P2</p><p align=\"center\"><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle.setText("")
        self.lbl_payroll.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">SISTEMA DE FOLHA DE PAGAMENTO</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/D:/UFAL/Projeto de Software/Projeto-de-Software/gui/icons/icons/icon_logo_2.png\"/></p></body></html>", None))
        self.txt_name.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.txt_adress.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.txt_adress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.txt_type.setText(QCoreApplication.translate("MainWindow", u"Tipo do Empregado", None))
        self.txt_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Employee Type", None))
        self.txt_Id.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.txt_Id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.lbl_employee.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">EMPREGADO</span></p></body></html>", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_add), QCoreApplication.translate("MainWindow", u"add", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">EMPREGADOS CADASTRADOS</span></p><p align=\"center\"><br/></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.bnt_edit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_employees), QCoreApplication.translate("MainWindow", u"Employees", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/D:/UFAL/Projeto de Software/Projeto-de-Software/gui/icons/icons/githubico.png\"/><a href=\"https://github.com/MarlosBalbino/Projeto-de-Software\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">GitHub</span></a></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/D:/UFAL/Projeto de Software/Projeto-de-Software/gui/icons/icons/email_ico.png\"/><a href=\"mbn2@ic.ufal.br\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">mbn2@ic.ufal.br</span></a></p></body></html>", None))
        self.lbl_about.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">SOBRE</span></p></body></html>", None))
        self.lbl_projsoft.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Projeto de Software - 2021.1</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:700;\">Sistema de Folha de Pagamento</span></p><p><br/>O objetivo do projeto \u00e9 construir um sistema de folha de pagamento. O sistema consiste do<br/>gerenciamento de pagamentos dos empregados de uma empresa. Al\u00e9m disso, o sistema deve<br/>gerenciar os dados destes empregados, a exemplo os cart\u00f5es de pontos. Empregados devem receber<br/>o sal\u00e1rio no momento correto, usando o m\u00e9todo que eles preferem, obedecendo v\u00e1rias taxas e<br/>impostos deduzidos do sal\u00e1rio. </p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u00a9\ufe0fmbn2</span></p></body></html>", None))
    # retranslateUi

