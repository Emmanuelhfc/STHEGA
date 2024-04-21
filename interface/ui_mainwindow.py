# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1265, 872)
        font = QFont()
        font.setPointSize(1)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.tab_StyleSheet = QWidget(MainWindow)
        self.tab_StyleSheet.setObjectName(u"tab_StyleSheet")
        self.tab_StyleSheet.setStyleSheet(u"/*///////////////////////////////////////\n"
"Baseado em: WANDERSON M.PIMENTA, v 1.0.0\n"
"Adaptado por: EMMANUEL CRAVALHO\n"
"*/\n"
"/*Cores WEG \n"
"\n"
"do mais escuro para mais claro\n"
"(16,47,76)\n"
"(10,45, 109)\n"
"(39,129, 190)\n"
"(40, 185, 218)\n"
"(34, 186, 222)\n"
"(150, 201, 229)\n"
"(162, 216, 230)\n"
"\n"
"*/\n"
"\n"
"/*///////////////////// ELEMENTOS GERAIS//////////////////////////////*/\n"
"/*GERAL*/\n"
"QWidget{\n"
"	color: #ffffff;\n"
"	font: 10pt \"Arial\";\n"
"}\n"
"QCheckBox{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"/*Bal\u00f5es de help*/\n"
"\n"
"/*Tabelas*/\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(34, 186, 222);\n"
"}\n"
"QTableWidget"
                        "::QLabel{\n"
"    border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(39,129, 190);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(39,129, 190);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(0, 117, 190);\n"
"	background-color: rgb(0, 117, 190);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/*Scroll Bar*/\n"
"/*horizontal*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(0, 117, 190);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
""
                        "QScrollBar::handle:horizontal {\n"
"    background: rgb(39,129, 190);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(0, 117, 190);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(0, 117, 190);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"/*vertical*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(0, 117, 190);\n"
"    width: 8px;\n"
"    margin: 21px"
                        " 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(39,129, 190);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(0, 117, 190);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(0, 117, 190);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/*LINE EDIT*/\n"
"/* N\u00e3o estava funcionando por aqui, foi aplicadodiretamente*/\n"
""
                        "\n"
"/*/////////////////////FRAMES//////////////////////////////*/\n"
"/*app_conteiner  */\n"
"#app_conteiner {	\n"
"	background-color: rgb(0, 117, 190);\n"
"	border: 1px solid rgb(0, 117, 190);\n"
"}\n"
"#tab_login{\n"
"	border: 3px solid rgb(39,129, 190);\n"
"	border-style: solid;\n"
"	border-radius: 5px;\n"
"}\n"
"#tab_register{\n"
"	border: 3px solid rgb(39,129, 190);\n"
"	border-style: solid;\n"
"	border-radius: 5px;\n"
"}\n"
"/*main_botton*/\n"
"#main_botton{\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(0, 117, 190);\n"
"	border-top: 3px solid rgb(0, 117, 190);\n"
"	\n"
"}\n"
"/*botton_bar*/\n"
"#botton_bar { \n"
"	background-color: rgb(0, 117, 190); \n"
"}\n"
"\n"
"/*///////////////////// ELEMENTOS ESPEC\u00cdFICOS//////////////////////////////*/\n"
"/* botton_bar*/\n"
"#botton_bar QLabel { \n"
"	font-size: 11px; color: rgb(113, 126, 149); \n"
"	padding-right: 10px; \n"
"	padding-left: 10px;\n"
"	padding-bottom: 2px; \n"
"}\n"
"\n"
"/* menu_box */\n"
"#menu_box .QPushButton {\n"
""
                        "    background-repeat: no-repeat;\n"
"    background-position: center center;	\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"}\n"
"#menu_box .QPushButton:hover {\n"
"	background-color: rgb(162, 216, 230);\n"
"}\n"
"#menu_box .QPushButton:pressed {	\n"
"	background-color: rgb(39,129, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#top_logo{\n"
"	border-top: 3px solid rgb(0, 117, 190);\n"
"}\n"
"\n"
"/*main_top*/\n"
"#main_top .QPushButton { \n"
"	background-color: rgba(255, 255, 255, 0);   \n"
"	border-radius: 5px;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"}\n"
"#main_top .QPushButton:hover { \n"
"	background-color: rgb(44, 49, 57); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}\n"
"#main_top .QPushButton:pressed { \n"
"	background-color: rgb(23, 26, 30); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}\n"
""
                        "\n"
