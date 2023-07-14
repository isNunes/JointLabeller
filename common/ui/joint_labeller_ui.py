'''
A module for creating and managing Joint Labeller User Interface
'''

import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

from maya import cmds
import maya.OpenMayaUI as omui

import JointLabeller.common.core.joint_labeller_core as core


def labeller_main_window():
    main_window_pointer = omui.MQtUtil.mainWindow()

    if sys.version_info.major >= 3: #A workaround to pythons versions
        return wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_pointer), QtWidgets.QWidget)


class JointLabellerUI(QtWidgets.QDialog):
    def __init__(self, parent = labeller_main_window()):
        super(JointLabellerUI, self).__init__(parent)

        print('\n\tjoint_labeller_ui module has been activated')

        self.setWindowTitle('Joint Labeller')
        self.setMinimumWidth(200)

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
        button_layout = QtWidgets.QHBoxLayout() # Not using self in this new layout
        #button_layout.addStretch()
        button_layout.addWidget(self.get_children_btn)
        button_layout.addWidget(self.maintain_selected_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.set_labels_btn)
        main_layout.addLayout(button_layout)


    def create_connections(self):
        self.maintain_selected_btn.toggled.connect(self.test_checkbox)

        #self.get_children_btn.clicked.connect(self.get_children)


    def test_checkbox(self):
        activated = self.maintain_selected_btn.isChecked()

        sender = self.sender()
        if activated:
            print('{} has been activated'.format(sender.text()))
        else:
            print('{} has been disabled'.format(sender.text()))


    def show_ui(self):
        '''
        An workaround for calling the UI, since I didn't understand how the
        __name__ condition is working so far.
        '''
        try:
            joint_labeller_ui.close()
            joint_labeller_ui.deleteLater()
        except:
            pass

        joint_labeller_ui = JointLabellerUI()
        joint_labeller_ui.show()


if __name__ == '__main__':

    try:
        joint_labeller_ui.close() # pylint: disable=E0601
        joint_labeller_ui.deleteLater()
    except:
        pass

    joint_labeller_ui = JointLabellerUI()
    joint_labeller_ui.show()


'''
Continue from:
How to make Get Children button works?
'''