import importlib
import os
import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

import JointLabeller.common.core.joint_labeller_core as core
importlib.reload(core)


def labeller_main_window():
    main_window_pointer = omui.MQtUtil.mainWindow()

    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
    else:
        return wrapInstance(
            long(main_window_pointer), # type: ignore
            QtWidgets.QWidget)


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

        root_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = '\\'.join([root_path, 'icon', 'jl_icon.svg'])
        self.setWindowIcon(QtGui.QIcon(icon_path))

        self.setWindowTitle('Joint Labeller')
        self.setMinimumWidth(250)

        self.setWindowFlags(
            self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()


    def create_widgets(self):
        self.get_all_joints_btn = QtWidgets.QPushButton(
                            'Get All Joints In The Scene')
        self.get_hierarchy_btn = QtWidgets.QPushButton(
                            'Get In The Selected Hierarchy')
        self.set_labels_btn = QtWidgets.QPushButton(
                            'Set Labels')


    def create_layouts(self):
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addWidget(self.get_all_joints_btn)
        top_layout.addWidget(self.get_hierarchy_btn)

        bottom_layout = QtWidgets.QVBoxLayout()
        bottom_layout.addWidget(self.set_labels_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)


    def create_connections(self):
        self.get_all_joints_btn.clicked.connect(self.get_in_scene)
        self.get_hierarchy_btn.clicked.connect(self.get_in_hierarchy)
        self.set_labels_btn.clicked.connect(self.set_labels)


    def get_in_scene(self):
        labeller_core = core.LabellerCore()
        labeller_core.get_all_joints_in_the_scene()


    def get_in_hierarchy(self):
        labeller_core = core.LabellerCore()
        labeller_core.get_joints_in_the_hierarchy()


    def set_labels(self):
        labeller_core = core.LabellerCore()
        labeller_core.set_labels()


if __name__ == '__main__':

    try:
        joint_labeller_ui.close() # type: ignore
        joint_labeller_ui.deleteLater() # type: ignore
    except:
        pass

    joint_labeller_ui = JointLabellerUI()
    joint_labeller_ui.show()
