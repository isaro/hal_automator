# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/config_widget.ui'
#
# Created: Wed Dec  4 11:56:01 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigForm(object):
    def setupUi(self, ConfigForm):
        ConfigForm.setObjectName("ConfigForm")
        ConfigForm.resize(1022, 642)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigForm.sizePolicy().hasHeightForWidth())
        ConfigForm.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(ConfigForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_name = QtGui.QLineEdit(ConfigForm)
        self.txt_name.setObjectName("txt_name")
        self.horizontalLayout.addWidget(self.txt_name)
        self.btn_save = QtGui.QPushButton(ConfigForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(ConfigForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabs_vars = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_vars.sizePolicy().hasHeightForWidth())
        self.tabs_vars.setSizePolicy(sizePolicy)
        self.tabs_vars.setBaseSize(QtCore.QSize(200, 0))
        self.tabs_vars.setObjectName("tabs_vars")
        self.tab_variables = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_variables.sizePolicy().hasHeightForWidth())
        self.tab_variables.setSizePolicy(sizePolicy)
        self.tab_variables.setObjectName("tab_variables")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_variables)
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lt_variables = QtGui.QVBoxLayout()
        self.lt_variables.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.lt_variables.setObjectName("lt_variables")
        self.verticalLayout_4.addLayout(self.lt_variables)
        self.tabs_vars.addTab(self.tab_variables, "")
        self.tab_resources = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_resources.sizePolicy().hasHeightForWidth())
        self.tab_resources.setSizePolicy(sizePolicy)
        self.tab_resources.setObjectName("tab_resources")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_resources)
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lt_resources = QtGui.QVBoxLayout()
        self.lt_resources.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.lt_resources.setObjectName("lt_resources")
        self.verticalLayout_6.addLayout(self.lt_resources)
        self.tabs_vars.addTab(self.tab_resources, "")
        self.tlbx_bundles = QtGui.QToolBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tlbx_bundles.sizePolicy().hasHeightForWidth())
        self.tlbx_bundles.setSizePolicy(sizePolicy)
        self.tlbx_bundles.setBaseSize(QtCore.QSize(0, 0))
        self.tlbx_bundles.setObjectName("tlbx_bundles")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 309, 530))
        self.page.setObjectName("page")
        self.tlbx_bundles.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 309, 530))
        self.page_2.setObjectName("page_2")
        self.tlbx_bundles.addItem(self.page_2, "")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(ConfigForm)
        self.tabs_vars.setCurrentIndex(0)
        self.tlbx_bundles.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConfigForm)

    def retranslateUi(self, ConfigForm):
        ConfigForm.setWindowTitle(QtGui.QApplication.translate("ConfigForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save.setText(QtGui.QApplication.translate("ConfigForm", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabText(self.tabs_vars.indexOf(self.tab_variables), QtGui.QApplication.translate("ConfigForm", "Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabToolTip(self.tabs_vars.indexOf(self.tab_variables), QtGui.QApplication.translate("ConfigForm", "List of available variables", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabText(self.tabs_vars.indexOf(self.tab_resources), QtGui.QApplication.translate("ConfigForm", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabToolTip(self.tabs_vars.indexOf(self.tab_resources), QtGui.QApplication.translate("ConfigForm", "List of available resources", None, QtGui.QApplication.UnicodeUTF8))
        self.tlbx_bundles.setItemText(self.tlbx_bundles.indexOf(self.page), QtGui.QApplication.translate("ConfigForm", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tlbx_bundles.setItemText(self.tlbx_bundles.indexOf(self.page_2), QtGui.QApplication.translate("ConfigForm", "Page 2", None, QtGui.QApplication.UnicodeUTF8))