"/* N\u00e3o estava funcionando por aqui, foi aplicadodiretamente*/")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_StyleSheet)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.app_conteiner = QFrame(self.tab_StyleSheet)
        self.app_conteiner.setObjectName(u"app_conteiner")
        self.app_conteiner.setFrameShape(QFrame.StyledPanel)
        self.app_conteiner.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.app_conteiner)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_box = QFrame(self.app_conteiner)
        self.menu_box.setObjectName(u"menu_box")
        self.menu_box.setMinimumSize(QSize(60, 0))
        self.menu_box.setMaximumSize(QSize(60, 16777215))
        self.menu_box.setFrameShape(QFrame.StyledPanel)
        self.menu_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.menu_box)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.top_logo = QFrame(self.menu_box)
        self.top_logo.setObjectName(u"top_logo")
        self.top_logo.setMinimumSize(QSize(0, 50))
        self.top_logo.setMaximumSize(QSize(16777215, 80))
        self.top_logo.setStyleSheet(u"")
        self.top_logo.setFrameShape(QFrame.StyledPanel)
        self.top_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.top_logo)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.top_logo)

        self.mid_menu = QFrame(self.menu_box)
        self.mid_menu.setObjectName(u"mid_menu")
        self.mid_menu.setFrameShape(QFrame.StyledPanel)
        self.mid_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.mid_menu)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_home = QPushButton(self.mid_menu)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setMinimumSize(QSize(0, 60))
        self.btn_menu_home.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_menu_home.setFont(font1)
        self.btn_menu_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_menu_home)

        self.btn_menu_create_dysse = QPushButton(self.mid_menu)
        self.btn_menu_create_dysse.setObjectName(u"btn_menu_create_dysse")
        self.btn_menu_create_dysse.setMinimumSize(QSize(0, 60))
        self.btn_menu_create_dysse.setMaximumSize(QSize(16777215, 60))
        self.btn_menu_create_dysse.setFont(font1)
        self.btn_menu_create_dysse.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_configurador.png);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_menu_create_dysse)

        self.btn_menu_reader = QPushButton(self.mid_menu)
        self.btn_menu_reader.setObjectName(u"btn_menu_reader")
        self.btn_menu_reader.setMinimumSize(QSize(0, 60))
        self.btn_menu_reader.setMaximumSize(QSize(16777215, 60))
        self.btn_menu_reader.setFont(font1)
        self.btn_menu_reader.setStyleSheet(u"background-image: url(:/icons/images/icons/search.png);")

        self.verticalLayout_10.addWidget(self.btn_menu_reader)

        self.btn_tab_suggestions = QPushButton(self.mid_menu)
        self.btn_tab_suggestions.setObjectName(u"btn_tab_suggestions")
        self.btn_tab_suggestions.setMinimumSize(QSize(0, 60))
        self.btn_tab_suggestions.setMaximumSize(QSize(16777215, 60))
        self.btn_tab_suggestions.setStyleSheet(u"background-image: url(:/icons/images/icons/chat_icon.png);")

        self.verticalLayout_10.addWidget(self.btn_tab_suggestions)

        self.btn_release_notes = QPushButton(self.mid_menu)
        self.btn_release_notes.setObjectName(u"btn_release_notes")
        self.btn_release_notes.setMinimumSize(QSize(0, 60))
        self.btn_release_notes.setMaximumSize(QSize(16777215, 60))
        self.btn_release_notes.setStyleSheet(u"background-image: url(:/images/images/icons/escrita_icon.png);")

        self.verticalLayout_10.addWidget(self.btn_release_notes)

        self.frame_space_mid_menu = QFrame(self.mid_menu)
        self.frame_space_mid_menu.setObjectName(u"frame_space_mid_menu")
        self.frame_space_mid_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_space_mid_menu.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_space_mid_menu)


        self.verticalLayout_8.addWidget(self.mid_menu)

        self.bot_menu = QFrame(self.menu_box)
        self.bot_menu.setObjectName(u"bot_menu")
        self.bot_menu.setMinimumSize(QSize(0, 60))
        self.bot_menu.setMaximumSize(QSize(16777215, 60))
        self.bot_menu.setFrameShape(QFrame.StyledPanel)
        self.bot_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.bot_menu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_logoff = QPushButton(self.bot_menu)
        self.btn_logoff.setObjectName(u"btn_logoff")
        self.btn_logoff.setMinimumSize(QSize(0, 60))
        self.btn_logoff.setMaximumSize(QSize(16777215, 60))
        self.btn_logoff.setStyleSheet(u"background-image: url(:/icons/images/icons/logout_icon.png);")

        self.verticalLayout_11.addWidget(self.btn_logoff)


        self.verticalLayout_8.addWidget(self.bot_menu)


        self.horizontalLayout.addWidget(self.menu_box)

        self.extraLeft_box = QFrame(self.app_conteiner)
        self.extraLeft_box.setObjectName(u"extraLeft_box")
        self.extraLeft_box.setMinimumSize(QSize(0, 0))
        self.extraLeft_box.setMaximumSize(QSize(0, 16777215))
        self.extraLeft_box.setFrameShape(QFrame.StyledPanel)
        self.extraLeft_box.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.extraLeft_box)

        self.main_box = QFrame(self.app_conteiner)
        self.main_box.setObjectName(u"main_box")
        self.main_box.setStyleSheet(u"")
        self.main_box.setFrameShape(QFrame.NoFrame)
        self.main_box.setFrameShadow(QFrame.Raised)
        self.left_layout = QVBoxLayout(self.main_box)
        self.left_layout.setSpacing(0)
        self.left_layout.setObjectName(u"left_layout")
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.main_top = QFrame(self.main_box)
        self.main_top.setObjectName(u"main_top")
        self.main_top.setMinimumSize(QSize(0, 85))
        self.main_top.setMaximumSize(QSize(16777215, 85))
        self.main_top.setFrameShape(QFrame.StyledPanel)
        self.main_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.main_top)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.title_main_top = QFrame(self.main_top)
        self.title_main_top.setObjectName(u"title_main_top")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_main_top.sizePolicy().hasHeightForWidth())
        self.title_main_top.setSizePolicy(sizePolicy)
        self.title_main_top.setFrameShape(QFrame.StyledPanel)
        self.title_main_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.title_main_top)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.title_main_top)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(300, 0))
        self.frame_21.setMaximumSize(QSize(300, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_21)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_21)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 700 30pt \"Romantic\";\n"
