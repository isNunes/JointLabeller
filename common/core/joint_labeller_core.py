'''
A module for creating and managing Joint Labeller functionalities.
'''

from maya import cmds


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

        print('\n\tjoint_labeller_core module has been activated')


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
