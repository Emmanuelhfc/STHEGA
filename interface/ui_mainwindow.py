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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 60, 16))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 241, 16))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 130, 241, 16))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 220, 241, 16))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 180, 241, 16))
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 270, 241, 16))
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 310, 241, 16))
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 350, 241, 16))
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 400, 241, 16))
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 440, 241, 16))
        self.shell_t_in = QLineEdit(self.frame)
        self.shell_t_in.setObjectName(u"shell_t_in")
        self.shell_t_in.setGeometry(QRect(200, 80, 161, 21))
        self.shell_t_o = QLineEdit(self.frame)
        self.shell_t_o.setObjectName(u"shell_t_o")
        self.shell_t_o.setGeometry(QRect(200, 130, 161, 21))
        self.shell_cp = QLineEdit(self.frame)
        self.shell_cp.setObjectName(u"shell_cp")
        self.shell_cp.setGeometry(QRect(200, 170, 161, 21))
        self.shell_mi = QLineEdit(self.frame)
        self.shell_mi.setObjectName(u"shell_mi")
        self.shell_mi.setGeometry(QRect(200, 220, 161, 21))
        self.shell_Rd = QLineEdit(self.frame)
        self.shell_Rd.setObjectName(u"shell_Rd")
        self.shell_Rd.setGeometry(QRect(200, 270, 161, 21))
        self.shell_k = QLineEdit(self.frame)
        self.shell_k.setObjectName(u"shell_k")
        self.shell_k.setGeometry(QRect(200, 310, 161, 21))
        self.shell_rho = QLineEdit(self.frame)
        self.shell_rho.setObjectName(u"shell_rho")
        self.shell_rho.setGeometry(QRect(200, 350, 161, 21))
        self.shell_w = QLineEdit(self.frame)
        self.shell_w.setObjectName(u"shell_w")
        self.shell_w.setGeometry(QRect(200, 400, 161, 21))
        self.shell_type = QLineEdit(self.frame)
        self.shell_type.setObjectName(u"shell_type")
        self.shell_type.setGeometry(QRect(200, 450, 161, 21))
        self.c_shell_t_in = QComboBox(self.frame)
        self.c_shell_t_in.setObjectName(u"c_shell_t_in")
        self.c_shell_t_in.setGeometry(QRect(390, 80, 121, 22))
        self.c_shell_cp = QComboBox(self.frame)
        self.c_shell_cp.setObjectName(u"c_shell_cp")
        self.c_shell_cp.setGeometry(QRect(390, 170, 121, 22))
        self.c_shell_mi = QComboBox(self.frame)
        self.c_shell_mi.setObjectName(u"c_shell_mi")
        self.c_shell_mi.setGeometry(QRect(390, 220, 121, 22))
        self.c_shell_Rd = QComboBox(self.frame)
        self.c_shell_Rd.setObjectName(u"c_shell_Rd")
        self.c_shell_Rd.setGeometry(QRect(390, 270, 121, 22))
        self.c_shell_k = QComboBox(self.frame)
        self.c_shell_k.setObjectName(u"c_shell_k")
        self.c_shell_k.setGeometry(QRect(390, 310, 121, 22))
        self.c_shell_rho = QComboBox(self.frame)
        self.c_shell_rho.setObjectName(u"c_shell_rho")
        self.c_shell_rho.setGeometry(QRect(390, 350, 121, 22))
        self.c_shell_w = QComboBox(self.frame)
        self.c_shell_w.setObjectName(u"c_shell_w")
        self.c_shell_w.setGeometry(QRect(390, 400, 121, 22))
        self.c_shell_t_o = QComboBox(self.frame)
        self.c_shell_t_o.setObjectName(u"c_shell_t_o")
        self.c_shell_t_o.setGeometry(QRect(390, 130, 121, 22))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 40, 551, 20))
        self.btn_test = QPushButton(self.frame)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setGeometry(QRect(590, 30, 75, 24))

        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_4 = QFrame(self.input_termo)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 10, 60, 16))
        self.label_45 = QLabel(self.frame_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(20, 80, 131, 16))
        self.label_46 = QLabel(self.frame_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(20, 130, 121, 16))
        self.label_47 = QLabel(self.frame_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(20, 220, 111, 16))
        self.label_48 = QLabel(self.frame_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 180, 111, 16))
        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(20, 270, 111, 16))
        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(20, 310, 131, 16))
        self.label_51 = QLabel(self.frame_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(20, 350, 131, 16))
        self.label_52 = QLabel(self.frame_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(20, 400, 181, 16))
        self.label_53 = QLabel(self.frame_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(20, 440, 141, 16))
        self.c_tube_cp = QComboBox(self.frame_4)
        self.c_tube_cp.setObjectName(u"c_tube_cp")
        self.c_tube_cp.setGeometry(QRect(360, 170, 121, 22))
        self.c_tube_mi = QComboBox(self.frame_4)
        self.c_tube_mi.setObjectName(u"c_tube_mi")
        self.c_tube_mi.setGeometry(QRect(360, 220, 121, 22))
        self.c_tube_w = QComboBox(self.frame_4)
        self.c_tube_w.setObjectName(u"c_tube_w")
        self.c_tube_w.setGeometry(QRect(360, 400, 121, 22))
        self.c_tube_t_o = QComboBox(self.frame_4)
        self.c_tube_t_o.setObjectName(u"c_tube_t_o")
        self.c_tube_t_o.setGeometry(QRect(360, 130, 121, 22))
        self.tube_k = QLineEdit(self.frame_4)
        self.tube_k.setObjectName(u"tube_k")
        self.tube_k.setGeometry(QRect(170, 310, 161, 21))
        self.c_tube_rho = QComboBox(self.frame_4)
        self.c_tube_rho.setObjectName(u"c_tube_rho")
        self.c_tube_rho.setGeometry(QRect(360, 350, 121, 22))
        self.tube_rho = QLineEdit(self.frame_4)
        self.tube_rho.setObjectName(u"tube_rho")
        self.tube_rho.setGeometry(QRect(170, 350, 161, 21))
        self.tube_mi = QLineEdit(self.frame_4)
        self.tube_mi.setObjectName(u"tube_mi")
        self.tube_mi.setGeometry(QRect(170, 220, 161, 21))
        self.tube_t_o = QLineEdit(self.frame_4)
        self.tube_t_o.setObjectName(u"tube_t_o")
        self.tube_t_o.setGeometry(QRect(170, 130, 161, 21))
        self.tube_Rd = QLineEdit(self.frame_4)
        self.tube_Rd.setObjectName(u"tube_Rd")
        self.tube_Rd.setGeometry(QRect(170, 270, 161, 21))
        self.tube_w = QLineEdit(self.frame_4)
        self.tube_w.setObjectName(u"tube_w")
        self.tube_w.setGeometry(QRect(170, 400, 161, 21))
        self.c_tube_k = QComboBox(self.frame_4)
        self.c_tube_k.setObjectName(u"c_tube_k")
        self.c_tube_k.setGeometry(QRect(360, 310, 121, 22))
        self.c_tube_t_in = QComboBox(self.frame_4)
        self.c_tube_t_in.setObjectName(u"c_tube_t_in")
        self.c_tube_t_in.setGeometry(QRect(360, 80, 121, 22))
        self.tube_t_in = QLineEdit(self.frame_4)
        self.tube_t_in.setObjectName(u"tube_t_in")
        self.tube_t_in.setGeometry(QRect(170, 80, 161, 21))
        self.tube_cp = QLineEdit(self.frame_4)
        self.tube_cp.setObjectName(u"tube_cp")
        self.tube_cp.setGeometry(QRect(170, 170, 161, 21))
        self.c_tube_Rd = QComboBox(self.frame_4)
        self.c_tube_Rd.setObjectName(u"c_tube_Rd")
        self.c_tube_Rd.setGeometry(QRect(360, 270, 121, 22))
        self.tube_type = QLineEdit(self.frame_4)
        self.tube_type.setObjectName(u"tube_type")
        self.tube_type.setGeometry(QRect(170, 440, 161, 21))

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.avaliation_tabs.addTab(self.input_termo, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.calculate_Nt = QPushButton(self.tab_2)
        self.calculate_Nt.setObjectName(u"calculate_Nt")
        self.calculate_Nt.setGeometry(QRect(680, 370, 75, 21))
        self.label_54 = QLabel(self.tab_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(30, 70, 171, 21))
        self.label_55 = QLabel(self.tab_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(30, 110, 171, 21))
        self.label_56 = QLabel(self.tab_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(30, 150, 171, 21))
        self.label_57 = QLabel(self.tab_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(30, 190, 171, 21))
        self.label_59 = QLabel(self.tab_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(30, 240, 131, 21))
        self.label_60 = QLabel(self.tab_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(30, 320, 171, 21))
        self.label_61 = QLabel(self.tab_2)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(30, 370, 171, 21))
        self.label_62 = QLabel(self.tab_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(30, 420, 171, 21))
        self.label_63 = QLabel(self.tab_2)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(30, 460, 171, 21))
        self.Ds = QLineEdit(self.tab_2)
        self.Ds.setObjectName(u"Ds")
        self.Ds.setGeometry(QRect(210, 70, 251, 21))
        self.shell_thickness = QLineEdit(self.tab_2)
        self.shell_thickness.setObjectName(u"shell_thickness")
        self.shell_thickness.setGeometry(QRect(210, 100, 251, 21))
        self.L = QLineEdit(self.tab_2)
        self.L.setObjectName(u"L")
        self.L.setGeometry(QRect(210, 190, 251, 21))
        self.Nt = QLineEdit(self.tab_2)
        self.Nt.setObjectName(u"Nt")
        self.Nt.setGeometry(QRect(200, 380, 251, 21))
        self.ls = QLineEdit(self.tab_2)
        self.ls.setObjectName(u"ls")
        self.ls.setGeometry(QRect(200, 420, 251, 21))
        self.lc = QLineEdit(self.tab_2)
        self.lc.setObjectName(u"lc")
        self.lc.setGeometry(QRect(200, 470, 251, 21))
        self.c_Ds = QComboBox(self.tab_2)
        self.c_Ds.setObjectName(u"c_Ds")
        self.c_Ds.setGeometry(QRect(490, 70, 141, 22))
        self.c_shell_thickness = QComboBox(self.tab_2)
        self.c_shell_thickness.setObjectName(u"c_shell_thickness")
        self.c_shell_thickness.setGeometry(QRect(490, 100, 141, 22))
        self.c_de_inch = QComboBox(self.tab_2)
        self.c_de_inch.setObjectName(u"c_de_inch")
        self.c_de_inch.setGeometry(QRect(490, 140, 141, 22))
        self.c_L = QComboBox(self.tab_2)
        self.c_L.setObjectName(u"c_L")
        self.c_L.setGeometry(QRect(480, 190, 141, 22))
        self.c_pitch_inch = QComboBox(self.tab_2)
        self.c_pitch_inch.setObjectName(u"c_pitch_inch")
        self.c_pitch_inch.setGeometry(QRect(480, 240, 141, 22))
        self.c_ls = QComboBox(self.tab_2)
        self.c_ls.setObjectName(u"c_ls")
        self.c_ls.setGeometry(QRect(490, 420, 141, 22))
        self.c_lc = QComboBox(self.tab_2)
        self.c_lc.setObjectName(u"c_lc")
        self.c_lc.setGeometry(QRect(490, 470, 141, 22))
        self.label_64 = QLabel(self.tab_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(110, 20, 551, 16))
        self.c_layout = QComboBox(self.tab_2)
        self.c_layout.setObjectName(u"c_layout")
        self.c_layout.setGeometry(QRect(200, 320, 251, 22))
        self.de_inch = QComboBox(self.tab_2)
        self.de_inch.setObjectName(u"de_inch")
        self.de_inch.setGeometry(QRect(210, 140, 241, 22))
        self.pitch_inch = QComboBox(self.tab_2)
        self.pitch_inch.setObjectName(u"pitch_inch")
        self.pitch_inch.setGeometry(QRect(210, 240, 251, 22))
        self.label_65 = QLabel(self.tab_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(30, 280, 131, 21))
        self.n = QComboBox(self.tab_2)
        self.n.setObjectName(u"n")
        self.n.setGeometry(QRect(200, 280, 251, 22))
        self.label_58 = QLabel(self.tab_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(20, 530, 171, 21))
        self.tube_thickness = QLineEdit(self.tab_2)
        self.tube_thickness.setObjectName(u"tube_thickness")
        self.tube_thickness.setGeometry(QRect(200, 530, 251, 21))
        self.c_tube_thickness = QComboBox(self.tab_2)
        self.c_tube_thickness.setObjectName(u"c_tube_thickness")
        self.c_tube_thickness.setGeometry(QRect(500, 530, 141, 22))
        self.label_66 = QLabel(self.tab_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(950, 100, 171, 21))
        self.tube_material = QComboBox(self.tab_2)
        self.tube_material.setObjectName(u"tube_material")
        self.tube_material.setGeometry(QRect(1150, 100, 251, 22))
        self.label_67 = QLabel(self.tab_2)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(940, 160, 171, 21))
        self.c_pressure_class = QComboBox(self.tab_2)
        self.c_pressure_class.addItem("")
        self.c_pressure_class.addItem("")
        self.c_pressure_class.setObjectName(u"c_pressure_class")
        self.c_pressure_class.setGeometry(QRect(1150, 150, 251, 22))
        self.avaliation_tabs.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 541, 521))
        self.tableWidget_2 = QTableWidget(self.tab)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        if (self.tableWidget_2.rowCount() < 6):
            self.tableWidget_2.setRowCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem21)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(630, 40, 541, 231))
        self.tableWidget_3 = QTableWidget(self.tab)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        if (self.tableWidget_3.rowCount() < 19):
            self.tableWidget_3.setRowCount(19)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, __qtablewidgetitem42)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(630, 290, 541, 231))
        self.avaliation_tabs.addTab(self.tab, "")

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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperature In", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temperature Out", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Viscosity", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Specific Heat", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fouling Factor", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Thermal Conductivity", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Density", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Mass Flow Rate", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"'t_in', 't_o', 'mi', 'cp', 'Rd', 'k', 'rho', 'w', 'type'", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Tube SIde", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Temperature In", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Temperature Out", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Viscosity", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Specific Heat", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Fouling Factor", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Thermal Conductivity", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Density", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Mass Flow Rate", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.avaliation_tabs.setTabText(self.avaliation_tabs.indexOf(self.input_termo), QCoreApplication.translate("MainWindow", u"Thermo Inputs", None))
        self.calculate_Nt.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Shell Diameter", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Shell Thickness", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Outiside Tube Diameter", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Legth", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Tube Pitch", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Layout", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Number of tubes", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Baffle Spacing", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Baffle Cut", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"['Ds', 'shell_thickness', 'de_pol', 'L', 'passo_pol', 'a_tubos', 'n', 'Nt', 'ls', 'lc', 'tube_wall_correction']", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Number Passes", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Tube Thickness", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Tube Material", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Pressure Class", None))
        self.c_pressure_class.setItemText(0, QCoreApplication.translate("MainWindow", u"150", None))
        self.c_pressure_class.setItemText(1, QCoreApplication.translate("MainWindow", u"600", None))

        self.avaliation_tabs.setTabText(self.avaliation_tabs.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Heat Duty (Q)", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Log Mean Temp. Diff (LMDT)", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"R", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"S", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"F", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"LMDT (corrected)", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Dotl", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"passo", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Project area (A_proj)", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Overall Heat Transfer Coefficient  min. (Ud_min)", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"inside tube diameter (di)", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Shell Diameter (Dc)", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem16 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"one tube area (at_)", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"tube area (at)", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"mass velocity per area (Gt)", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Reynolds Number of tube (Re_t)", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Heat transfer coeefficient ideal (hi)", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Heat transfer coefficient (hio)", None));
        ___qtablewidgetitem22 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem23 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem24 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"pn", None));
        ___qtablewidgetitem25 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"pp", None));
        ___qtablewidgetitem26 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Sm", None));
        ___qtablewidgetitem27 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Res", None));
        ___qtablewidgetitem28 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"ji", None));
        ___qtablewidgetitem29 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"h_ideal", None));
        ___qtablewidgetitem30 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Fc", None));
        ___qtablewidgetitem31 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"jc", None));
        ___qtablewidgetitem32 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"delta_sb", None));
        ___qtablewidgetitem33 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Ssb", None));
        ___qtablewidgetitem34 = self.tableWidget_3.verticalHeaderItem(10)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"delta_tb", None));
        ___qtablewidgetitem35 = self.tableWidget_3.verticalHeaderItem(11)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Stb", None));
        ___qtablewidgetitem36 = self.tableWidget_3.verticalHeaderItem(12)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"jl", None));
        ___qtablewidgetitem37 = self.tableWidget_3.verticalHeaderItem(13)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Fbp", None));
        ___qtablewidgetitem38 = self.tableWidget_3.verticalHeaderItem(14)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Sbp", None));
        ___qtablewidgetitem39 = self.tableWidget_3.verticalHeaderItem(15)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Nc", None));
        ___qtablewidgetitem40 = self.tableWidget_3.verticalHeaderItem(16)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Nss", None));
        ___qtablewidgetitem41 = self.tableWidget_3.verticalHeaderItem(17)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"jb", None));
        ___qtablewidgetitem42 = self.tableWidget_3.verticalHeaderItem(18)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"jr", None));
        self.avaliation_tabs.setTabText(self.avaliation_tabs.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Results", None))
        self.next_pages.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.credits.setText(QCoreApplication.translate("MainWindow", u"By Emmanuel Henrique de Faria Carvalho", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.01", None))
    # retranslateUi

