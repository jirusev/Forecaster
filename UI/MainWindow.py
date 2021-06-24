# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowdWpLme.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(368, 513)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cmbCountry = QComboBox(self.centralwidget)
        self.cmbCountry.setObjectName(u"cmbCountry")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmbCountry)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.cmbCity = QComboBox(self.centralwidget)
        self.cmbCity.setObjectName(u"cmbCity")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cmbCity)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnLoadWeather = QPushButton(self.centralwidget)
        self.btnLoadWeather.setObjectName(u"btnLoadWeather")

        self.horizontalLayout_2.addWidget(self.btnLoadWeather)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblIcon = QLabel(self.centralwidget)
        self.lblIcon.setObjectName(u"lblIcon")
        self.lblIcon.setMaximumSize(QSize(16, 16))
        self.lblIcon.setSizeIncrement(QSize(16, 16))

        self.horizontalLayout.addWidget(self.lblIcon)

        self.lblWeather = QLabel(self.centralwidget)
        self.lblWeather.setObjectName(u"lblWeather")

        self.horizontalLayout.addWidget(self.lblWeather)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.lblWind = QLabel(self.centralwidget)
        self.lblWind.setObjectName(u"lblWind")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.lblWind.setFont(font1)
        self.lblWind.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lblWind)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lblTemp = QLabel(self.centralwidget)
        self.lblTemp.setObjectName(u"lblTemp")
        self.lblTemp.setFont(font1)
        self.lblTemp.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lblTemp)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.lblHumidity = QLabel(self.centralwidget)
        self.lblHumidity.setObjectName(u"lblHumidity")
        self.lblHumidity.setFont(font1)
        self.lblHumidity.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lblHumidity)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_17)

        self.lblPressure = QLabel(self.centralwidget)
        self.lblPressure.setObjectName(u"lblPressure")
        self.lblPressure.setFont(font1)
        self.lblPressure.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lblPressure)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.lblLongitude = QLabel(self.centralwidget)
        self.lblLongitude.setObjectName(u"lblLongitude")
        self.lblLongitude.setFont(font1)
        self.lblLongitude.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lblLongitude)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.lblLatitude = QLabel(self.centralwidget)
        self.lblLatitude.setObjectName(u"lblLatitude")
        self.lblLatitude.setFont(font1)
        self.lblLatitude.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lblLatitude)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_15)

        self.lblSunrise = QLabel(self.centralwidget)
        self.lblSunrise.setObjectName(u"lblSunrise")
        self.lblSunrise.setFont(font1)
        self.lblSunrise.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lblSunrise)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblTime2 = QLabel(self.centralwidget)
        self.lblTime2.setObjectName(u"lblTime2")
        self.lblTime2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTime2, 0, 1, 1, 1)

        self.lblTime4 = QLabel(self.centralwidget)
        self.lblTime4.setObjectName(u"lblTime4")
        self.lblTime4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTime4, 0, 3, 1, 1)

        self.lblIcon2 = QLabel(self.centralwidget)
        self.lblIcon2.setObjectName(u"lblIcon2")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIcon2.sizePolicy().hasHeightForWidth())
        self.lblIcon2.setSizePolicy(sizePolicy)
        self.lblIcon2.setMinimumSize(QSize(16, 16))
        self.lblIcon2.setMaximumSize(QSize(200, 16))
        self.lblIcon2.setBaseSize(QSize(0, 0))
        self.lblIcon2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblIcon2, 1, 1, 1, 1)

        self.lblTime5 = QLabel(self.centralwidget)
        self.lblTime5.setObjectName(u"lblTime5")
        self.lblTime5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTime5, 0, 4, 1, 1)

        self.lblTemp2 = QLabel(self.centralwidget)
        self.lblTemp2.setObjectName(u"lblTemp2")
        self.lblTemp2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTemp2, 2, 1, 1, 1)

        self.lblTemp4 = QLabel(self.centralwidget)
        self.lblTemp4.setObjectName(u"lblTemp4")
        self.lblTemp4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTemp4, 2, 3, 1, 1)

        self.lblIcon4 = QLabel(self.centralwidget)
        self.lblIcon4.setObjectName(u"lblIcon4")
        sizePolicy.setHeightForWidth(self.lblIcon4.sizePolicy().hasHeightForWidth())
        self.lblIcon4.setSizePolicy(sizePolicy)
        self.lblIcon4.setMinimumSize(QSize(16, 16))
        self.lblIcon4.setMaximumSize(QSize(200, 16))
        self.lblIcon4.setBaseSize(QSize(0, 0))
        self.lblIcon4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblIcon4, 1, 3, 1, 1)

        self.lblTemp1 = QLabel(self.centralwidget)
        self.lblTemp1.setObjectName(u"lblTemp1")
        self.lblTemp1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTemp1, 2, 0, 1, 1)

        self.lblTime1 = QLabel(self.centralwidget)
        self.lblTime1.setObjectName(u"lblTime1")
        self.lblTime1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTime1, 0, 0, 1, 1)

        self.lblTime3 = QLabel(self.centralwidget)
        self.lblTime3.setObjectName(u"lblTime3")
        self.lblTime3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTime3, 0, 2, 1, 1)

        self.lblIcon1 = QLabel(self.centralwidget)
        self.lblIcon1.setObjectName(u"lblIcon1")
        sizePolicy.setHeightForWidth(self.lblIcon1.sizePolicy().hasHeightForWidth())
        self.lblIcon1.setSizePolicy(sizePolicy)
        self.lblIcon1.setMinimumSize(QSize(16, 16))
        self.lblIcon1.setMaximumSize(QSize(200, 16))
        self.lblIcon1.setBaseSize(QSize(0, 0))
        self.lblIcon1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblIcon1, 1, 0, 1, 1)

        self.lblIcon3 = QLabel(self.centralwidget)
        self.lblIcon3.setObjectName(u"lblIcon3")
        sizePolicy.setHeightForWidth(self.lblIcon3.sizePolicy().hasHeightForWidth())
        self.lblIcon3.setSizePolicy(sizePolicy)
        self.lblIcon3.setMinimumSize(QSize(16, 16))
        self.lblIcon3.setMaximumSize(QSize(200, 16))
        self.lblIcon3.setBaseSize(QSize(0, 0))
        self.lblIcon3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblIcon3, 1, 2, 1, 1)

        self.lblIcon5 = QLabel(self.centralwidget)
        self.lblIcon5.setObjectName(u"lblIcon5")
        sizePolicy.setHeightForWidth(self.lblIcon5.sizePolicy().hasHeightForWidth())
        self.lblIcon5.setSizePolicy(sizePolicy)
        self.lblIcon5.setMinimumSize(QSize(16, 16))
        self.lblIcon5.setMaximumSize(QSize(200, 16))
        self.lblIcon5.setBaseSize(QSize(0, 0))
        self.lblIcon5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblIcon5, 1, 4, 1, 1)

        self.lblTemp3 = QLabel(self.centralwidget)
        self.lblTemp3.setObjectName(u"lblTemp3")
        self.lblTemp3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTemp3, 2, 2, 1, 1)

        self.lblTemp5 = QLabel(self.centralwidget)
        self.lblTemp5.setObjectName(u"lblTemp5")
        self.lblTemp5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTemp5, 2, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Forecaster", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Country", None))
#if QT_CONFIG(tooltip)
        self.cmbCountry.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.btnLoadWeather.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.lblIcon.setText("")
        self.lblWeather.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Wind", None))
        self.lblWind.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.lblTemp.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.lblHumidity.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.lblPressure.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lblLongitude.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.lblLatitude.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sunrise", None))
        self.lblSunrise.setText("")
        self.lblTime2.setText("")
        self.lblTime4.setText("")
        self.lblIcon2.setText("")
        self.lblTime5.setText("")
        self.lblTemp2.setText("")
        self.lblTemp4.setText("")
        self.lblIcon4.setText("")
        self.lblTemp1.setText("")
        self.lblTime1.setText("")
        self.lblTime3.setText("")
        self.lblIcon1.setText("")
        self.lblIcon3.setText("")
        self.lblIcon5.setText("")
        self.lblTemp3.setText("")
        self.lblTemp5.setText("")
    # retranslateUi









