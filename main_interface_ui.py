# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interface_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(891, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 550))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:#1a1a1a;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"background-color:#0076ff;\n"
"border-style:outlet;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"color:white;\n"
"/*border-left:2px solid transparent;\n"
"border-bottom:2px solid transparent;*/\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3592ff;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_top_side_menu_container = QFrame(self.centralwidget)
        self.left_top_side_menu_container.setObjectName(u"left_top_side_menu_container")
        self.left_top_side_menu_container.setMinimumSize(QSize(0, 0))
        self.left_top_side_menu_container.setMaximumSize(QSize(38, 16777215))
        self.left_top_side_menu_container.setStyleSheet(u"QPushButton{\n"
"background-color:#000000;\n"
"padding:5px 10px;\n"
"border-style:outlet;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"color:white;\n"
"/*border-left:2px solid transparent;\n"
"border-bottom:2px solid transparent;*/\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#0076ff;\n"
"}\n"
"QPushButton:pressed{\n"
"border:none\n"
"}\n"
"QFrame{\n"
"background-color:#000000\n"
"}")
        self.left_top_side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.left_top_side_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_top_side_menu_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.burger_menu_btn = QPushButton(self.left_top_side_menu_container)
        self.burger_menu_btn.setObjectName(u"burger_menu_btn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu-burger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.burger_menu_btn.setIcon(icon)

        self.verticalLayout.addWidget(self.burger_menu_btn, 0, Qt.AlignLeft)

        self.left_side_menu = QFrame(self.left_top_side_menu_container)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setFrameShape(QFrame.StyledPanel)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 0, 0, 0)
        self.homeButton = QPushButton(self.left_side_menu)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(110, 0))
        self.homeButton.setStyleSheet(u"background-image: url(:/icons/icons/16x16/home16x16.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.verticalLayout_5.addWidget(self.homeButton)

        self.installButton = QPushButton(self.left_side_menu)
        self.installButton.setObjectName(u"installButton")
        self.installButton.setMinimumSize(QSize(110, 0))
        self.installButton.setStyleSheet(u"background-image: url(:/icons/icons/16x16/download16x16.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.verticalLayout_5.addWidget(self.installButton)

        self.UninstallButton = QPushButton(self.left_side_menu)
        self.UninstallButton.setObjectName(u"UninstallButton")
        self.UninstallButton.setMinimumSize(QSize(110, 0))
        self.UninstallButton.setStyleSheet(u"background-image: url(:/icons/icons/16x16/trash-free-icon-font.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.verticalLayout_5.addWidget(self.UninstallButton)


        self.verticalLayout.addWidget(self.left_side_menu, 0, Qt.AlignTop)

        self.left_bottom_side_menu = QFrame(self.left_top_side_menu_container)
        self.left_bottom_side_menu.setObjectName(u"left_bottom_side_menu")
        self.left_bottom_side_menu.setFrameShape(QFrame.StyledPanel)
        self.left_bottom_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.left_bottom_side_menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.settingsButton = QPushButton(self.left_bottom_side_menu)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(110, 0))
        self.settingsButton.setStyleSheet(u"background-image: url(:/icons/icons/16x16/settings16x16.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.verticalLayout_6.addWidget(self.settingsButton)

        self.check_for_update_btn = QPushButton(self.left_bottom_side_menu)
        self.check_for_update_btn.setObjectName(u"check_for_update_btn")
        sizePolicy.setHeightForWidth(self.check_for_update_btn.sizePolicy().hasHeightForWidth())
        self.check_for_update_btn.setSizePolicy(sizePolicy)
        self.check_for_update_btn.setMinimumSize(QSize(110, 0))
        self.check_for_update_btn.setAutoFillBackground(False)
        self.check_for_update_btn.setStyleSheet(u"background-image: url(:/icons/icons/16x16/hourglass.png);\n"
"background-repeat:none;\n"
"background-position:left center;")
        self.check_for_update_btn.setFlat(False)

        self.verticalLayout_6.addWidget(self.check_for_update_btn)


        self.verticalLayout.addWidget(self.left_bottom_side_menu, 0, Qt.AlignBottom)


        self.gridLayout_6.addWidget(self.left_top_side_menu_container, 0, 0, 1, 1)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 20))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"background-color: #0076ff;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"}")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_footer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 12, 0)
        self.bottom_title = QLabel(self.main_footer)
        self.bottom_title.setObjectName(u"bottom_title")

        self.horizontalLayout.addWidget(self.bottom_title)

        self.label_StatusBar = QLabel(self.main_footer)
        self.label_StatusBar.setObjectName(u"label_StatusBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_StatusBar.sizePolicy().hasHeightForWidth())
        self.label_StatusBar.setSizePolicy(sizePolicy1)
        self.label_StatusBar.setMinimumSize(QSize(0, 1))
        self.label_StatusBar.setLayoutDirection(Qt.LeftToRight)
        self.label_StatusBar.setStyleSheet(u"")
        self.label_StatusBar.setFrameShape(QFrame.NoFrame)
        self.label_StatusBar.setFrameShadow(QFrame.Plain)
        self.label_StatusBar.setAlignment(Qt.AlignCenter)
        self.label_StatusBar.setMargin(0)

        self.horizontalLayout.addWidget(self.label_StatusBar)

        self.author_desc_label = QLabel(self.main_footer)
        self.author_desc_label.setObjectName(u"author_desc_label")

        self.horizontalLayout.addWidget(self.author_desc_label)


        self.gridLayout_6.addWidget(self.main_footer, 2, 0, 1, 3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.home_page_container = QWidget()
        self.home_page_container.setObjectName(u"home_page_container")
        self.home_page_container.setStyleSheet(u"QFrame{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.466, y2:0, stop:0.233662 #6618ab, stop:0.8 #3b00b3);\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.home_page_container)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.home_page_frame = QFrame(self.home_page_container)
        self.home_page_frame.setObjectName(u"home_page_frame")
        self.home_page_frame.setStyleSheet(u"")
        self.home_page_frame.setFrameShape(QFrame.StyledPanel)
        self.home_page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.home_page_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.home_page_frame)
        self.title_label.setObjectName(u"title_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy2)
        self.title_label.setMinimumSize(QSize(0, 39))
        font = QFont()
        font.setPointSize(32)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color:skyblue;\n"
"background:none;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_label)

        self.choco_desc_label = QLabel(self.home_page_frame)
        self.choco_desc_label.setObjectName(u"choco_desc_label")
        sizePolicy2.setHeightForWidth(self.choco_desc_label.sizePolicy().hasHeightForWidth())
        self.choco_desc_label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(14)
        self.choco_desc_label.setFont(font1)
        self.choco_desc_label.setAutoFillBackground(False)
        self.choco_desc_label.setStyleSheet(u"color:white;\n"
"background:none;")
        self.choco_desc_label.setTextFormat(Qt.AutoText)
        self.choco_desc_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.choco_desc_label)

        self.home_middle_frame = QFrame(self.home_page_frame)
        self.home_middle_frame.setObjectName(u"home_middle_frame")
        self.home_middle_frame.setStyleSheet(u"QFrame{background:none}\n"
"QPushButton{\n"
"background-color:#0076ff;\n"
"padding:2px;\n"
"border-style:outlet;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"color:white;\n"
"/*border-left:2px solid transparent;\n"
"border-bottom:2px solid transparent;*/\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3592ff;\n"
"}\n"
"QPushButton:pressed{\n"
"border:none\n"
"}")
        self.home_middle_frame.setFrameShape(QFrame.StyledPanel)
        self.home_middle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.home_middle_frame)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 40, 6, 0)
        self.Install_Chocolatey_btn = QPushButton(self.home_middle_frame)
        self.Install_Chocolatey_btn.setObjectName(u"Install_Chocolatey_btn")
        sizePolicy.setHeightForWidth(self.Install_Chocolatey_btn.sizePolicy().hasHeightForWidth())
        self.Install_Chocolatey_btn.setSizePolicy(sizePolicy)
        self.Install_Chocolatey_btn.setMaximumSize(QSize(170, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.Install_Chocolatey_btn.setFont(font2)
        self.Install_Chocolatey_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#ff0000;\n"
"padding:2px;\n"
"border-style:outlet;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"color:white;\n"
"/*border-left:2px solid transparent;\n"
"border-bottom:2px solid transparent;*/\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ff2100;\n"
"}\n"
"QPushButton:pressed{\n"
"border:none\n"
"}")
        self.Install_Chocolatey_btn.setCheckable(False)
        self.Install_Chocolatey_btn.setAutoDefault(False)
        self.Install_Chocolatey_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.Install_Chocolatey_btn)

        self.Download_AKMSorter_btn = QPushButton(self.home_middle_frame)
        self.Download_AKMSorter_btn.setObjectName(u"Download_AKMSorter_btn")
        self.Download_AKMSorter_btn.setMaximumSize(QSize(170, 16777215))
        self.Download_AKMSorter_btn.setFont(font2)
        self.Download_AKMSorter_btn.setStyleSheet(u"")
        self.Download_AKMSorter_btn.setCheckable(False)
        self.Download_AKMSorter_btn.setAutoDefault(False)
        self.Download_AKMSorter_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.Download_AKMSorter_btn)

        self.Download_AmazeX_btn = QPushButton(self.home_middle_frame)
        self.Download_AmazeX_btn.setObjectName(u"Download_AmazeX_btn")
        self.Download_AmazeX_btn.setMaximumSize(QSize(170, 16777215))
        self.Download_AmazeX_btn.setFont(font2)
        self.Download_AmazeX_btn.setStyleSheet(u"")
        self.Download_AmazeX_btn.setCheckable(False)
        self.Download_AmazeX_btn.setAutoDefault(False)
        self.Download_AmazeX_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.Download_AmazeX_btn)

        self.home_bottom_frame = QFrame(self.home_middle_frame)
        self.home_bottom_frame.setObjectName(u"home_bottom_frame")
        self.home_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.home_bottom_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.home_bottom_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar = QProgressBar(self.home_bottom_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.verticalLayout_3.addWidget(self.home_bottom_frame, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.home_middle_frame)


        self.verticalLayout_7.addWidget(self.home_page_frame)

        self.stackedWidget.addWidget(self.home_page_container)
        self.install_page_container = QWidget()
        self.install_page_container.setObjectName(u"install_page_container")
        self.install_page_container.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.install_page_container)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_2 = QScrollArea(self.install_page_container)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy3)
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setSizeIncrement(QSize(0, 0))
        self.scrollArea_2.setBaseSize(QSize(0, 0))
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setFrameShadow(QFrame.Raised)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 827, 560))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(0, 560))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"QPushButton:pressed{\n"
"border:none\n"
"}\n"
"QLabel{\n"
"background-color:none;\n"
"}\n"
"#scrollAreaWidgetContents_3{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.466, y2:0, stop:0.233662 #6618ab, stop:0.8 #3b00b3);\n"
"}\n"
"QCheckBox::indicator{\n"
"width:20px;height:20px;\n"
"}\n"
"QCheckBox{\n"
"background-color:none;\n"
"color:white;\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/icons/icons/checkbox-blue-dark/uncheckmark.png);}\n"
"QCheckBox::indicator:unchecked:hover{image: url(:/icons/icons/checkbox-blue-dark/uncheckmark-hover.png);}\n"
"QCheckBox::indicator:checked{image: url(:/icons/icons/checkbox-blue-dark/check-mark.png);}\n"
"QCheckBox::indicator:checked:hover{\n"
"image: url(:/icons/icons/checkbox-blue-dark/check-mark-hover.png);}")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_TeamViewer = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_TeamViewer.setObjectName(u"checkBox_TeamViewer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_TeamViewer.sizePolicy().hasHeightForWidth())
        self.checkBox_TeamViewer.setSizePolicy(sizePolicy4)
        self.checkBox_TeamViewer.setBaseSize(QSize(0, 0))
        self.checkBox_TeamViewer.setFont(font2)
        self.checkBox_TeamViewer.setStyleSheet(u"")
        self.checkBox_TeamViewer.setIconSize(QSize(16, 16))
        self.checkBox_TeamViewer.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_TeamViewer, 14, 3, 1, 1)

        self.label_Utilities = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Utilities.setObjectName(u"label_Utilities")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_Utilities.setFont(font3)

        self.gridLayout.addWidget(self.label_Utilities, 6, 1, 1, 1)

        self.checkBox_Chrome = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Chrome.setObjectName(u"checkBox_Chrome")
        sizePolicy4.setHeightForWidth(self.checkBox_Chrome.sizePolicy().hasHeightForWidth())
        self.checkBox_Chrome.setSizePolicy(sizePolicy4)
        self.checkBox_Chrome.setBaseSize(QSize(0, 0))
        self.checkBox_Chrome.setFont(font2)
        self.checkBox_Chrome.setStyleSheet(u"")
        self.checkBox_Chrome.setIconSize(QSize(16, 16))
        self.checkBox_Chrome.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Chrome, 1, 1, 1, 1)

        self.label_Development = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Development.setObjectName(u"label_Development")
        self.label_Development.setFont(font3)

        self.gridLayout.addWidget(self.label_Development, 0, 3, 1, 1)

        self.label_Browser = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Browser.setObjectName(u"label_Browser")
        self.label_Browser.setFont(font3)

        self.gridLayout.addWidget(self.label_Browser, 0, 1, 1, 1)

        self.checkBox_Duplicati = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Duplicati.setObjectName(u"checkBox_Duplicati")
        sizePolicy4.setHeightForWidth(self.checkBox_Duplicati.sizePolicy().hasHeightForWidth())
        self.checkBox_Duplicati.setSizePolicy(sizePolicy4)
        self.checkBox_Duplicati.setBaseSize(QSize(0, 0))
        self.checkBox_Duplicati.setFont(font2)
        self.checkBox_Duplicati.setStyleSheet(u"")
        self.checkBox_Duplicati.setIconSize(QSize(16, 16))
        self.checkBox_Duplicati.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Duplicati, 16, 1, 1, 1)

        self.checkBox_Everything = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Everything.setObjectName(u"checkBox_Everything")
        sizePolicy4.setHeightForWidth(self.checkBox_Everything.sizePolicy().hasHeightForWidth())
        self.checkBox_Everything.setSizePolicy(sizePolicy4)
        self.checkBox_Everything.setBaseSize(QSize(0, 0))
        self.checkBox_Everything.setFont(font2)
        self.checkBox_Everything.setStyleSheet(u"")
        self.checkBox_Everything.setIconSize(QSize(16, 16))
        self.checkBox_Everything.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Everything, 9, 3, 1, 1)

        self.checkBox_TaskbarX = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_TaskbarX.setObjectName(u"checkBox_TaskbarX")
        sizePolicy4.setHeightForWidth(self.checkBox_TaskbarX.sizePolicy().hasHeightForWidth())
        self.checkBox_TaskbarX.setSizePolicy(sizePolicy4)
        self.checkBox_TaskbarX.setBaseSize(QSize(0, 0))
        self.checkBox_TaskbarX.setFont(font2)
        self.checkBox_TaskbarX.setStyleSheet(u"")
        self.checkBox_TaskbarX.setIconSize(QSize(16, 16))
        self.checkBox_TaskbarX.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_TaskbarX, 8, 3, 1, 1)

        self.label_Other = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Other.setObjectName(u"label_Other")
        self.label_Other.setFont(font3)

        self.gridLayout.addWidget(self.label_Other, 6, 3, 1, 1)

        self.checkBox_Vlc = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Vlc.setObjectName(u"checkBox_Vlc")
        sizePolicy4.setHeightForWidth(self.checkBox_Vlc.sizePolicy().hasHeightForWidth())
        self.checkBox_Vlc.setSizePolicy(sizePolicy4)
        self.checkBox_Vlc.setBaseSize(QSize(0, 0))
        self.checkBox_Vlc.setFont(font2)
        self.checkBox_Vlc.setStyleSheet(u"")
        self.checkBox_Vlc.setIconSize(QSize(16, 16))
        self.checkBox_Vlc.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Vlc, 10, 3, 1, 1)

        self.checkBox_Spotify = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Spotify.setObjectName(u"checkBox_Spotify")
        sizePolicy4.setHeightForWidth(self.checkBox_Spotify.sizePolicy().hasHeightForWidth())
        self.checkBox_Spotify.setSizePolicy(sizePolicy4)
        self.checkBox_Spotify.setBaseSize(QSize(0, 0))
        self.checkBox_Spotify.setFont(font2)
        self.checkBox_Spotify.setStyleSheet(u"")
        self.checkBox_Spotify.setIconSize(QSize(16, 16))
        self.checkBox_Spotify.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Spotify, 11, 3, 1, 1)

        self.checkBox_QtTabBar = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_QtTabBar.setObjectName(u"checkBox_QtTabBar")
        sizePolicy4.setHeightForWidth(self.checkBox_QtTabBar.sizePolicy().hasHeightForWidth())
        self.checkBox_QtTabBar.setSizePolicy(sizePolicy4)
        self.checkBox_QtTabBar.setBaseSize(QSize(0, 0))
        self.checkBox_QtTabBar.setFont(font2)
        self.checkBox_QtTabBar.setStyleSheet(u"")
        self.checkBox_QtTabBar.setIconSize(QSize(16, 16))
        self.checkBox_QtTabBar.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_QtTabBar, 12, 3, 1, 1)

        self.checkBox_AutoHotkey = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_AutoHotkey.setObjectName(u"checkBox_AutoHotkey")
        sizePolicy4.setHeightForWidth(self.checkBox_AutoHotkey.sizePolicy().hasHeightForWidth())
        self.checkBox_AutoHotkey.setSizePolicy(sizePolicy4)
        self.checkBox_AutoHotkey.setBaseSize(QSize(0, 0))
        self.checkBox_AutoHotkey.setFont(font2)
        self.checkBox_AutoHotkey.setStyleSheet(u"")
        self.checkBox_AutoHotkey.setIconSize(QSize(16, 16))
        self.checkBox_AutoHotkey.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_AutoHotkey, 13, 3, 1, 1)

        self.checkBox_Xodo = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Xodo.setObjectName(u"checkBox_Xodo")
        sizePolicy4.setHeightForWidth(self.checkBox_Xodo.sizePolicy().hasHeightForWidth())
        self.checkBox_Xodo.setSizePolicy(sizePolicy4)
        self.checkBox_Xodo.setBaseSize(QSize(0, 0))
        self.checkBox_Xodo.setFont(font2)
        self.checkBox_Xodo.setStyleSheet(u"")
        self.checkBox_Xodo.setIconSize(QSize(16, 16))
        self.checkBox_Xodo.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Xodo, 9, 0, 1, 1)

        self.checkBox_IrfanView = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_IrfanView.setObjectName(u"checkBox_IrfanView")
        self.checkBox_IrfanView.setFont(font2)

        self.gridLayout.addWidget(self.checkBox_IrfanView, 4, 0, 1, 1)

        self.checkBox_VsCode = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_VsCode.setObjectName(u"checkBox_VsCode")
        sizePolicy4.setHeightForWidth(self.checkBox_VsCode.sizePolicy().hasHeightForWidth())
        self.checkBox_VsCode.setSizePolicy(sizePolicy4)
        self.checkBox_VsCode.setBaseSize(QSize(0, 0))
        self.checkBox_VsCode.setFont(font2)
        self.checkBox_VsCode.setStyleSheet(u"")
        self.checkBox_VsCode.setIconSize(QSize(16, 16))
        self.checkBox_VsCode.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_VsCode, 1, 3, 1, 1)

        self.checkBox_Brave = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Brave.setObjectName(u"checkBox_Brave")
        sizePolicy4.setHeightForWidth(self.checkBox_Brave.sizePolicy().hasHeightForWidth())
        self.checkBox_Brave.setSizePolicy(sizePolicy4)
        self.checkBox_Brave.setBaseSize(QSize(0, 0))
        self.checkBox_Brave.setFont(font2)
        self.checkBox_Brave.setStyleSheet(u"")
        self.checkBox_Brave.setIconSize(QSize(16, 16))
        self.checkBox_Brave.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Brave, 2, 1, 1, 1)

        self.checkBox_Telegram = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Telegram.setObjectName(u"checkBox_Telegram")
        sizePolicy4.setHeightForWidth(self.checkBox_Telegram.sizePolicy().hasHeightForWidth())
        self.checkBox_Telegram.setSizePolicy(sizePolicy4)
        self.checkBox_Telegram.setBaseSize(QSize(0, 0))
        self.checkBox_Telegram.setFont(font2)
        self.checkBox_Telegram.setStyleSheet(u"")
        self.checkBox_Telegram.setIconSize(QSize(16, 16))
        self.checkBox_Telegram.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Telegram, 3, 2, 1, 1)

        self.checkBox_Firefox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Firefox.setObjectName(u"checkBox_Firefox")
        sizePolicy4.setHeightForWidth(self.checkBox_Firefox.sizePolicy().hasHeightForWidth())
        self.checkBox_Firefox.setSizePolicy(sizePolicy4)
        self.checkBox_Firefox.setBaseSize(QSize(0, 0))
        self.checkBox_Firefox.setFont(font2)
        self.checkBox_Firefox.setStyleSheet(u"")
        self.checkBox_Firefox.setIconSize(QSize(16, 16))
        self.checkBox_Firefox.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Firefox, 3, 1, 1, 1)

        self.checkBox_ShareX = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_ShareX.setObjectName(u"checkBox_ShareX")
        self.checkBox_ShareX.setFont(font2)

        self.gridLayout.addWidget(self.checkBox_ShareX, 2, 0, 1, 1)

        self.Update_Apps_btn = QPushButton(self.scrollAreaWidgetContents_3)
        self.Update_Apps_btn.setObjectName(u"Update_Apps_btn")
        self.Update_Apps_btn.setMaximumSize(QSize(170, 16777215))
        self.Update_Apps_btn.setFont(font2)
        self.Update_Apps_btn.setStyleSheet(u"")
        self.Update_Apps_btn.setCheckable(False)
        self.Update_Apps_btn.setAutoDefault(False)
        self.Update_Apps_btn.setFlat(False)

        self.gridLayout.addWidget(self.Update_Apps_btn, 3, 4, 1, 1)

        self.label_Documents = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Documents.setObjectName(u"label_Documents")
        sizePolicy2.setHeightForWidth(self.label_Documents.sizePolicy().hasHeightForWidth())
        self.label_Documents.setSizePolicy(sizePolicy2)
        self.label_Documents.setFont(font3)

        self.gridLayout.addWidget(self.label_Documents, 6, 0, 1, 1)

        self.checkBox_Ventoy = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Ventoy.setObjectName(u"checkBox_Ventoy")
        sizePolicy4.setHeightForWidth(self.checkBox_Ventoy.sizePolicy().hasHeightForWidth())
        self.checkBox_Ventoy.setSizePolicy(sizePolicy4)
        self.checkBox_Ventoy.setBaseSize(QSize(0, 0))
        self.checkBox_Ventoy.setFont(font2)
        self.checkBox_Ventoy.setStyleSheet(u"")
        self.checkBox_Ventoy.setIconSize(QSize(16, 16))
        self.checkBox_Ventoy.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Ventoy, 11, 1, 1, 1)

        self.checkBox_Ccleaner = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Ccleaner.setObjectName(u"checkBox_Ccleaner")
        sizePolicy4.setHeightForWidth(self.checkBox_Ccleaner.sizePolicy().hasHeightForWidth())
        self.checkBox_Ccleaner.setSizePolicy(sizePolicy4)
        self.checkBox_Ccleaner.setBaseSize(QSize(0, 0))
        self.checkBox_Ccleaner.setFont(font2)
        self.checkBox_Ccleaner.setStyleSheet(u"")
        self.checkBox_Ccleaner.setIconSize(QSize(16, 16))
        self.checkBox_Ccleaner.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Ccleaner, 8, 1, 1, 1)

        self.checkBox_WinaeroTweaker = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_WinaeroTweaker.setObjectName(u"checkBox_WinaeroTweaker")
        sizePolicy4.setHeightForWidth(self.checkBox_WinaeroTweaker.sizePolicy().hasHeightForWidth())
        self.checkBox_WinaeroTweaker.setSizePolicy(sizePolicy4)
        self.checkBox_WinaeroTweaker.setBaseSize(QSize(0, 0))
        self.checkBox_WinaeroTweaker.setFont(font2)
        self.checkBox_WinaeroTweaker.setStyleSheet(u"")
        self.checkBox_WinaeroTweaker.setIconSize(QSize(16, 16))
        self.checkBox_WinaeroTweaker.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_WinaeroTweaker, 12, 1, 1, 1)

        self.checkBox_Powertoys = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Powertoys.setObjectName(u"checkBox_Powertoys")
        sizePolicy4.setHeightForWidth(self.checkBox_Powertoys.sizePolicy().hasHeightForWidth())
        self.checkBox_Powertoys.setSizePolicy(sizePolicy4)
        self.checkBox_Powertoys.setBaseSize(QSize(0, 0))
        self.checkBox_Powertoys.setFont(font2)
        self.checkBox_Powertoys.setStyleSheet(u"")
        self.checkBox_Powertoys.setIconSize(QSize(16, 16))
        self.checkBox_Powertoys.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Powertoys, 10, 1, 1, 1)

        self.checkBox_7zip = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_7zip.setObjectName(u"checkBox_7zip")
        sizePolicy4.setHeightForWidth(self.checkBox_7zip.sizePolicy().hasHeightForWidth())
        self.checkBox_7zip.setSizePolicy(sizePolicy4)
        self.checkBox_7zip.setBaseSize(QSize(0, 0))
        self.checkBox_7zip.setFont(font2)
        self.checkBox_7zip.setStyleSheet(u"")
        self.checkBox_7zip.setIconSize(QSize(16, 16))
        self.checkBox_7zip.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_7zip, 9, 1, 1, 1)

        self.checkBox_RevoUninstaller = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_RevoUninstaller.setObjectName(u"checkBox_RevoUninstaller")
        sizePolicy4.setHeightForWidth(self.checkBox_RevoUninstaller.sizePolicy().hasHeightForWidth())
        self.checkBox_RevoUninstaller.setSizePolicy(sizePolicy4)
        self.checkBox_RevoUninstaller.setBaseSize(QSize(0, 0))
        self.checkBox_RevoUninstaller.setFont(font2)
        self.checkBox_RevoUninstaller.setStyleSheet(u"")
        self.checkBox_RevoUninstaller.setIconSize(QSize(16, 16))
        self.checkBox_RevoUninstaller.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_RevoUninstaller, 14, 1, 1, 1)

        self.checkBox_Whatsapp = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Whatsapp.setObjectName(u"checkBox_Whatsapp")
        sizePolicy4.setHeightForWidth(self.checkBox_Whatsapp.sizePolicy().hasHeightForWidth())
        self.checkBox_Whatsapp.setSizePolicy(sizePolicy4)
        self.checkBox_Whatsapp.setBaseSize(QSize(0, 0))
        self.checkBox_Whatsapp.setFont(font2)
        self.checkBox_Whatsapp.setStyleSheet(u"")
        self.checkBox_Whatsapp.setIconSize(QSize(16, 16))
        self.checkBox_Whatsapp.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Whatsapp, 2, 2, 1, 1)

        self.checkBox_WindowsTerminal = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_WindowsTerminal.setObjectName(u"checkBox_WindowsTerminal")
        sizePolicy4.setHeightForWidth(self.checkBox_WindowsTerminal.sizePolicy().hasHeightForWidth())
        self.checkBox_WindowsTerminal.setSizePolicy(sizePolicy4)
        self.checkBox_WindowsTerminal.setBaseSize(QSize(0, 0))
        self.checkBox_WindowsTerminal.setFont(font2)
        self.checkBox_WindowsTerminal.setStyleSheet(u"")
        self.checkBox_WindowsTerminal.setIconSize(QSize(16, 16))
        self.checkBox_WindowsTerminal.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_WindowsTerminal, 15, 1, 1, 1)

        self.checkBox_IoUnlocker = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_IoUnlocker.setObjectName(u"checkBox_IoUnlocker")
        sizePolicy4.setHeightForWidth(self.checkBox_IoUnlocker.sizePolicy().hasHeightForWidth())
        self.checkBox_IoUnlocker.setSizePolicy(sizePolicy4)
        self.checkBox_IoUnlocker.setBaseSize(QSize(0, 0))
        self.checkBox_IoUnlocker.setFont(font2)
        self.checkBox_IoUnlocker.setStyleSheet(u"")
        self.checkBox_IoUnlocker.setIconSize(QSize(16, 16))
        self.checkBox_IoUnlocker.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_IoUnlocker, 13, 1, 1, 1)

        self.Titus_Utility_btn = QPushButton(self.scrollAreaWidgetContents_3)
        self.Titus_Utility_btn.setObjectName(u"Titus_Utility_btn")
        self.Titus_Utility_btn.setMaximumSize(QSize(170, 16777215))
        self.Titus_Utility_btn.setFont(font2)
        self.Titus_Utility_btn.setStyleSheet(u"")
        self.Titus_Utility_btn.setCheckable(False)
        self.Titus_Utility_btn.setAutoDefault(False)
        self.Titus_Utility_btn.setFlat(False)

        self.gridLayout.addWidget(self.Titus_Utility_btn, 2, 4, 1, 1)

        self.checkBox_Discord = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Discord.setObjectName(u"checkBox_Discord")
        sizePolicy4.setHeightForWidth(self.checkBox_Discord.sizePolicy().hasHeightForWidth())
        self.checkBox_Discord.setSizePolicy(sizePolicy4)
        self.checkBox_Discord.setBaseSize(QSize(0, 0))
        self.checkBox_Discord.setFont(font2)
        self.checkBox_Discord.setStyleSheet(u"")
        self.checkBox_Discord.setIconSize(QSize(16, 16))
        self.checkBox_Discord.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Discord, 1, 2, 1, 1)

        self.checkBox_Greenshot = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Greenshot.setObjectName(u"checkBox_Greenshot")
        self.checkBox_Greenshot.setFont(font2)

        self.gridLayout.addWidget(self.checkBox_Greenshot, 3, 0, 1, 1)

        self.checkBox_Git = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Git.setObjectName(u"checkBox_Git")
        sizePolicy4.setHeightForWidth(self.checkBox_Git.sizePolicy().hasHeightForWidth())
        self.checkBox_Git.setSizePolicy(sizePolicy4)
        self.checkBox_Git.setBaseSize(QSize(0, 0))
        self.checkBox_Git.setFont(font2)
        self.checkBox_Git.setStyleSheet(u"")
        self.checkBox_Git.setIconSize(QSize(16, 16))
        self.checkBox_Git.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Git, 4, 3, 1, 1)

        self.checkBox_Drawboard = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Drawboard.setObjectName(u"checkBox_Drawboard")
        sizePolicy4.setHeightForWidth(self.checkBox_Drawboard.sizePolicy().hasHeightForWidth())
        self.checkBox_Drawboard.setSizePolicy(sizePolicy4)
        self.checkBox_Drawboard.setBaseSize(QSize(0, 0))
        self.checkBox_Drawboard.setFont(font2)
        self.checkBox_Drawboard.setStyleSheet(u"")
        self.checkBox_Drawboard.setIconSize(QSize(16, 16))
        self.checkBox_Drawboard.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Drawboard, 8, 0, 1, 1)

        self.checkBox_SublimeText = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_SublimeText.setObjectName(u"checkBox_SublimeText")
        sizePolicy4.setHeightForWidth(self.checkBox_SublimeText.sizePolicy().hasHeightForWidth())
        self.checkBox_SublimeText.setSizePolicy(sizePolicy4)
        self.checkBox_SublimeText.setBaseSize(QSize(0, 0))
        self.checkBox_SublimeText.setFont(font2)
        self.checkBox_SublimeText.setStyleSheet(u"")
        self.checkBox_SublimeText.setIconSize(QSize(16, 16))
        self.checkBox_SublimeText.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_SublimeText, 2, 3, 1, 1)

        self.Install_selected_btn = QPushButton(self.scrollAreaWidgetContents_3)
        self.Install_selected_btn.setObjectName(u"Install_selected_btn")
        self.Install_selected_btn.setMaximumSize(QSize(170, 16777215))
        self.Install_selected_btn.setFont(font2)
        self.Install_selected_btn.setStyleSheet(u"")
        self.Install_selected_btn.setCheckable(False)
        self.Install_selected_btn.setAutoDefault(False)
        self.Install_selected_btn.setFlat(False)

        self.gridLayout.addWidget(self.Install_selected_btn, 1, 4, 1, 1)

        self.checkBox_Obsidian = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Obsidian.setObjectName(u"checkBox_Obsidian")
        sizePolicy4.setHeightForWidth(self.checkBox_Obsidian.sizePolicy().hasHeightForWidth())
        self.checkBox_Obsidian.setSizePolicy(sizePolicy4)
        self.checkBox_Obsidian.setBaseSize(QSize(0, 0))
        self.checkBox_Obsidian.setFont(font2)
        self.checkBox_Obsidian.setStyleSheet(u"")
        self.checkBox_Obsidian.setIconSize(QSize(16, 16))
        self.checkBox_Obsidian.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Obsidian, 12, 0, 1, 1)

        self.checkBox_GithubDesktop = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_GithubDesktop.setObjectName(u"checkBox_GithubDesktop")
        sizePolicy4.setHeightForWidth(self.checkBox_GithubDesktop.sizePolicy().hasHeightForWidth())
        self.checkBox_GithubDesktop.setSizePolicy(sizePolicy4)
        self.checkBox_GithubDesktop.setBaseSize(QSize(0, 0))
        self.checkBox_GithubDesktop.setFont(font2)
        self.checkBox_GithubDesktop.setStyleSheet(u"")
        self.checkBox_GithubDesktop.setIconSize(QSize(16, 16))
        self.checkBox_GithubDesktop.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_GithubDesktop, 3, 3, 1, 1)

        self.checkBox_VmwarePlayer = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_VmwarePlayer.setObjectName(u"checkBox_VmwarePlayer")
        sizePolicy4.setHeightForWidth(self.checkBox_VmwarePlayer.sizePolicy().hasHeightForWidth())
        self.checkBox_VmwarePlayer.setSizePolicy(sizePolicy4)
        self.checkBox_VmwarePlayer.setBaseSize(QSize(0, 0))
        self.checkBox_VmwarePlayer.setFont(font2)
        self.checkBox_VmwarePlayer.setStyleSheet(u"")
        self.checkBox_VmwarePlayer.setIconSize(QSize(16, 16))
        self.checkBox_VmwarePlayer.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_VmwarePlayer, 5, 3, 1, 1)

        self.label_Social = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Social.setObjectName(u"label_Social")
        self.label_Social.setFont(font3)

        self.gridLayout.addWidget(self.label_Social, 0, 2, 1, 1)

        self.label_Photos = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Photos.setObjectName(u"label_Photos")
        sizePolicy2.setHeightForWidth(self.label_Photos.sizePolicy().hasHeightForWidth())
        self.label_Photos.setSizePolicy(sizePolicy2)
        self.label_Photos.setFont(font3)

        self.gridLayout.addWidget(self.label_Photos, 0, 0, 1, 1)

        self.checkBox_NotepadPlusPlus = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_NotepadPlusPlus.setObjectName(u"checkBox_NotepadPlusPlus")
        sizePolicy4.setHeightForWidth(self.checkBox_NotepadPlusPlus.sizePolicy().hasHeightForWidth())
        self.checkBox_NotepadPlusPlus.setSizePolicy(sizePolicy4)
        self.checkBox_NotepadPlusPlus.setBaseSize(QSize(0, 0))
        self.checkBox_NotepadPlusPlus.setFont(font2)
        self.checkBox_NotepadPlusPlus.setStyleSheet(u"")
        self.checkBox_NotepadPlusPlus.setIconSize(QSize(16, 16))
        self.checkBox_NotepadPlusPlus.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_NotepadPlusPlus, 10, 0, 1, 1)

        self.checkBox_Notepads = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Notepads.setObjectName(u"checkBox_Notepads")
        sizePolicy4.setHeightForWidth(self.checkBox_Notepads.sizePolicy().hasHeightForWidth())
        self.checkBox_Notepads.setSizePolicy(sizePolicy4)
        self.checkBox_Notepads.setBaseSize(QSize(0, 0))
        self.checkBox_Notepads.setFont(font2)
        self.checkBox_Notepads.setStyleSheet(u"")
        self.checkBox_Notepads.setIconSize(QSize(16, 16))
        self.checkBox_Notepads.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Notepads, 11, 0, 1, 1)

        self.label_Options = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Options.setObjectName(u"label_Options")
        self.label_Options.setFont(font3)
        self.label_Options.setFrameShadow(QFrame.Plain)
        self.label_Options.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Options, 0, 4, 1, 1)

        self.checkBox_Canva = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Canva.setObjectName(u"checkBox_Canva")
        sizePolicy4.setHeightForWidth(self.checkBox_Canva.sizePolicy().hasHeightForWidth())
        self.checkBox_Canva.setSizePolicy(sizePolicy4)
        self.checkBox_Canva.setBaseSize(QSize(0, 0))
        self.checkBox_Canva.setFont(font2)
        self.checkBox_Canva.setStyleSheet(u"")
        self.checkBox_Canva.setIconSize(QSize(16, 16))
        self.checkBox_Canva.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Canva, 1, 0, 1, 1)

        self.checkBox_Keepass = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_Keepass.setObjectName(u"checkBox_Keepass")
        sizePolicy4.setHeightForWidth(self.checkBox_Keepass.sizePolicy().hasHeightForWidth())
        self.checkBox_Keepass.setSizePolicy(sizePolicy4)
        self.checkBox_Keepass.setBaseSize(QSize(0, 0))
        self.checkBox_Keepass.setFont(font2)
        self.checkBox_Keepass.setStyleSheet(u"")
        self.checkBox_Keepass.setIconSize(QSize(16, 16))
        self.checkBox_Keepass.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_Keepass, 8, 2, 1, 1)

        self.label_Security = QLabel(self.scrollAreaWidgetContents_3)
        self.label_Security.setObjectName(u"label_Security")
        self.label_Security.setFont(font3)

        self.gridLayout.addWidget(self.label_Security, 6, 2, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.install_page_container)
        self.uninstall_page_container = QWidget()
        self.uninstall_page_container.setObjectName(u"uninstall_page_container")
        self.uninstall_page_container.setStyleSheet(u"QFrame{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.466, y2:0, stop:0.233662 #6618ab, stop:0.8 #3b00b3);\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.uninstall_page_container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.uninstall_page_frame = QFrame(self.uninstall_page_container)
        self.uninstall_page_frame.setObjectName(u"uninstall_page_frame")
        self.uninstall_page_frame.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"}")
        self.uninstall_page_frame.setFrameShape(QFrame.StyledPanel)
        self.uninstall_page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.uninstall_page_frame)
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.uninstall_page_frame)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 58))
        self.title.setMaximumSize(QSize(16777215, 55))
        font4 = QFont()
        font4.setPointSize(38)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setKerning(True)
        self.title.setFont(font4)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.title)

        self.uninstall_item_list = QFrame(self.uninstall_page_frame)
        self.uninstall_item_list.setObjectName(u"uninstall_item_list")
        self.uninstall_item_list.setStyleSheet(u"#uninstall_item_list{\n"
"background:none;\n"
"border:none;\n"
"max-height:19000;\n"
"}\n"
"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:0.357955 rgba(72, 86, 97, 255), stop:0.704545 rgba(100, 119, 135, 255));\n"
"border-radius:0px;\n"
"border: 1px solid #9cb9d3;\n"
"min-height:40px;\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"min-width:none;\n"
"}\n"
"QPushButton{\n"
"max-width:170px;\n"
"min-height:25px;\n"
"}\n"
"QPushButton:pressed{\n"
"border:none\n"
"}")
        self.uninstall_item_list.setFrameShape(QFrame.StyledPanel)
        self.uninstall_item_list.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.uninstall_item_list)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.item_map = QFrame(self.uninstall_item_list)
        self.item_map.setObjectName(u"item_map")
        self.item_map.setFrameShape(QFrame.StyledPanel)
        self.item_map.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.item_map)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.item_map)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-image: url(:/icons/icons/microsoft/maps32x32.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.MapUninBtn = QPushButton(self.item_map)
        self.MapUninBtn.setObjectName(u"MapUninBtn")

        self.horizontalLayout_5.addWidget(self.MapUninBtn)

        self.MapInsBtn = QPushButton(self.item_map)
        self.MapInsBtn.setObjectName(u"MapInsBtn")

        self.horizontalLayout_5.addWidget(self.MapInsBtn)


        self.gridLayout_2.addWidget(self.item_map, 3, 0, 1, 3)

        self.item_phone = QFrame(self.uninstall_item_list)
        self.item_phone.setObjectName(u"item_phone")
        self.item_phone.setFrameShape(QFrame.StyledPanel)
        self.item_phone.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.item_phone)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.item_phone)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-image: url(:/icons/icons/microsoft/phone link32x32x.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.PhoneUninBtn = QPushButton(self.item_phone)
        self.PhoneUninBtn.setObjectName(u"PhoneUninBtn")

        self.horizontalLayout_8.addWidget(self.PhoneUninBtn)

        self.PhoneInsBtn = QPushButton(self.item_phone)
        self.PhoneInsBtn.setObjectName(u"PhoneInsBtn")

        self.horizontalLayout_8.addWidget(self.PhoneInsBtn)


        self.gridLayout_2.addWidget(self.item_phone, 6, 0, 1, 3)

        self.item_cortana = QFrame(self.uninstall_item_list)
        self.item_cortana.setObjectName(u"item_cortana")
        self.item_cortana.setFrameShape(QFrame.StyledPanel)
        self.item_cortana.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.item_cortana)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.item_cortana)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-image: url(:/icons/icons/microsoft/cortana.png);\n"
