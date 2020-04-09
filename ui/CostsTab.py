# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CostsTab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_costs_tab(object):
    def setupUi(self, costs_tab):
        costs_tab.setObjectName("costs_tab")
        costs_tab.resize(898, 671)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/resources/tab_icons/costs_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        costs_tab.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(costs_tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(costs_tab)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.costs_parameters_frame = QtWidgets.QFrame(self.frame)
        self.costs_parameters_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.costs_parameters_frame.setObjectName("costs_parameters_frame")
        self.formLayout_3 = QtWidgets.QFormLayout(self.costs_parameters_frame)
        self.formLayout_3.setObjectName("formLayout_3")
        self.costs_report_parameter_label = QtWidgets.QLabel(self.costs_parameters_frame)
        self.costs_report_parameter_label.setObjectName("costs_report_parameter_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.costs_report_parameter_label)
        self.costs_report_parameter_combobox = QtWidgets.QComboBox(self.costs_parameters_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costs_report_parameter_combobox.sizePolicy().hasHeightForWidth())
        self.costs_report_parameter_combobox.setSizePolicy(sizePolicy)
        self.costs_report_parameter_combobox.setMinimumSize(QtCore.QSize(300, 0))
        self.costs_report_parameter_combobox.setObjectName("costs_report_parameter_combobox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.costs_report_parameter_combobox)
        self.costs_vendor_parameter_label = QtWidgets.QLabel(self.costs_parameters_frame)
        self.costs_vendor_parameter_label.setObjectName("costs_vendor_parameter_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.costs_vendor_parameter_label)
        self.costs_vendor_parameter_combobox = QtWidgets.QComboBox(self.costs_parameters_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costs_vendor_parameter_combobox.sizePolicy().hasHeightForWidth())
        self.costs_vendor_parameter_combobox.setSizePolicy(sizePolicy)
        self.costs_vendor_parameter_combobox.setMinimumSize(QtCore.QSize(300, 0))
        self.costs_vendor_parameter_combobox.setEditable(False)
        self.costs_vendor_parameter_combobox.setObjectName("costs_vendor_parameter_combobox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.costs_vendor_parameter_combobox)
        self.costs_year_parameter_label = QtWidgets.QLabel(self.costs_parameters_frame)
        self.costs_year_parameter_label.setObjectName("costs_year_parameter_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.costs_year_parameter_label)
        self.costs_year_parameter_dateedit = QtWidgets.QDateEdit(self.costs_parameters_frame)
        self.costs_year_parameter_dateedit.setObjectName("costs_year_parameter_dateedit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.costs_year_parameter_dateedit)
        self.costs_name_parameter_label = QtWidgets.QLabel(self.costs_parameters_frame)
        self.costs_name_parameter_label.setObjectName("costs_name_parameter_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.costs_name_parameter_label)
        self.costs_name_parameter_combobox = QtWidgets.QComboBox(self.costs_parameters_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costs_name_parameter_combobox.sizePolicy().hasHeightForWidth())
        self.costs_name_parameter_combobox.setSizePolicy(sizePolicy)
        self.costs_name_parameter_combobox.setMinimumSize(QtCore.QSize(300, 0))
        self.costs_name_parameter_combobox.setEditable(True)
        self.costs_name_parameter_combobox.setObjectName("costs_name_parameter_combobox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.costs_name_parameter_combobox)
        self.verticalLayout_2.addWidget(self.costs_parameters_frame)
        self.costs_values_frame = QtWidgets.QFrame(self.frame)
        self.costs_values_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.costs_values_frame.setObjectName("costs_values_frame")
        self.formLayout = QtWidgets.QFormLayout(self.costs_values_frame)
        self.formLayout.setObjectName("formLayout")
        self.costs_cost_in_original_currency_label = QtWidgets.QLabel(self.costs_values_frame)
        self.costs_cost_in_original_currency_label.setObjectName("costs_cost_in_original_currency_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.costs_cost_in_original_currency_label)
        self.costs_cost_in_original_currency_doublespinbox = QtWidgets.QDoubleSpinBox(self.costs_values_frame)
        self.costs_cost_in_original_currency_doublespinbox.setEnabled(False)
        self.costs_cost_in_original_currency_doublespinbox.setMaximum(999999999.99)
        self.costs_cost_in_original_currency_doublespinbox.setObjectName("costs_cost_in_original_currency_doublespinbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.costs_cost_in_original_currency_doublespinbox)
        self.costs_original_currency_label = QtWidgets.QLabel(self.costs_values_frame)
        self.costs_original_currency_label.setObjectName("costs_original_currency_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.costs_original_currency_label)
        self.costs_original_currency_value_combobox = QtWidgets.QComboBox(self.costs_values_frame)
        self.costs_original_currency_value_combobox.setEnabled(False)
        self.costs_original_currency_value_combobox.setEditable(True)
        self.costs_original_currency_value_combobox.setObjectName("costs_original_currency_value_combobox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.costs_original_currency_value_combobox)
        self.costs_cost_in_local_currency_label = QtWidgets.QLabel(self.costs_values_frame)
        self.costs_cost_in_local_currency_label.setObjectName("costs_cost_in_local_currency_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.costs_cost_in_local_currency_label)
        self.costs_cost_in_local_currency_doublespinbox = QtWidgets.QDoubleSpinBox(self.costs_values_frame)
        self.costs_cost_in_local_currency_doublespinbox.setEnabled(False)
        self.costs_cost_in_local_currency_doublespinbox.setMaximum(999999999.99)
        self.costs_cost_in_local_currency_doublespinbox.setObjectName("costs_cost_in_local_currency_doublespinbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.costs_cost_in_local_currency_doublespinbox)
        self.costs_cost_in_local_currency_with_tax_label = QtWidgets.QLabel(self.costs_values_frame)
        self.costs_cost_in_local_currency_with_tax_label.setObjectName("costs_cost_in_local_currency_with_tax_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.costs_cost_in_local_currency_with_tax_label)
        self.costs_cost_in_local_currency_with_tax_doublespinbox = QtWidgets.QDoubleSpinBox(self.costs_values_frame)
        self.costs_cost_in_local_currency_with_tax_doublespinbox.setEnabled(False)
        self.costs_cost_in_local_currency_with_tax_doublespinbox.setMaximum(999999999.99)
        self.costs_cost_in_local_currency_with_tax_doublespinbox.setObjectName("costs_cost_in_local_currency_with_tax_doublespinbox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.costs_cost_in_local_currency_with_tax_doublespinbox)
        self.verticalLayout_2.addWidget(self.costs_values_frame)
        self.costs_control_frame = QtWidgets.QFrame(self.frame)
        self.costs_control_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.costs_control_frame.setObjectName("costs_control_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.costs_control_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.costs_save_button = QtWidgets.QPushButton(self.costs_control_frame)
        self.costs_save_button.setObjectName("costs_save_button")
        self.gridLayout.addWidget(self.costs_save_button, 0, 0, 1, 1)
        self.costs_clear_button = QtWidgets.QPushButton(self.costs_control_frame)
        self.costs_clear_button.setObjectName("costs_clear_button")
        self.gridLayout.addWidget(self.costs_clear_button, 0, 2, 1, 1)
        self.costs_load_button = QtWidgets.QPushButton(self.costs_control_frame)
        self.costs_load_button.setObjectName("costs_load_button")
        self.gridLayout.addWidget(self.costs_load_button, 0, 4, 1, 1)
        self.costs_import_costs_button = QtWidgets.QPushButton(self.costs_control_frame)
        self.costs_import_costs_button.setObjectName("costs_import_costs_button")
        self.gridLayout.addWidget(self.costs_import_costs_button, 0, 5, 1, 1)
        self.verticalLayout_2.addWidget(self.costs_control_frame)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(costs_tab)
        QtCore.QMetaObject.connectSlotsByName(costs_tab)

    def retranslateUi(self, costs_tab):
        _translate = QtCore.QCoreApplication.translate
        costs_tab.setWindowTitle(_translate("costs_tab", "Costs"))
        self.costs_report_parameter_label.setText(_translate("costs_tab", "Report"))
        self.costs_vendor_parameter_label.setText(_translate("costs_tab", "Vendor"))
        self.costs_year_parameter_label.setText(_translate("costs_tab", "Year"))
        self.costs_year_parameter_dateedit.setDisplayFormat(_translate("costs_tab", "yyyy"))
        self.costs_name_parameter_label.setText(_translate("costs_tab", "Name"))
        self.costs_cost_in_original_currency_label.setText(_translate("costs_tab", "Cost in Original Currency"))
        self.costs_original_currency_label.setText(_translate("costs_tab", "Original Currency"))
        self.costs_cost_in_local_currency_label.setText(_translate("costs_tab", "Cost in Local Currency"))
        self.costs_cost_in_local_currency_with_tax_label.setText(_translate("costs_tab", "Cost in Local Currency with Tax"))
        self.costs_save_button.setText(_translate("costs_tab", "Save Costs"))
        self.costs_clear_button.setText(_translate("costs_tab", "Clear"))
        self.costs_load_button.setText(_translate("costs_tab", "Edit"))
        self.costs_import_costs_button.setText(_translate("costs_tab", "Import Costs File"))
import Resources_rc
