# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settings_tab(object):
    def setupUi(self, settings_tab):
        settings_tab.setObjectName("settings_tab")
        settings_tab.resize(852, 507)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/resources/tab_icons/settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settings_tab.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(settings_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(settings_tab)
        self.scrollArea.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 815, 596))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_27 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_2.addWidget(self.label_27, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.show_debug_check_box = QtWidgets.QCheckBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_debug_check_box.sizePolicy().hasHeightForWidth())
        self.show_debug_check_box.setSizePolicy(sizePolicy)
        self.show_debug_check_box.setText("")
        self.show_debug_check_box.setObjectName("show_debug_check_box")
        self.gridLayout.addWidget(self.show_debug_check_box, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_33 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_24 = QtWidgets.QLabel(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_19.addWidget(self.label_24, 0, QtCore.Qt.AlignHCenter)
        self.frame_34 = QtWidgets.QFrame(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setObjectName("frame_34")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_34)
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.other_directory_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_directory_help_button.sizePolicy().hasHeightForWidth())
        self.other_directory_help_button.setSizePolicy(sizePolicy)
        self.other_directory_help_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ui/resources/help_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.other_directory_help_button.setIcon(icon1)
        self.other_directory_help_button.setObjectName("other_directory_help_button")
        self.gridLayout_11.addWidget(self.other_directory_help_button, 1, 3, 1, 1)
        self.other_directory_button = QtWidgets.QPushButton(self.frame_34)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ui/resources/folder_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.other_directory_button.setIcon(icon2)
        self.other_directory_button.setObjectName("other_directory_button")
        self.gridLayout_11.addWidget(self.other_directory_button, 1, 2, 1, 1)
        self.request_timeout_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.request_timeout_help_button.sizePolicy().hasHeightForWidth())
        self.request_timeout_help_button.setSizePolicy(sizePolicy)
        self.request_timeout_help_button.setText("")
        self.request_timeout_help_button.setIcon(icon1)
        self.request_timeout_help_button.setObjectName("request_timeout_help_button")
        self.gridLayout_11.addWidget(self.request_timeout_help_button, 6, 2, 1, 1)
        self.concurrent_vendors_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concurrent_vendors_help_button.sizePolicy().hasHeightForWidth())
        self.concurrent_vendors_help_button.setSizePolicy(sizePolicy)
        self.concurrent_vendors_help_button.setText("")
        self.concurrent_vendors_help_button.setIcon(icon1)
        self.concurrent_vendors_help_button.setObjectName("concurrent_vendors_help_button")
        self.gridLayout_11.addWidget(self.concurrent_vendors_help_button, 7, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.frame_34)
        self.label_37.setObjectName("label_37")
        self.gridLayout_11.addWidget(self.label_37, 6, 0, 1, 1)
        self.user_agent_edit = QtWidgets.QLineEdit(self.frame_34)
        self.user_agent_edit.setObjectName("user_agent_edit")
        self.gridLayout_11.addWidget(self.user_agent_edit, 10, 1, 1, 1)
        self.other_directory_edit = QtWidgets.QLineEdit(self.frame_34)
        self.other_directory_edit.setReadOnly(True)
        self.other_directory_edit.setObjectName("other_directory_edit")
        self.gridLayout_11.addWidget(self.other_directory_edit, 1, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_34)
        self.label_32.setObjectName("label_32")
        self.gridLayout_11.addWidget(self.label_32, 8, 0, 1, 1)
        self.yearly_directory_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearly_directory_help_button.sizePolicy().hasHeightForWidth())
        self.yearly_directory_help_button.setSizePolicy(sizePolicy)
        self.yearly_directory_help_button.setText("")
        self.yearly_directory_help_button.setIcon(icon1)
        self.yearly_directory_help_button.setObjectName("yearly_directory_help_button")
        self.gridLayout_11.addWidget(self.yearly_directory_help_button, 0, 3, 1, 1)
        self.request_interval_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.request_interval_spin_box.setMaximum(999)
        self.request_interval_spin_box.setObjectName("request_interval_spin_box")
        self.gridLayout_11.addWidget(self.request_interval_spin_box, 5, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_34)
        self.label_25.setObjectName("label_25")
        self.gridLayout_11.addWidget(self.label_25, 0, 0, 1, 1)
        self.request_interval_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.request_interval_help_button.sizePolicy().hasHeightForWidth())
        self.request_interval_help_button.setSizePolicy(sizePolicy)
        self.request_interval_help_button.setText("")
        self.request_interval_help_button.setIcon(icon1)
        self.request_interval_help_button.setObjectName("request_interval_help_button")
        self.gridLayout_11.addWidget(self.request_interval_help_button, 5, 2, 1, 1)
        self.request_timeout_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.request_timeout_spin_box.setMaximum(9999)
        self.request_timeout_spin_box.setSingleStep(30)
        self.request_timeout_spin_box.setObjectName("request_timeout_spin_box")
        self.gridLayout_11.addWidget(self.request_timeout_spin_box, 6, 1, 1, 1)
        self.yearly_directory_button = QtWidgets.QPushButton(self.frame_34)
        self.yearly_directory_button.setIcon(icon2)
        self.yearly_directory_button.setObjectName("yearly_directory_button")
        self.gridLayout_11.addWidget(self.yearly_directory_button, 0, 2, 1, 1)
        self.concurrent_reports_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.concurrent_reports_spin_box.setMaximum(999)
        self.concurrent_reports_spin_box.setObjectName("concurrent_reports_spin_box")
        self.gridLayout_11.addWidget(self.concurrent_reports_spin_box, 8, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.frame_34)
        self.label_31.setObjectName("label_31")
        self.gridLayout_11.addWidget(self.label_31, 7, 0, 1, 1)
        self.yearly_directory_edit = QtWidgets.QLineEdit(self.frame_34)
        self.yearly_directory_edit.setReadOnly(True)
        self.yearly_directory_edit.setObjectName("yearly_directory_edit")
        self.gridLayout_11.addWidget(self.yearly_directory_edit, 0, 1, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.frame_34)
        self.label_73.setObjectName("label_73")
        self.gridLayout_11.addWidget(self.label_73, 10, 0, 1, 1)
        self.user_agent_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_agent_help_button.sizePolicy().hasHeightForWidth())
        self.user_agent_help_button.setSizePolicy(sizePolicy)
        self.user_agent_help_button.setText("")
        self.user_agent_help_button.setIcon(icon1)
        self.user_agent_help_button.setObjectName("user_agent_help_button")
        self.gridLayout_11.addWidget(self.user_agent_help_button, 10, 2, 1, 1)
        self.concurrent_reports_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concurrent_reports_help_button.sizePolicy().hasHeightForWidth())
        self.concurrent_reports_help_button.setSizePolicy(sizePolicy)
        self.concurrent_reports_help_button.setText("")
        self.concurrent_reports_help_button.setIcon(icon1)
        self.concurrent_reports_help_button.setObjectName("concurrent_reports_help_button")
        self.gridLayout_11.addWidget(self.concurrent_reports_help_button, 8, 2, 1, 1)
        self.concurrent_vendors_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.concurrent_vendors_spin_box.setMaximum(999)
        self.concurrent_vendors_spin_box.setObjectName("concurrent_vendors_spin_box")
        self.gridLayout_11.addWidget(self.concurrent_vendors_spin_box, 7, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_34)
        self.label_29.setObjectName("label_29")
        self.gridLayout_11.addWidget(self.label_29, 1, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame_34)
        self.label_30.setObjectName("label_30")
        self.gridLayout_11.addWidget(self.label_30, 5, 0, 1, 1)
        self.verticalLayout_19.addWidget(self.frame_34)
        self.verticalLayout.addWidget(self.frame_33)
        self.settings_costs_frame = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_costs_frame.sizePolicy().hasHeightForWidth())
        self.settings_costs_frame.setSizePolicy(sizePolicy)
        self.settings_costs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_costs_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.settings_costs_frame.setObjectName("settings_costs_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.settings_costs_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.settings_costs_label = QtWidgets.QLabel(self.settings_costs_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.settings_costs_label.setFont(font)
        self.settings_costs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_costs_label.setObjectName("settings_costs_label")
        self.verticalLayout_3.addWidget(self.settings_costs_label)
        self.settings_costs_items_frame = QtWidgets.QFrame(self.settings_costs_frame)
        self.settings_costs_items_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_costs_items_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_costs_items_frame.setObjectName("settings_costs_items_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.settings_costs_items_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.settings_costs_default_currency_label = QtWidgets.QLabel(self.settings_costs_items_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_costs_default_currency_label.sizePolicy().hasHeightForWidth())
        self.settings_costs_default_currency_label.setSizePolicy(sizePolicy)
        self.settings_costs_default_currency_label.setObjectName("settings_costs_default_currency_label")
        self.horizontalLayout_4.addWidget(self.settings_costs_default_currency_label)
        self.settings_costs_default_currency_combobox = QtWidgets.QComboBox(self.settings_costs_items_frame)
        self.settings_costs_default_currency_combobox.setEditable(True)
        self.settings_costs_default_currency_combobox.setObjectName("settings_costs_default_currency_combobox")
        self.horizontalLayout_4.addWidget(self.settings_costs_default_currency_combobox)
        self.default_currency_help_button = QtWidgets.QPushButton(self.settings_costs_items_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.default_currency_help_button.sizePolicy().hasHeightForWidth())
        self.default_currency_help_button.setSizePolicy(sizePolicy)
        self.default_currency_help_button.setText("")
        self.default_currency_help_button.setIcon(icon1)
        self.default_currency_help_button.setObjectName("default_currency_help_button")
        self.horizontalLayout_4.addWidget(self.default_currency_help_button)
        self.verticalLayout_3.addWidget(self.settings_costs_items_frame)
        self.verticalLayout.addWidget(self.settings_costs_frame)
        self.save_button = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ui/resources/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon3)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button, 0, QtCore.Qt.AlignHCenter)
        self.settings_search_frame = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_search_frame.sizePolicy().hasHeightForWidth())
        self.settings_search_frame.setSizePolicy(sizePolicy)
        self.settings_search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_search_frame.setObjectName("settings_search_frame")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.settings_search_frame)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.settings_search_label = QtWidgets.QLabel(self.settings_search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_search_label.sizePolicy().hasHeightForWidth())
        self.settings_search_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.settings_search_label.setFont(font)
        self.settings_search_label.setObjectName("settings_search_label")
        self.verticalLayout_20.addWidget(self.settings_search_label, 0, QtCore.Qt.AlignHCenter)
        self.settings_rebuild_database_button = QtWidgets.QPushButton(self.settings_search_frame)
        self.settings_rebuild_database_button.setObjectName("settings_rebuild_database_button")
        self.verticalLayout_20.addWidget(self.settings_rebuild_database_button)
        self.verticalLayout.addWidget(self.settings_search_frame)
        self.frame = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3.addWidget(self.frame_4)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(settings_tab)
        QtCore.QMetaObject.connectSlotsByName(settings_tab)

    def retranslateUi(self, settings_tab):
        _translate = QtCore.QCoreApplication.translate
        settings_tab.setWindowTitle(_translate("settings_tab", "Settings"))
        self.label_27.setText(_translate("settings_tab", "General"))
        self.label.setText(_translate("settings_tab", "Show Debug Messages in Console Window"))
        self.label_24.setText(_translate("settings_tab", "Reports"))
        self.other_directory_button.setText(_translate("settings_tab", "Choose"))
        self.label_37.setText(_translate("settings_tab", "Request Timeout"))
        self.label_32.setText(_translate("settings_tab", "Concurrent Reports"))
        self.label_25.setText(_translate("settings_tab", "Yearly Reports Directory"))
        self.yearly_directory_button.setText(_translate("settings_tab", "Choose"))
        self.label_31.setText(_translate("settings_tab", "Concurrent Vendors"))
        self.label_73.setText(_translate("settings_tab", "User Agent"))
        self.label_29.setText(_translate("settings_tab", "Other Reports Directory"))
        self.label_30.setText(_translate("settings_tab", "Report Request Interval"))
        self.settings_costs_label.setText(_translate("settings_tab", "Costs"))
        self.settings_costs_default_currency_label.setText(_translate("settings_tab", "Default Currency"))
        self.save_button.setText(_translate("settings_tab", "Save All Changes"))
        self.settings_search_label.setText(_translate("settings_tab", "Search"))
        self.settings_rebuild_database_button.setText(_translate("settings_tab", "Rebuild Database"))

import Resources_rc