"background-repeat:none;\n"
"background-position:left center;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.CortanaUninBtn = QPushButton(self.item_cortana)
        self.CortanaUninBtn.setObjectName(u"CortanaUninBtn")

        self.horizontalLayout_2.addWidget(self.CortanaUninBtn)

        self.CortanaInsBtn = QPushButton(self.item_cortana)
        self.CortanaInsBtn.setObjectName(u"CortanaInsBtn")

        self.horizontalLayout_2.addWidget(self.CortanaInsBtn)


        self.gridLayout_2.addWidget(self.item_cortana, 1, 0, 1, 3)

        self.item_getHelp = QFrame(self.uninstall_item_list)
        self.item_getHelp.setObjectName(u"item_getHelp")
        self.item_getHelp.setFrameShape(QFrame.StyledPanel)
        self.item_getHelp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.item_getHelp)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.item_getHelp)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-image: url(:/icons/icons/microsoft/get help32x32.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.GetHelpUninBtn = QPushButton(self.item_getHelp)
        self.GetHelpUninBtn.setObjectName(u"GetHelpUninBtn")

        self.horizontalLayout_4.addWidget(self.GetHelpUninBtn)

        self.GetHelpInsBtn = QPushButton(self.item_getHelp)
        self.GetHelpInsBtn.setObjectName(u"GetHelpInsBtn")

        self.horizontalLayout_4.addWidget(self.GetHelpInsBtn)


        self.gridLayout_2.addWidget(self.item_getHelp, 2, 0, 1, 3)

        self.item_XboxGameBar = QFrame(self.uninstall_item_list)
        self.item_XboxGameBar.setObjectName(u"item_XboxGameBar")
        self.item_XboxGameBar.setFrameShape(QFrame.StyledPanel)
        self.item_XboxGameBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.item_XboxGameBar)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.item_XboxGameBar)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-image: url(:/icons/icons/microsoft/xbox gamebar32x32x.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.XboxGameBarUninBtn = QPushButton(self.item_XboxGameBar)
        self.XboxGameBarUninBtn.setObjectName(u"XboxGameBarUninBtn")

        self.horizontalLayout_9.addWidget(self.XboxGameBarUninBtn)

        self.XboxGameBarInsBtn = QPushButton(self.item_XboxGameBar)
        self.XboxGameBarInsBtn.setObjectName(u"XboxGameBarInsBtn")

        self.horizontalLayout_9.addWidget(self.XboxGameBarInsBtn)


        self.gridLayout_2.addWidget(self.item_XboxGameBar, 7, 0, 1, 3)

        self.item_MicrosoftEdge = QFrame(self.uninstall_item_list)
        self.item_MicrosoftEdge.setObjectName(u"item_MicrosoftEdge")
        self.item_MicrosoftEdge.setFrameShape(QFrame.StyledPanel)
        self.item_MicrosoftEdge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.item_MicrosoftEdge)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.item_MicrosoftEdge)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-image: url(:/icons/icons/microsoft/microsoft edge.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.EdgeUninBtn = QPushButton(self.item_MicrosoftEdge)
        self.EdgeUninBtn.setObjectName(u"EdgeUninBtn")

        self.horizontalLayout_6.addWidget(self.EdgeUninBtn)

        self.EdgeInsBtn = QPushButton(self.item_MicrosoftEdge)
        self.EdgeInsBtn.setObjectName(u"EdgeInsBtn")

        self.horizontalLayout_6.addWidget(self.EdgeInsBtn)


        self.gridLayout_2.addWidget(self.item_MicrosoftEdge, 4, 0, 1, 3)

        self.item_People = QFrame(self.uninstall_item_list)
        self.item_People.setObjectName(u"item_People")
        self.item_People.setFrameShape(QFrame.StyledPanel)
        self.item_People.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.item_People)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.item_People)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-image: url(:/icons/icons/microsoft/people32x32.png);\n"
