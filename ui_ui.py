# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 450)
        MainWindow.setMinimumSize(QSize(650, 450))
        MainWindow.setMaximumSize(QSize(650, 450))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BaseFrame = QFrame(self.centralwidget)
        self.BaseFrame.setObjectName(u"BaseFrame")
        self.BaseFrame.setStyleSheet(u"QFrame{\n"
"\n"
"\n"
"border-radius:20px;\n"
"	\n"
"	background-color: rgb(24, 24, 24);\n"
"	background-color: rgb(12, 12, 12);\n"
"	border:  1px solid rgb(34, 34, 34);\n"
"\n"
"\n"
"}")
        self.BaseFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.BaseFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.windowFrame = QFrame(self.BaseFrame)
        self.windowFrame.setObjectName(u"windowFrame")
        self.windowFrame.setMinimumSize(QSize(650, 0))
        self.windowFrame.setMaximumSize(QSize(16777215, 35))
        self.windowFrame.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgba(255, 255, 255,000);\n"
"border-radius:0px;\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border:none;\n"
"\n"
"\n"
"\n"
"}")
        self.windowFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.windowFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 14, 0)
        self.horizontalSpacer_2 = QSpacerItem(558, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.windowButtonFrame = QFrame(self.windowFrame)
        self.windowButtonFrame.setObjectName(u"windowButtonFrame")
        self.windowButtonFrame.setStyleSheet(u"QFrame{\n"
"background-color: rgba(155, 155, 155,00);\n"
"border-radius:0px;\n"
"}")
        self.windowButtonFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.windowButtonFrame)
        self.horizontalLayout_2.setSpacing(21)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimiseButton = QPushButton(self.windowButtonFrame)
        self.minimiseButton.setObjectName(u"minimiseButton")
        self.minimiseButton.setMinimumSize(QSize(27, 27))
        self.minimiseButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimiseButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	background-image: url(:/newPrefix/assets/minimiseButton.png);\n"
"	background-position:centre;\n"
"background-repeat:none;\n"
"\n"
"}")
        self.minimiseButton.setIconSize(QSize(39, 33))

        self.horizontalLayout_2.addWidget(self.minimiseButton)

        self.closeButton = QPushButton(self.windowButtonFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(27, 27))
        self.closeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	background-image: url(:/newPrefix/assets/closeButton.png);\n"
