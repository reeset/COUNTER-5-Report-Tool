# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FetchSpecialReportsTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fetch_special_reports_tab(object):
    def setupUi(self, fetch_special_reports_tab):
        fetch_special_reports_tab.setObjectName("fetch_special_reports_tab")
        fetch_special_reports_tab.resize(1094, 577)
        fetch_special_reports_tab.setMinimumSize(QtCore.QSize(800, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/resources/tab_icons/fetch_special_reports_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fetch_special_reports_tab.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fetch_special_reports_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(fetch_special_reports_tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_26 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_21 = QtWidgets.QLabel(self.frame_26)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_15.addWidget(self.label_21)
        self.frame_32 = QtWidgets.QFrame(self.frame_26)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.select_vendors_button_special = QtWidgets.QPushButton(self.frame_32)
        self.select_vendors_button_special.setObjectName("select_vendors_button_special")
        self.horizontalLayout_9.addWidget(self.select_vendors_button_special)
        self.deselect_vendors_button_special = QtWidgets.QPushButton(self.frame_32)
        self.deselect_vendors_button_special.setObjectName("deselect_vendors_button_special")
        self.horizontalLayout_9.addWidget(self.deselect_vendors_button_special)
        self.verticalLayout_15.addWidget(self.frame_32)
        self.vendors_list_view_special = QtWidgets.QListView(self.frame_26)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.vendors_list_view_special.setFont(font)
        self.vendors_list_view_special.setAlternatingRowColors(True)
        self.vendors_list_view_special.setObjectName("vendors_list_view_special")
        self.verticalLayout_15.addWidget(self.vendors_list_view_special)
        self.horizontalLayout_2.addWidget(self.frame_26)
        self.frame_25 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QtCore.QSize(180, 0))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_20 = QtWidgets.QLabel(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_14.addWidget(self.label_20)
        self.frame_30 = QtWidgets.QFrame(self.frame_25)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setObjectName("frame_30")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_30)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tr_radio_button = QtWidgets.QRadioButton(self.frame_30)
        self.tr_radio_button.setObjectName("tr_radio_button")
        self.gridLayout_9.addWidget(self.tr_radio_button, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pr_radio_button = QtWidgets.QRadioButton(self.frame_30)
        self.pr_radio_button.setChecked(True)
        self.pr_radio_button.setObjectName("pr_radio_button")
        self.gridLayout_9.addWidget(self.pr_radio_button, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dr_radio_button = QtWidgets.QRadioButton(self.frame_30)
        self.dr_radio_button.setObjectName("dr_radio_button")
        self.gridLayout_9.addWidget(self.dr_radio_button, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ir_radio_button = QtWidgets.QRadioButton(self.frame_30)
        self.ir_radio_button.setObjectName("ir_radio_button")
        self.gridLayout_9.addWidget(self.ir_radio_button, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_14.addWidget(self.frame_30)
        self.horizontalLayout_2.addWidget(self.frame_25)
        self.frame_27 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_15 = QtWidgets.QFrame(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_3 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.options_help_button = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options_help_button.sizePolicy().hasHeightForWidth())
        self.options_help_button.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ui/resources/help_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.options_help_button.setIcon(icon1)
        self.options_help_button.setObjectName("options_help_button")
        self.horizontalLayout.addWidget(self.options_help_button)
        self.verticalLayout_22.addWidget(self.frame_3)
        self.options_frame = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options_frame.sizePolicy().hasHeightForWidth())
        self.options_frame.setSizePolicy(sizePolicy)
        self.options_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_frame.setObjectName("options_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.options_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_22.addWidget(self.options_frame)
        self.verticalLayout_16.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_16)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.date_range_help_button = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_range_help_button.sizePolicy().hasHeightForWidth())
        self.date_range_help_button.setSizePolicy(sizePolicy)
        self.date_range_help_button.setText("")
        self.date_range_help_button.setIcon(icon1)
        self.date_range_help_button.setObjectName("date_range_help_button")
        self.horizontalLayout_3.addWidget(self.date_range_help_button)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 1, 0, 1, 1)
        self.begin_date_edit_special_year = QtWidgets.QDateEdit(self.frame)
        self.begin_date_edit_special_year.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.begin_date_edit_special_year.setObjectName("begin_date_edit_special_year")
        self.gridLayout_2.addWidget(self.begin_date_edit_special_year, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 1)
        self.end_date_edit_special_year = QtWidgets.QDateEdit(self.frame)
        self.end_date_edit_special_year.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date_edit_special_year.setObjectName("end_date_edit_special_year")
        self.gridLayout_2.addWidget(self.end_date_edit_special_year, 1, 1, 1, 1)
        self.begin_month_combo_box = QtWidgets.QComboBox(self.frame)
        self.begin_month_combo_box.setObjectName("begin_month_combo_box")
        self.gridLayout_2.addWidget(self.begin_month_combo_box, 0, 2, 1, 1)
        self.end_month_combo_box = QtWidgets.QComboBox(self.frame)
        self.end_month_combo_box.setObjectName("end_month_combo_box")
        self.gridLayout_2.addWidget(self.end_month_combo_box, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.custom_dir_frame = QtWidgets.QFrame(self.frame_16)
        self.custom_dir_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custom_dir_frame.setObjectName("custom_dir_frame")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.custom_dir_frame)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_41 = QtWidgets.QLabel(self.custom_dir_frame)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_26.addWidget(self.label_41)
        self.frame_39 = QtWidgets.QFrame(self.custom_dir_frame)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.custom_dir_edit = QtWidgets.QLineEdit(self.frame_39)
        self.custom_dir_edit.setObjectName("custom_dir_edit")
        self.horizontalLayout_7.addWidget(self.custom_dir_edit)
        self.custom_dir_button = QtWidgets.QPushButton(self.frame_39)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_dir_button.sizePolicy().hasHeightForWidth())
        self.custom_dir_button.setSizePolicy(sizePolicy)
        self.custom_dir_button.setObjectName("custom_dir_button")
        self.horizontalLayout_7.addWidget(self.custom_dir_button)
        self.verticalLayout_26.addWidget(self.frame_39)
        self.verticalLayout.addWidget(self.custom_dir_frame)
        self.verticalLayout_16.addWidget(self.frame_16)
        self.frame_29 = QtWidgets.QFrame(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setObjectName("frame_29")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_29)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.fetch_special_data_button = QtWidgets.QPushButton(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_special_data_button.sizePolicy().hasHeightForWidth())
        self.fetch_special_data_button.setSizePolicy(sizePolicy)
        self.fetch_special_data_button.setMaximumSize(QtCore.QSize(180, 16777215))
        self.fetch_special_data_button.setObjectName("fetch_special_data_button")
        self.gridLayout_8.addWidget(self.fetch_special_data_button, 0, 0, 1, 1)
        self.verticalLayout_16.addWidget(self.frame_29)
        self.horizontalLayout_2.addWidget(self.frame_27)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.label = QtWidgets.QLabel(fetch_special_reports_tab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.retranslateUi(fetch_special_reports_tab)
        QtCore.QMetaObject.connectSlotsByName(fetch_special_reports_tab)
        fetch_special_reports_tab.setTabOrder(self.select_vendors_button_special, self.deselect_vendors_button_special)
        fetch_special_reports_tab.setTabOrder(self.deselect_vendors_button_special, self.vendors_list_view_special)
        fetch_special_reports_tab.setTabOrder(self.vendors_list_view_special, self.pr_radio_button)
        fetch_special_reports_tab.setTabOrder(self.pr_radio_button, self.dr_radio_button)
        fetch_special_reports_tab.setTabOrder(self.dr_radio_button, self.tr_radio_button)
        fetch_special_reports_tab.setTabOrder(self.tr_radio_button, self.ir_radio_button)
        fetch_special_reports_tab.setTabOrder(self.ir_radio_button, self.options_frame)
        fetch_special_reports_tab.setTabOrder(self.options_frame, self.begin_date_edit_special_year)
        fetch_special_reports_tab.setTabOrder(self.begin_date_edit_special_year, self.end_date_edit_special_year)
        fetch_special_reports_tab.setTabOrder(self.end_date_edit_special_year, self.fetch_special_data_button)

    def retranslateUi(self, fetch_special_reports_tab):
        _translate = QtCore.QCoreApplication.translate
        fetch_special_reports_tab.setWindowTitle(_translate("fetch_special_reports_tab", "Fetch Special Reports"))
        self.label_21.setText(_translate("fetch_special_reports_tab", "Select Vendors"))
        self.select_vendors_button_special.setText(_translate("fetch_special_reports_tab", "Select All"))
        self.deselect_vendors_button_special.setText(_translate("fetch_special_reports_tab", "Deselect All"))
        self.label_20.setText(_translate("fetch_special_reports_tab", "Select Report Type"))
        self.tr_radio_button.setText(_translate("fetch_special_reports_tab", "TR"))
        self.pr_radio_button.setText(_translate("fetch_special_reports_tab", "PR"))
        self.dr_radio_button.setText(_translate("fetch_special_reports_tab", "DR"))
        self.ir_radio_button.setText(_translate("fetch_special_reports_tab", "IR"))
        self.label_14.setText(_translate("fetch_special_reports_tab", "Options"))
        self.label_15.setText(_translate("fetch_special_reports_tab", "Date Range"))
        self.label_25.setText(_translate("fetch_special_reports_tab", "End Date"))
        self.begin_date_edit_special_year.setDisplayFormat(_translate("fetch_special_reports_tab", "yyyy"))
        self.label_24.setText(_translate("fetch_special_reports_tab", "Begin Date"))
        self.end_date_edit_special_year.setDisplayFormat(_translate("fetch_special_reports_tab", "yyyy"))
        self.label_41.setText(_translate("fetch_special_reports_tab", "Report(s) will be saved to:"))
        self.custom_dir_button.setText(_translate("fetch_special_reports_tab", "Change"))
        self.fetch_special_data_button.setText(_translate("fetch_special_reports_tab", "Fetch Special Report"))
        self.label.setText(_translate("fetch_special_reports_tab", "Note: Special reports are not added to the search database."))

import Resources_rc
