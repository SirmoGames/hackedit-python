# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/HackEdit/hackedit-python/data/forms/dlg_edit_breakpoints.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1030, 713)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree_breakpoints = QtWidgets.QTreeWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_breakpoints.sizePolicy().hasHeightForWidth())
        self.tree_breakpoints.setSizePolicy(sizePolicy)
        self.tree_breakpoints.setMinimumSize(QtCore.QSize(300, 0))
        self.tree_breakpoints.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tree_breakpoints.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tree_breakpoints.setObjectName("tree_breakpoints")
        self.tree_breakpoints.headerItem().setText(0, "1")
        self.tree_breakpoints.header().setVisible(False)
        self.tree_breakpoints.header().setCascadingSectionResizes(False)
        self.horizontalLayout.addWidget(self.tree_breakpoints)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.bt_remove_bp = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.bt_remove_bp.setIcon(icon)
        self.bt_remove_bp.setObjectName("bt_remove_bp")
        self.verticalLayout.addWidget(self.bt_remove_bp)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBoxProperties = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxProperties.sizePolicy().hasHeightForWidth())
        self.groupBoxProperties.setSizePolicy(sizePolicy)
        self.groupBoxProperties.setCheckable(False)
        self.groupBoxProperties.setObjectName("groupBoxProperties")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxProperties)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cb_enabled = QtWidgets.QCheckBox(self.groupBoxProperties)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_enabled.sizePolicy().hasHeightForWidth())
        self.cb_enabled.setSizePolicy(sizePolicy)
        self.cb_enabled.setObjectName("cb_enabled")
        self.verticalLayout_3.addWidget(self.cb_enabled)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBoxProperties)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.edit_condition = QtWidgets.QLineEdit(self.groupBoxProperties)
        self.edit_condition.setMinimumSize(QtCore.QSize(250, 0))
        self.edit_condition.setObjectName("edit_condition")
        self.horizontalLayout_3.addWidget(self.edit_condition)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.cb_suspend = QtWidgets.QCheckBox(self.groupBoxProperties)
        self.cb_suspend.setObjectName("cb_suspend")
        self.verticalLayout_3.addWidget(self.cb_suspend)
        self.cb_log_msg = QtWidgets.QCheckBox(self.groupBoxProperties)
        self.cb_log_msg.setObjectName("cb_log_msg")
        self.verticalLayout_3.addWidget(self.cb_log_msg)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cb_log_exp = QtWidgets.QCheckBox(self.groupBoxProperties)
        self.cb_log_exp.setObjectName("cb_log_exp")
        self.horizontalLayout_4.addWidget(self.cb_log_exp)
        self.edit_log_exp = QtWidgets.QLineEdit(self.groupBoxProperties)
        self.edit_log_exp.setObjectName("edit_log_exp")
        self.horizontalLayout_4.addWidget(self.edit_log_exp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.editor = DisplayEditor(self.groupBoxProperties)
        self.editor.setReadOnly(True)
        self.editor.setObjectName("editor")
        self.verticalLayout_3.addWidget(self.editor)
        self.horizontalLayout_2.addWidget(self.groupBoxProperties)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        from hackedit.api.gettext import translation
        _ = translation(package="hackedit-python")
        Dialog.setWindowTitle(_("Edit breakpoints"))
        self.groupBox.setTitle(_("Breakpoints"))
        self.bt_remove_bp.setText(_("..."))
        self.groupBoxProperties.setTitle(_("Properties"))
        self.cb_enabled.setText(_("Enabled"))
        self.label_2.setText(_("Condition:"))
        self.cb_suspend.setToolTip(_("True to suspend program when the debugger hits the breakpoint. False to continue."))
        self.cb_suspend.setText(_("Suspend"))
        self.cb_log_msg.setText(_("Log message to console"))
        self.cb_log_exp.setText(_("Log evaluated expression:"))

from hackedit_python.editor import DisplayEditor
from . import hackedit_python_rc
