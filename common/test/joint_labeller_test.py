'''
A module for creating and managing Joint Labeller User Interface
'''

import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

from maya import cmds
import maya.OpenMayaUI as omui


class LabellerBase(object):
    def __init__(self):
        self.selection = list()

        self.joint_side = {0: 'center', 1: 'left', 2: 'right', 3: 'none'}
        self.joint_type = {'none': 0, 'root': 1, 'hip': 2, 'knee': 3,
                        'foot': 4,             'spine': 6, 'neck': 7,
                        'head': 8, 'collar': 9, 'shoulder': 10, 'elbow': 11,
                        'hand': 12,             'thumb': 14, 'propA': 15,
                        'propB': 16, 'propC': 17, 'other': 18, 'indexFinger': 19,
                        'middleFinger': 20, 'ringFinger': 21, 'pinkyFinger': 22,
                        'extraFinger': 23, 'bigToe': 24, 'indexToe': 25,
                        'middleToe': 26, 'ringToe': 27, 'pinkyToe': 28 ,
                        'footThumb': 29}


    def get_selection(self):
        '''
        A function to store all selected objects names
        '''
        selection_list = list()
        for obj in cmds.ls(selection = True):
            selection_list.append(obj)
        self.selection = selection_list
        return self.selection


    def get_children(self, maintainSelection = None):
        '''This script returns all joints below in the hierarchy from
        the selected object.

        :maintainSelection     None -> removes selection from the list 
        '''
        for node in self.get_selection():
            if maintainSelection:
                cmds.select(cmds.listRelatives(type = 'joint',
                                allDescendents = True), add = True)
            else:
                cmds.select(cmds.listRelatives(type = 'joint',
                                allDescendents = True))


    def set_labels(self):
        '''
        A function to set joint labelling accordingly to its name and side
        '''
        # Defining joint side:
        for node in self.get_selection():
            if node[0:2].lower() == 'l_':
                cmds.setAttr(node + '.side', 1)
            elif node[0:2].lower() == 'r_':
                cmds.setAttr(node + '.side', 2)
            else:
                cmds.setAttr(node + '.side', 0)
        # Defining joint type:
        for type_jnt in cmds.ls(selection = True):
            cmds.setAttr(type_jnt + '.type', 18)
            cmds.setAttr(type_jnt + '.otherType', type_jnt, type = 'string')


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