# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportReportTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_import_report_tab(object):
    def setupUi(self, import_report_tab):
        import_report_tab.setObjectName("import_report_tab")
        import_report_tab.resize(786, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/resources/tab_icons/import_report_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        import_report_tab.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(import_report_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_21 = QtWidgets.QFrame(import_report_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_18 = QtWidgets.QLabel(self.frame_21)
        self.label_18.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 1)
        self.vendor_combo_box = QtWidgets.QComboBox(self.frame_21)
        self.vendor_combo_box.setObjectName("vendor_combo_box")
        self.gridLayout.addWidget(self.vendor_combo_box, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_21)
        self.label_19.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 1, 1, 1)
        self.report_year_date_edit = QtWidgets.QDateEdit(self.frame_21)
        self.report_year_date_edit.setObjectName("report_year_date_edit")
        self.gridLayout.addWidget(self.report_year_date_edit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 2, 1)
        self.verticalLayout.addWidget(self.frame_21)
        self.frame = QtWidgets.QFrame(import_report_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_2 = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_24.addWidget(self.label_2)
        self.frame_2 = QtWidgets.QFrame(self.frame_17)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 0, 1, 1, 1)
        self.frame_38 = QtWidgets.QFrame(self.frame_2)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.selected_file_edit = QtWidgets.QLineEdit(self.frame_38)
        self.selected_file_edit.setReadOnly(True)
        self.selected_file_edit.setObjectName("selected_file_edit")
        self.horizontalLayout_15.addWidget(self.selected_file_edit)
        self.select_file_button = QtWidgets.QPushButton(self.frame_38)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_file_button.sizePolicy().hasHeightForWidth())
        self.select_file_button.setSizePolicy(sizePolicy)
        self.select_file_button.setObjectName("select_file_button")
        self.horizontalLayout_15.addWidget(self.select_file_button)
        self.gridLayout_2.addWidget(self.frame_38, 1, 1, 1, 1)
        self.c5_report_type_combo_box = QtWidgets.QComboBox(self.frame_2)
        self.c5_report_type_combo_box.setObjectName("c5_report_type_combo_box")
        self.gridLayout_2.addWidget(self.c5_report_type_combo_box, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_24.addWidget(self.frame_2)
        self.frame_25 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setObjectName("frame_25")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_25)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.import_report_button_2 = QtWidgets.QPushButton(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_report_button_2.sizePolicy().hasHeightForWidth())
        self.import_report_button_2.setSizePolicy(sizePolicy)
        self.import_report_button_2.setMaximumSize(QtCore.QSize(180, 16777215))
        self.import_report_button_2.setObjectName("import_report_button_2")
        self.gridLayout_8.addWidget(self.import_report_button_2, 0, 0, 1, 1)
        self.verticalLayout_24.addWidget(self.frame_25)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_24.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frame_3 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.c4_report_type_combo_box = QtWidgets.QComboBox(self.frame_4)
        self.c4_report_type_combo_box.setObjectName("c4_report_type_combo_box")
        self.verticalLayout_2.addWidget(self.c4_report_type_combo_box)
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.c4_report_type_equiv_label = QtWidgets.QLabel(self.frame_4)
        self.c4_report_type_equiv_label.setObjectName("c4_report_type_equiv_label")
        self.verticalLayout_2.addWidget(self.c4_report_type_equiv_label)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_37 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_4.addWidget(self.label_37)
        self.c4_files_frame = QtWidgets.QFrame(self.frame_5)
        self.c4_files_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c4_files_frame.setObjectName("c4_files_frame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.c4_files_frame)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.selected_file_edit_2 = QtWidgets.QLineEdit(self.c4_files_frame)
        self.selected_file_edit_2.setReadOnly(True)
        self.selected_file_edit_2.setObjectName("selected_file_edit_2")
        self.horizontalLayout_16.addWidget(self.selected_file_edit_2)
        self.select_file_button_2 = QtWidgets.QPushButton(self.c4_files_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_file_button_2.sizePolicy().hasHeightForWidth())
        self.select_file_button_2.setSizePolicy(sizePolicy)
        self.select_file_button_2.setObjectName("select_file_button_2")
        self.horizontalLayout_16.addWidget(self.select_file_button_2)
        self.verticalLayout_4.addWidget(self.c4_files_frame)
        self.horizontalLayout_2.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_24 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.import_report_button = QtWidgets.QPushButton(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_report_button.sizePolicy().hasHeightForWidth())
        self.import_report_button.setSizePolicy(sizePolicy)
        self.import_report_button.setMaximumSize(QtCore.QSize(180, 16777215))
        self.import_report_button.setObjectName("import_report_button")
        self.gridLayout_7.addWidget(self.import_report_button, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_24)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.frame_18)
        self.verticalLayout.addWidget(self.frame)
        self.label = QtWidgets.QLabel(import_report_tab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(import_report_tab)
        QtCore.QMetaObject.connectSlotsByName(import_report_tab)
        import_report_tab.setTabOrder(self.selected_file_edit, self.import_report_button)

    def retranslateUi(self, import_report_tab):
        _translate = QtCore.QCoreApplication.translate
        import_report_tab.setWindowTitle(_translate("import_report_tab", "Import Report"))
        self.label_18.setText(_translate("import_report_tab", "Select Vendor"))
        self.label_19.setText(_translate("import_report_tab", "Report Year"))
        self.report_year_date_edit.setDisplayFormat(_translate("import_report_tab", "yyyy"))
        self.label_2.setText(_translate("import_report_tab", "COUNTER 5"))
        self.label_17.setText(_translate("import_report_tab", "Select Report Type"))
        self.label_36.setText(_translate("import_report_tab", "Target Report File"))
        self.select_file_button.setText(_translate("import_report_tab", "Select File"))
        self.import_report_button_2.setText(_translate("import_report_tab", "Import Selected Report"))
        self.label_3.setText(_translate("import_report_tab", "COUNTER 4 (Converts to COUNTER 5)"))
        self.label_20.setText(_translate("import_report_tab", "Counter 4 Report Type"))
        self.label_21.setText(_translate("import_report_tab", "Counter 5 Equivalent"))
        self.c4_report_type_equiv_label.setText(_translate("import_report_tab", "TextLabel"))
        self.label_37.setText(_translate("import_report_tab", "Target Report File(s)"))
        self.select_file_button_2.setText(_translate("import_report_tab", "Select File(s)"))
        self.import_report_button.setText(_translate("import_report_tab", "Import Selected Report"))
        self.label.setText(_translate("import_report_tab", "Note: Only yearly reports (all available data for one calender year) should be imported. Imported reports are added to the search database."))

import Resources_rc
