# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 559)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setStyleSheet("font-weight: bold; color: #3399ff;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ticket_title = QtGui.QLineEdit(Dialog)
        self.ticket_title.setObjectName("ticket_title")
        self.horizontalLayout_2.addWidget(self.ticket_title)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cc_layout = QtGui.QHBoxLayout()
        self.cc_layout.setContentsMargins(-1, 0, -1, -1)
        self.cc_layout.setObjectName("cc_layout")
        self.cc_label = QtGui.QLabel(Dialog)
        self.cc_label.setStyleSheet("font-weight: bold; color: #3399ff;")
        self.cc_label.setObjectName("cc_label")
        self.cc_layout.addWidget(self.cc_label)
        self.verticalLayout.addLayout(self.cc_layout)
        self.type_layout = QtGui.QHBoxLayout()
        self.type_layout.setObjectName("type_layout")
        self.type_label = QtGui.QLabel(Dialog)
        self.type_label.setStyleSheet("font-weight: bold; color: #3399ff;")
        self.type_label.setObjectName("type_label")
        self.type_layout.addWidget(self.type_label)
        self.verticalLayout.addLayout(self.type_layout)
        self.priority_layout = QtGui.QHBoxLayout()
        self.priority_layout.setObjectName("priority_layout")
        self.priority_label = QtGui.QLabel(Dialog)
        self.priority_label.setStyleSheet("font-weight: bold; color: #3399ff;")
        self.priority_label.setObjectName("priority_label")
        self.priority_layout.addWidget(self.priority_label)
        self.verticalLayout.addLayout(self.priority_layout)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setStyleSheet("font-weight: bold; color: #3399ff;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.ticket_body = QtGui.QPlainTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ticket_body.sizePolicy().hasHeightForWidth())
        self.ticket_body.setSizePolicy(sizePolicy)
        self.ticket_body.setObjectName("ticket_body")
        self.verticalLayout.addWidget(self.ticket_body)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setStyleSheet("font-weight: bold; color: #3399ff;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.error_log = QtGui.QPlainTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.error_log.sizePolicy().hasHeightForWidth())
        self.error_log.setSizePolicy(sizePolicy)
        self.error_log.setObjectName("error_log")
        self.verticalLayout.addWidget(self.error_log)
        self.lower_layout = QtGui.QHBoxLayout()
        self.lower_layout.setSpacing(5)
        self.lower_layout.setContentsMargins(-1, 0, -1, -1)
        self.lower_layout.setObjectName("lower_layout")
        self.screenshot = QtGui.QLabel(Dialog)
        self.screenshot.setMinimumSize(QtCore.QSize(70, 50))
        self.screenshot.setMaximumSize(QtCore.QSize(50, 50))
        self.screenshot.setStyleSheet("padding: 0;\n"
"border: none;\n"
"background: none;")
        self.screenshot.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshot.setObjectName("screenshot")
        self.lower_layout.addWidget(self.screenshot)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lower_layout.addItem(spacerItem)
        self.screen_grab = QtGui.QPushButton(Dialog)
        self.screen_grab.setMinimumSize(QtCore.QSize(170, 50))
        self.screen_grab.setMaximumSize(QtCore.QSize(1666, 1666))
        self.screen_grab.setObjectName("screen_grab")
        self.lower_layout.addWidget(self.screen_grab)
        self.verticalLayout.addLayout(self.lower_layout)
        self.buttons = QtGui.QDialogButtonBox(Dialog)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttons.setObjectName("buttons")
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Report a bug!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Subject:", None, QtGui.QApplication.UnicodeUTF8))
        self.cc_label.setText(QtGui.QApplication.translate("Dialog", "CC:", None, QtGui.QApplication.UnicodeUTF8))
        self.type_label.setText(QtGui.QApplication.translate("Dialog", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.priority_label.setText(QtGui.QApplication.translate("Dialog", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Error Log:", None, QtGui.QApplication.UnicodeUTF8))
        self.screen_grab.setText(QtGui.QApplication.translate("Dialog", "Take a screenshot!", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