"	background-position:centre;\n"
"background-repeat:none;\n"
"\n"
"}")
        self.closeButton.setIconSize(QSize(39, 33))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout_3.addWidget(self.windowButtonFrame)


        self.verticalLayout.addWidget(self.windowFrame)

        self.contentFrame = QFrame(self.BaseFrame)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setStyleSheet(u"QFrame{\n"
"background-color: rgba(196, 196, 196,00);\n"
"border-radius:0px;\n"
"border:none;\n"
"}")
        self.contentFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_4 = QGridLayout(self.contentFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(13)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.progressbarTextArea = QFrame(self.contentFrame)
        self.progressbarTextArea.setObjectName(u"progressbarTextArea")
        self.progressbarTextArea.setMaximumSize(QSize(16777215, 134))
        self.progressbarTextArea.setStyleSheet(u"QFrame{\n"
"background-color: rgba(138, 138, 138,00);\n"
"\n"
"\n"
"}")
        self.progressbarTextArea.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout = QGridLayout(self.progressbarTextArea)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(16)
        self.videoTitle = QLabel(self.progressbarTextArea)
        self.videoTitle.setObjectName(u"videoTitle")
        self.videoTitle.setMinimumSize(QSize(0, 16))
        self.videoTitle.setMaximumSize(QSize(16777215, 13))
        self.videoTitle.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(95, 95, 95);\n"
"margin-bottom:1px;\n"
"}")
        self.videoTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.videoTitle, 0, 0, 1, 3)

        self.urlArea = QLineEdit(self.progressbarTextArea)
        self.urlArea.setObjectName(u"urlArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlArea.sizePolicy().hasHeightForWidth())
        self.urlArea.setSizePolicy(sizePolicy)
        self.urlArea.setMinimumSize(QSize(410, 40))
        self.urlArea.setStyleSheet(u"QLineEdit{\n"
"\n"
"border-radius:  20px;\n"
"background-color:white;\n"
"	font: 10pt \"Segoe MDL2 Assets\";\n"
"color:black;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"\n"
"border:2px solid \n"
"	color: rgb(94, 226, 255);\n"
"}")
        self.urlArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.urlArea.setDragEnabled(True)
        self.urlArea.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.urlArea.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.urlArea, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(76, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.progressBar = QProgressBar(self.progressbarTextArea)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(257, 13))
        self.progressBar.setMaximumSize(QSize(261, 13))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"\n"
"height:13px;\n"
"border-style:none;\n"
"\n"
"border-radius:6px;\n"
"	background-color: rgb(24, 24, 24);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius:6px;\n"
"    background-color:rgb(94, 226, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.progressBar.setValue(84)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(76, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)


        self.gridLayout_4.addWidget(self.progressbarTextArea, 1, 1, 1, 5)

        self.horizontalSpacer_11 = QSpacerItem(136, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 2, 5, 1, 2)

        self.label_2 = QLabel(self.contentFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(250, 91))
        self.label_2.setMaximumSize(QSize(250, 91))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: rgba(161, 161, 161,00);\n"
"\n"
"}")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/assets/Logo.png"))

        self.gridLayout_4.addWidget(self.label_2, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(192, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 0, 0, 1, 3)

        self.horizontalSpacer_7 = QSpacerItem(99, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(182, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 0, 4, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(90, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 6, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(145, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 2, 0, 1, 2)

        self.frame = QFrame(self.contentFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 165))
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(26, 26, 26);\n"
"border-radius:11px;\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(20, 0, 20, -1)
        self.horizontalSpacer_5 = QSpacerItem(66, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(67, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.DownloadButton = QPushButton(self.frame)
        self.DownloadButton.setObjectName(u"DownloadButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DownloadButton.sizePolicy().hasHeightForWidth())
        self.DownloadButton.setSizePolicy(sizePolicy1)
        self.DownloadButton.setMinimumSize(QSize(139, 32))
        self.DownloadButton.setMaximumSize(QSize(156, 39))
        self.DownloadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DownloadButton.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius:11px;\n"
"	background-color: rgb(46, 46, 46);\n"
"	color: rgb(234, 234, 234);\n"
"	padding:5px;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border:1px solid rgb(76, 76, 76);\n"
"}")

        self.gridLayout_3.addWidget(self.DownloadButton, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border:0px;\n"
"background:none;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(12)
        self.downloadThumbnail = QRadioButton(self.page)
        self.downloadThumbnail.setObjectName(u"downloadThumbnail")
        self.downloadThumbnail.setMinimumSize(QSize(0, 19))
        self.downloadThumbnail.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.downloadThumbnail.setStyleSheet(u"\n"
"QRadioButton{\n"
"color: rgb(173, 173, 173);\n"
"	font: 11pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 11px;\n"
"height: 11px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 6px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 2px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 9px; \n"
"height: 9px; \n"
"}")
        self.downloadThumbnail.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.downloadThumbnail, 2, 0, 1, 1)

        self.downloadVideoBtn = QRadioButton(self.page)
        self.downloadVideoBtn.setObjectName(u"downloadVideoBtn")
        self.downloadVideoBtn.setMinimumSize(QSize(0, 19))
        self.downloadVideoBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.downloadVideoBtn.setStyleSheet(u"\n"
"QRadioButton{\n"
"color: rgb(173, 173, 173);\n"
"	font: 11pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 11px;\n"
"height: 11px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 6px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 2px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 9px; \n"
"height: 9px; \n"
"}")
        self.downloadVideoBtn.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.downloadVideoBtn, 2, 1, 1, 1)

        self.urlType = QLabel(self.page)
        self.urlType.setObjectName(u"urlType")
        self.urlType.setMinimumSize(QSize(0, 19))
        self.urlType.setStyleSheet(u"QLabel{\n"
"color: rgb(173, 173, 173);\n"
"	font: 11pt \"Segoe UI\";\n"
"}")
        self.urlType.setScaledContents(False)

        self.gridLayout_2.addWidget(self.urlType, 1, 0, 1, 1)

        self.downloadudioBtn = QRadioButton(self.page)
        self.downloadudioBtn.setObjectName(u"downloadudioBtn")
        self.downloadudioBtn.setMinimumSize(QSize(0, 19))
        self.downloadudioBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.downloadudioBtn.setStyleSheet(u"\n"
"QRadioButton{\n"
"color: rgb(173, 173, 173);\n"
"	font: 11pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 11px;\n"
"height: 11px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 6px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 2px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 9px; \n"
"height: 9px; \n"
"}")
        self.downloadudioBtn.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.downloadudioBtn, 1, 1, 1, 1)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(0, 19))
        self.label_6.setStyleSheet(u"QLabel{\n"
"color: rgb(173, 173, 173);\n"
"	font: 12pt \"Segoe UI\";\n"
"margin-bottom:5px;\n"
"}")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.backButton = QPushButton(self.page_2)
        self.backButton.setObjectName(u"backButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy3)
        self.backButton.setMinimumSize(QSize(41, 26))
        self.backButton.setStyleSheet(u"QPushButton{\n"
"padding:3px;\n"
"border-radius:5px;\n"
"	background-color: rgb(34, 34, 34);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:none;\n"
"}")

        self.gridLayout_5.addWidget(self.backButton, 1, 1, 1, 1)

        self.urlType_2 = QLabel(self.page_2)
        self.urlType_2.setObjectName(u"urlType_2")
        self.urlType_2.setMinimumSize(QSize(0, 19))
        self.urlType_2.setMaximumSize(QSize(16777215, 20))
        self.urlType_2.setStyleSheet(u"QLabel{\n"
"color: rgb(173, 173, 173);\n"
"	font: 11pt \"Segoe UI\";\n"
"	\n"
"	background-color: rgb(26, 26, 26);\n"
"}")
        self.urlType_2.setScaledContents(False)
        self.urlType_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.urlType_2, 2, 0, 1, 3)

        self.fileSize = QLabel(self.page_2)
        self.fileSize.setObjectName(u"fileSize")
        sizePolicy2.setHeightForWidth(self.fileSize.sizePolicy().hasHeightForWidth())
        self.fileSize.setSizePolicy(sizePolicy2)
        self.fileSize.setMinimumSize(QSize(0, 19))
        self.fileSize.setStyleSheet(u"QLabel{\n"
"color: rgb(173, 173, 173);\n"
"	font: 8pt \"Segoe UI\";\n"
"}")
        self.fileSize.setScaledContents(False)
        self.fileSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.fileSize, 3, 0, 1, 3)

        self.qualityDropDown = QComboBox(self.page_2)
        self.qualityDropDown.setObjectName(u"qualityDropDown")
        self.qualityDropDown.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.qualityDropDown.setStyleSheet(u"QComboBox {\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
" 	border:1px solid rgba(0,0,0,0);\n"
"		\n"
"	background-color: rgb(25, 25, 25);\n"
"color:white;\n"
"	font: 8pt \"Sans Serif Collection\";\n"
"	\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"	color:white;\n"
"border:1px solid rgb(64, 197, 49);\n"
"\n"
"}\n"
"QComboBox::hover{\n"
"border:1px solid rgb(69, 69, 69);\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"	color:white;\n"
"    border-left-width: 1px;\n"
"	\n"
"    border-left-color: white;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.qualityDropDown.setEditable(False)
        self.qualityDropDown.setFrame(False)

        self.gridLayout_5.addWidget(self.qualityDropDown, 4, 0, 1, 3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_13, 1, 2, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_5)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 3)


        self.gridLayout_4.addWidget(self.frame, 2, 2, 1, 3)


        self.verticalLayout.addWidget(self.contentFrame)

        self.label = QLabel(self.BaseFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(159, 16))
        self.label.setStyleSheet(u"QLabel{\n"
"color: rgb(77, 77, 77);\n"
"\n"
"	font: 63 8pt \"Segoe UI Semibold\";\n"
"margin-left:10px;\n"
"margin-bottom:2px;\n"
"bakground:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.BaseFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimiseButton.setText("")
        self.closeButton.setText("")
        self.videoTitle.setText(QCoreApplication.translate("MainWindow", u"Title : Video title", None))
        self.urlArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Video/Playlist link here", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_2.setText("")
        self.DownloadButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.downloadThumbnail.setText(QCoreApplication.translate("MainWindow", u"Download Thumbnail", None))
        self.downloadVideoBtn.setText(QCoreApplication.translate("MainWindow", u"Video ", None))
        self.urlType.setText(QCoreApplication.translate("MainWindow", u"Type : Video", None))
        self.downloadudioBtn.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"OPTIONS", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.urlType_2.setText(QCoreApplication.translate("MainWindow", u"Select The Quality of File", None))
        self.fileSize.setText(QCoreApplication.translate("MainWindow", u"File Size :  Mb", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"github.com/2005Kaladhar", None))
    # retranslateUi