"color: white;")

        self.verticalLayout_14.addWidget(self.label_15)

        self.name_tela = QLabel(self.frame_21)
        self.name_tela.setObjectName(u"name_tela")
        self.name_tela.setStyleSheet(u"color: #FAC710;\n"
"font: 700 20pt \"Sitka\";")

        self.verticalLayout_14.addWidget(self.name_tela)


        self.horizontalLayout_11.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.title_main_top)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 5)
        self.logo_tela = QFrame(self.frame_22)
        self.logo_tela.setObjectName(u"logo_tela")
        self.logo_tela.setStyleSheet(u"background-image: url(:/images/images/images/creator_logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;")
        self.logo_tela.setFrameShape(QFrame.StyledPanel)
        self.logo_tela.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.logo_tela)


        self.horizontalLayout_11.addWidget(self.frame_22)


        self.horizontalLayout_9.addWidget(self.title_main_top)

        self.marca_top_rigth = QFrame(self.main_top)
        self.marca_top_rigth.setObjectName(u"marca_top_rigth")
        self.marca_top_rigth.setMinimumSize(QSize(300, 28))
        self.marca_top_rigth.setFrameShape(QFrame.StyledPanel)
        self.marca_top_rigth.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.marca_top_rigth)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 20, 0)
        self.frame_13 = QFrame(self.marca_top_rigth)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(10, 40))
        self.frame_13.setMaximumSize(QSize(16777215, 40))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 10, 0)
        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(60, 34))
        self.frame_18.setMaximumSize(QSize(60, 34))
        self.frame_18.setStyleSheet(u"background-image: url(:/images/images/images/weg_logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right center;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_18)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.marca_top_rigth)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"color: #ffffff;\n"
"font: 12pt \"Swis721 Blk BT\";\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Swis721 Blk BT"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_6.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_13.addWidget(self.frame_14)


        self.horizontalLayout_9.addWidget(self.marca_top_rigth)


        self.left_layout.addWidget(self.main_top)

        self.main_botton = QFrame(self.main_box)
        self.main_botton.setObjectName(u"main_botton")
        self.main_botton.setStyleSheet(u"")
        self.main_botton.setFrameShape(QFrame.StyledPanel)
        self.main_botton.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_botton)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_msg = QFrame(self.main_botton)
        self.frame_msg.setObjectName(u"frame_msg")
        self.frame_msg.setMinimumSize(QSize(0, 37))
        self.frame_msg.setStyleSheet(u"QPushButton {\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;	\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 216, 230);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(39,129, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_msg.setFrameShape(QFrame.StyledPanel)
        self.frame_msg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_msg)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(23, 5, 30, 0)
        self.status_msg = QLabel(self.frame_msg)
        self.status_msg.setObjectName(u"status_msg")
        self.status_msg.setMinimumSize(QSize(0, 25))
        self.status_msg.setMaximumSize(QSize(16777215, 25))
        self.status_msg.setMargin(30)

        self.horizontalLayout_6.addWidget(self.status_msg)

        self.pushButton_2 = QPushButton(self.frame_msg)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(40, 30))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/icons/images/icons/brasil.png);")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_msg)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 30))
        self.pushButton_3.setMaximumSize(QSize(40, 30))
        self.pushButton_3.setStyleSheet(u"background-image: url(:/icons/images/icons/estados-unidos.png);")

        self.horizontalLayout_6.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.frame_msg)

        self.main_content = QFrame(self.main_botton)
        self.main_content.setObjectName(u"main_content")
        self.main_content.setStyleSheet(u"")
        self.main_content.setFrameShape(QFrame.StyledPanel)
        self.main_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pages_container = QFrame(self.main_content)
        self.pages_container.setObjectName(u"pages_container")
        self.pages_container.setStyleSheet(u"")
        self.pages_container.setFrameShape(QFrame.StyledPanel)
        self.pages_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pages_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.avaliation_tabs = QTabWidget(self.pages_container)
        self.avaliation_tabs.setObjectName(u"avaliation_tabs")
        self.avaliation_tabs.setStyleSheet(u"color:black;")
        self.avaliation_tabs.setTabBarAutoHide(False)
        self.input_termo = QWidget()
        self.input_termo.setObjectName(u"input_termo")
        self.horizontalLayout_4 = QHBoxLayout(self.input_termo)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.input_termo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.termoTableShell = QTableWidget(self.frame)
        if (self.termoTableShell.columnCount() < 2):
            self.termoTableShell.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.termoTableShell.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.termoTableShell.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.termoTableShell.rowCount() < 9):
            self.termoTableShell.setRowCount(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.termoTableShell.setVerticalHeaderItem(8, __qtablewidgetitem10)
        self.termoTableShell.setObjectName(u"termoTableShell")
        self.termoTableShell.setStyleSheet(u"color: black;")

        self.verticalLayout.addWidget(self.termoTableShell)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.input_termo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.termoTableTube = QTableWidget(self.frame_2)
        if (self.termoTableTube.columnCount() < 2):
            self.termoTableTube.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.termoTableTube.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.termoTableTube.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.termoTableTube.rowCount() < 9):
            self.termoTableTube.setRowCount(9)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.termoTableTube.setVerticalHeaderItem(8, __qtablewidgetitem21)
        self.termoTableTube.setObjectName(u"termoTableTube")
        self.termoTableTube.setStyleSheet(u"color: black;")

        self.verticalLayout_4.addWidget(self.termoTableTube)

        self.name_avaliation = QLineEdit(self.frame_2)
        self.name_avaliation.setObjectName(u"name_avaliation")

        self.verticalLayout_4.addWidget(self.name_avaliation)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.avaliation_tabs.addTab(self.input_termo, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.designInpTable = QTableWidget(self.tab_2)
        if (self.designInpTable.columnCount() < 2):
            self.designInpTable.setColumnCount(2)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.designInpTable.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.designInpTable.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        if (self.designInpTable.rowCount() < 11):
            self.designInpTable.setRowCount(11)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(8, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(9, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.designInpTable.setVerticalHeaderItem(10, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.designInpTable.setItem(0, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.designInpTable.setItem(1, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.designInpTable.setItem(2, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.designInpTable.setItem(3, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.designInpTable.setItem(4, 1, __qtablewidgetitem39)
        self.designInpTable.setObjectName(u"designInpTable")
        self.designInpTable.setGeometry(QRect(10, 20, 481, 381))
        self.designInpTable.setStyleSheet(u"color: black")
        self.calculate_Nt = QPushButton(self.tab_2)
        self.calculate_Nt.setObjectName(u"calculate_Nt")
        self.calculate_Nt.setGeometry(QRect(490, 280, 75, 21))
        self.avaliation_tabs.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.avaliation_tabs)

        self.pages_container_footer = QFrame(self.pages_container)
        self.pages_container_footer.setObjectName(u"pages_container_footer")
        self.pages_container_footer.setFrameShape(QFrame.StyledPanel)
        self.pages_container_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.pages_container_footer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_3 = QFrame(self.pages_container_footer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_3)

        self.next_pages = QPushButton(self.pages_container_footer)
        self.next_pages.setObjectName(u"next_pages")
        self.next_pages.setMinimumSize(QSize(100, 0))
        self.next_pages.setMaximumSize(QSize(100, 16777215))
        self.next_pages.setStyleSheet(u"color:black;")

        self.horizontalLayout_7.addWidget(self.next_pages)


        self.verticalLayout_3.addWidget(self.pages_container_footer)


        self.horizontalLayout_3.addWidget(self.pages_container)

        self.extra_rigth_box = QFrame(self.main_content)
        self.extra_rigth_box.setObjectName(u"extra_rigth_box")
        self.extra_rigth_box.setMaximumSize(QSize(0, 16777215))
        self.extra_rigth_box.setFrameShape(QFrame.StyledPanel)
        self.extra_rigth_box.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.extra_rigth_box)


        self.verticalLayout_2.addWidget(self.main_content)

        self.botton_bar = QFrame(self.main_botton)
        self.botton_bar.setObjectName(u"botton_bar")
        self.botton_bar.setMinimumSize(QSize(0, 25))
        self.botton_bar.setMaximumSize(QSize(16777215, 25))
        self.botton_bar.setFrameShape(QFrame.StyledPanel)
        self.botton_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.botton_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.credits = QLabel(self.botton_bar)
        self.credits.setObjectName(u"credits")
        self.credits.setMinimumSize(QSize(0, 16))
        self.credits.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(False)
        font3.setItalic(False)
        self.credits.setFont(font3)
        self.credits.setStyleSheet(u"color: white;")
        self.credits.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.credits.setMargin(0)

        self.horizontalLayout_2.addWidget(self.credits)

        self.version = QLabel(self.botton_bar)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(0, 16))
        self.version.setMaximumSize(QSize(16777215, 16))
        self.version.setFont(font3)
        self.version.setStyleSheet(u"color: white;")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.version)

        self.frame_size_grip = QFrame(self.botton_bar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_size_grip)


        self.verticalLayout_2.addWidget(self.botton_bar)


        self.left_layout.addWidget(self.main_botton)


        self.horizontalLayout.addWidget(self.main_box)


        self.horizontalLayout_8.addWidget(self.app_conteiner)

        MainWindow.setCentralWidget(self.tab_StyleSheet)

        self.retranslateUi(MainWindow)

        self.avaliation_tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu_home.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_create_dysse.setToolTip(QCoreApplication.translate("MainWindow", u"DYSSE Creator", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu_create_dysse.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_reader.setToolTip(QCoreApplication.translate("MainWindow", u"DYSSE Reader", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu_reader.setText("")
#if QT_CONFIG(tooltip)
        self.btn_tab_suggestions.setToolTip(QCoreApplication.translate("MainWindow", u"Suggestions", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tab_suggestions.setText("")
#if QT_CONFIG(tooltip)
        self.btn_release_notes.setToolTip(QCoreApplication.translate("MainWindow", u"Release Notes", None))
#endif // QT_CONFIG(tooltip)
        self.btn_release_notes.setText("")
#if QT_CONFIG(tooltip)
        self.btn_logoff.setToolTip(QCoreApplication.translate("MainWindow", u"Logout", None))
#endif // QT_CONFIG(tooltip)
        self.btn_logoff.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"HeatExGA", None))
        self.name_tela.setText(QCoreApplication.translate("MainWindow", u"UTFPR - CP", None))
        self.label_6.setText("")
        self.status_msg.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shell SIde", None))
        ___qtablewidgetitem = self.termoTableShell.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem1 = self.termoTableShell.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Unity", None));
        ___qtablewidgetitem2 = self.termoTableShell.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Temperature In (T1)", None));
        ___qtablewidgetitem3 = self.termoTableShell.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Temperature Out (T2)", None));
        ___qtablewidgetitem4 = self.termoTableShell.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Viscosity (mi_q)", None));
        ___qtablewidgetitem5 = self.termoTableShell.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Specific Heat (cp_quente)", None));
        ___qtablewidgetitem6 = self.termoTableShell.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Fouling Factor (Rd_q)", None));
        ___qtablewidgetitem7 = self.termoTableShell.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Thermal Conductivity (k_q)", None));
        ___qtablewidgetitem8 = self.termoTableShell.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Density (rho_q)", None));
        ___qtablewidgetitem9 = self.termoTableShell.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mass Flow Rate (w_q)", None));
        ___qtablewidgetitem10 = self.termoTableShell.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Type (tipo_q)", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tubel SIde", None))
        ___qtablewidgetitem11 = self.termoTableTube.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem12 = self.termoTableTube.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Unity", None));
        ___qtablewidgetitem13 = self.termoTableTube.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Temperature In", None));
        ___qtablewidgetitem14 = self.termoTableTube.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Temperature Out", None));
        ___qtablewidgetitem15 = self.termoTableTube.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Viscosity", None));
        ___qtablewidgetitem16 = self.termoTableTube.verticalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Specific Heat", None));
        ___qtablewidgetitem17 = self.termoTableTube.verticalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Fouling Factor", None));
        ___qtablewidgetitem18 = self.termoTableTube.verticalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Thermal Conductivity", None));
        ___qtablewidgetitem19 = self.termoTableTube.verticalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Density", None));
        ___qtablewidgetitem20 = self.termoTableTube.verticalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Mass Flow Rate", None));
        ___qtablewidgetitem21 = self.termoTableTube.verticalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.avaliation_tabs.setTabText(self.avaliation_tabs.indexOf(self.input_termo), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        ___qtablewidgetitem22 = self.designInpTable.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem23 = self.designInpTable.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Unity", None));
        ___qtablewidgetitem24 = self.designInpTable.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Shell Diameter (Ds)", None));
        ___qtablewidgetitem25 = self.designInpTable.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Shell Thickness (shell_thickness)", None));
        ___qtablewidgetitem26 = self.designInpTable.verticalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Outside Tube Diameter (de_pol)", None));
        ___qtablewidgetitem27 = self.designInpTable.verticalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Length (L)", None));
        ___qtablewidgetitem28 = self.designInpTable.verticalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Tube pitch (passo_pol)", None));
        ___qtablewidgetitem29 = self.designInpTable.verticalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Pitch Type (a_tubos)", None));
        ___qtablewidgetitem30 = self.designInpTable.verticalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Number Of Tube Passes (n)", None));
        ___qtablewidgetitem31 = self.designInpTable.verticalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Number Of Tubes (Nt)", None));
        ___qtablewidgetitem32 = self.designInpTable.verticalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Baffle Spacing (ls)", None));
        ___qtablewidgetitem33 = self.designInpTable.verticalHeaderItem(9)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Baffle Cut (lc)", None));
        ___qtablewidgetitem34 = self.designInpTable.verticalHeaderItem(10)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Tube Wall Correction ((mi/miw) ^ 0.14 )", None));

        __sortingEnabled = self.designInpTable.isSortingEnabled()
        self.designInpTable.setSortingEnabled(False)
        ___qtablewidgetitem35 = self.designInpTable.item(0, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"pol", None));
        ___qtablewidgetitem36 = self.designInpTable.item(1, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"m", None));
        ___qtablewidgetitem37 = self.designInpTable.item(2, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"pol", None));
        ___qtablewidgetitem38 = self.designInpTable.item(3, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"m", None));
        ___qtablewidgetitem39 = self.designInpTable.item(4, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"pol", None));
        self.designInpTable.setSortingEnabled(__sortingEnabled)

        self.calculate_Nt.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.avaliation_tabs.setTabText(self.avaliation_tabs.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.next_pages.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.credits.setText(QCoreApplication.translate("MainWindow", u"By Emmanuel Henrique de Faria Carvalho", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.01", None))
    # retranslateUi

