'''
A module for creating and managing Joint Labeller User Interface

TODO:
How to make Get Children button works?

'''

import sys
from imp import reload

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

from maya import cmds
import maya.OpenMayaUI as omui

import JointLabeller.common.core.joint_labeller_core as core
reload(core)


def labeller_main_window():
    main_window_pointer = omui.MQtUtil.mainWindow()

    if sys.version_info.major >= 3: #A workaround to pythons versions
        return wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_pointer), QtWidgets.QWidget)


class JointLabellerUI(QtWidgets.QDialog):

    ui_instance = None

    @classmethod
    def show_ui(cls):
        if not cls.ui_instance:
            cls.ui_instance = JointLabellerUI()

        if cls.ui_instance.isHidden():
            cls.ui_instance.show()
        else:
            cls.ui_instance.raise_()
            cls.ui_instance.activateWindow()


    def __init__(self, parent = labeller_main_window()):
        super(JointLabellerUI, self).__init__(parent)

        self.setWindowTitle('Joint Labeller')
        self.setMinimumWidth(250)

        # Remove ? signal from the window bar
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()


    def create_widgets(self):
        '''
        UI elements to apply into layouts that will be parented to the dialog
        '''
        self.get_children_btn = QtWidgets.QPushButton('Get Children')
        self.maintain_selected_btn = QtWidgets.QCheckBox('Maintain Selected')
        self.set_labels_btn = QtWidgets.QPushButton('Set Labels')


    def create_layouts(self):
        top_layout = QtWidgets.QHBoxLayout() # Not using self in this new layout
        #top_layout.addStretch()
        top_layout.addWidget(self.get_children_btn)
        top_layout.addWidget(self.maintain_selected_btn)

        bottom_layout = QtWidgets.QVBoxLayout()
        bottom_layout.addWidget(self.set_labels_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)


    def create_connections(self):
        self.set_labels_btn.clicked.connect(self.set_labels)

        self.get_children_btn.clicked.connect(self.get_children)
        self.maintain_selected_btn.toggled.connect(self.test_checkbox)


    def get_children(self):
        labeller_core = core.LabellerCore()
        labeller_core.get_children()


    def set_labels(self):
        labeller_core = core.LabellerCore()
        labeller_core.set_labels()


    def test_checkbox(self):
        activated = self.maintain_selected_btn.isChecked()

        sender = self.sender()
        if activated:
            print('{} has been activated'.format(sender.text()))
        else:
            print('{} has been disabled'.format(sender.text()))


if __name__ == '__main__':

    try:
        joint_labeller_ui.close() # pylint: disable=E0601
        joint_labeller_ui.deleteLater()
    except:
        pass

    joint_labeller_ui = JointLabellerUI()
    joint_labeller_ui.show()