"background-repeat:none;\n"
"background-position:left center;")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.PeopleUninBtn = QPushButton(self.item_People)
        self.PeopleUninBtn.setObjectName(u"PeopleUninBtn")

        self.horizontalLayout_7.addWidget(self.PeopleUninBtn)

        self.PeopleInsBtn = QPushButton(self.item_People)
        self.PeopleInsBtn.setObjectName(u"PeopleInsBtn")

        self.horizontalLayout_7.addWidget(self.PeopleInsBtn)


        self.gridLayout_2.addWidget(self.item_People, 5, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.uninstall_item_list, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.uninstall_page_frame)

        self.stackedWidget.addWidget(self.uninstall_page_container)
        self.settings_page_container = QWidget()
        self.settings_page_container.setObjectName(u"settings_page_container")
        self.settings_page_container.setStyleSheet(u"QFrame{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.466, y2:0, stop:0.233662 #6618ab, stop:0.8 #3b00b3);\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.settings_page_container)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_2 = QFrame(self.settings_page_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:white;\n"
"background:none;")

        self.verticalLayout_12.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.settings_page_container)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.Install_Chocolatey_btn.setDefault(False)
        self.Download_AKMSorter_btn.setDefault(False)
        self.Download_AmazeX_btn.setDefault(False)
        self.Update_Apps_btn.setDefault(False)
        self.Titus_Utility_btn.setDefault(False)
        self.Install_selected_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AmazeX Utility", None))
        self.burger_menu_btn.setText("")
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.installButton.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.UninstallButton.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.check_for_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bottom_title.setText(QCoreApplication.translate("MainWindow", u"AmazeX Utility", None))
        self.label_StatusBar.setText(QCoreApplication.translate("MainWindow", u"Current Version: ", None))
        self.author_desc_label.setText(QCoreApplication.translate("MainWindow", u"Developed By EliteFantasy", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"AmazeX Utility", None))
        self.choco_desc_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This Utility Requires<span style=\" font-weight:600;\"> Chocoltey Package Manger </span>to install other Programs</p><p>Make Sure it is <span style=\" font-weight:600;\">Installed </span>on your system  before installing anything!!.</p></body></html>", None))
        self.Install_Chocolatey_btn.setText(QCoreApplication.translate("MainWindow", u"Install Chocolatey", None))
        self.Download_AKMSorter_btn.setText(QCoreApplication.translate("MainWindow", u"Download AKM Sorter", None))
        self.Download_AmazeX_btn.setText(QCoreApplication.translate("MainWindow", u"Download AmazeX", None))
        self.checkBox_TeamViewer.setText(QCoreApplication.translate("MainWindow", u"TeamViewer", None))
        self.label_Utilities.setText(QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.checkBox_Chrome.setText(QCoreApplication.translate("MainWindow", u"Chrome", None))
        self.label_Development.setText(QCoreApplication.translate("MainWindow", u"Development", None))
        self.label_Browser.setText(QCoreApplication.translate("MainWindow", u"Browser", None))
        self.checkBox_Duplicati.setText(QCoreApplication.translate("MainWindow", u"Duplicati", None))
        self.checkBox_Everything.setText(QCoreApplication.translate("MainWindow", u"Everything", None))
        self.checkBox_TaskbarX.setText(QCoreApplication.translate("MainWindow", u"TaskbarX", None))
        self.label_Other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.checkBox_Vlc.setText(QCoreApplication.translate("MainWindow", u"Vlc", None))
        self.checkBox_Spotify.setText(QCoreApplication.translate("MainWindow", u"Spotify", None))
        self.checkBox_QtTabBar.setText(QCoreApplication.translate("MainWindow", u"QtTabBar", None))
        self.checkBox_AutoHotkey.setText(QCoreApplication.translate("MainWindow", u"AutoHotkey", None))
        self.checkBox_Xodo.setText(QCoreApplication.translate("MainWindow", u"Xodo", None))
        self.checkBox_IrfanView.setText(QCoreApplication.translate("MainWindow", u"IrfanView", None))
        self.checkBox_VsCode.setText(QCoreApplication.translate("MainWindow", u"Vs Code", None))
        self.checkBox_Brave.setText(QCoreApplication.translate("MainWindow", u"Brave", None))
        self.checkBox_Telegram.setText(QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.checkBox_Firefox.setText(QCoreApplication.translate("MainWindow", u"Firefox", None))
        self.checkBox_ShareX.setText(QCoreApplication.translate("MainWindow", u"ShareX", None))
        self.Update_Apps_btn.setText(QCoreApplication.translate("MainWindow", u"Update Apps", None))
        self.label_Documents.setText(QCoreApplication.translate("MainWindow", u"Documents", None))
        self.checkBox_Ventoy.setText(QCoreApplication.translate("MainWindow", u"Ventoy", None))
        self.checkBox_Ccleaner.setText(QCoreApplication.translate("MainWindow", u"Ccleaner", None))
        self.checkBox_WinaeroTweaker.setText(QCoreApplication.translate("MainWindow", u"Winaero Tweaker", None))
        self.checkBox_Powertoys.setText(QCoreApplication.translate("MainWindow", u"Powertoys", None))
        self.checkBox_7zip.setText(QCoreApplication.translate("MainWindow", u"7zip", None))
        self.checkBox_RevoUninstaller.setText(QCoreApplication.translate("MainWindow", u"Revo Uninstaller", None))
        self.checkBox_Whatsapp.setText(QCoreApplication.translate("MainWindow", u"Whatsapp", None))
        self.checkBox_WindowsTerminal.setText(QCoreApplication.translate("MainWindow", u"Windows Terminal", None))
        self.checkBox_IoUnlocker.setText(QCoreApplication.translate("MainWindow", u"Io Unlocker", None))
        self.Titus_Utility_btn.setText(QCoreApplication.translate("MainWindow", u"Titus Utility", None))
        self.checkBox_Discord.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.checkBox_Greenshot.setText(QCoreApplication.translate("MainWindow", u"Greenshot", None))
        self.checkBox_Git.setText(QCoreApplication.translate("MainWindow", u"Git", None))
        self.checkBox_Drawboard.setText(QCoreApplication.translate("MainWindow", u"Drawboard", None))
        self.checkBox_SublimeText.setText(QCoreApplication.translate("MainWindow", u"Sublime Text", None))
        self.Install_selected_btn.setText(QCoreApplication.translate("MainWindow", u"Install Selected", None))
        self.checkBox_Obsidian.setText(QCoreApplication.translate("MainWindow", u"Obsidian", None))
        self.checkBox_GithubDesktop.setText(QCoreApplication.translate("MainWindow", u"Github Desktop", None))
        self.checkBox_VmwarePlayer.setText(QCoreApplication.translate("MainWindow", u"Vmware Player", None))
        self.label_Social.setText(QCoreApplication.translate("MainWindow", u"Social", None))
        self.label_Photos.setText(QCoreApplication.translate("MainWindow", u"Photos", None))
        self.checkBox_NotepadPlusPlus.setText(QCoreApplication.translate("MainWindow", u"Notepad++", None))
        self.checkBox_Notepads.setText(QCoreApplication.translate("MainWindow", u"Notepads", None))
        self.label_Options.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.checkBox_Canva.setText(QCoreApplication.translate("MainWindow", u"Canva", None))
        self.checkBox_Keepass.setText(QCoreApplication.translate("MainWindow", u"Keepass", None))
        self.label_Security.setText(QCoreApplication.translate("MainWindow", u"Security", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Windows Apps", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"                Map", None))
        self.MapUninBtn.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.MapInsBtn.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"                Phone link", None))
        self.PhoneUninBtn.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.PhoneInsBtn.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"                Cortana", None))
        self.CortanaUninBtn.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.CortanaInsBtn.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"                Get Help", None))
        self.GetHelpUninBtn.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.GetHelpInsBtn.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"                Xbox Game Bar", None))
        self.XboxGameBarUninBtn.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.XboxGameBarInsBtn.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"                Microsoft edge", None))
        self.EdgeUninBtn.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.EdgeInsBtn.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"                People", None))
        self.PeopleUninBtn.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.PeopleInsBtn.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings Page Coming Soon", None))
    # retranslateUi

