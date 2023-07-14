'''
Joint Labeller v0.20230713
'''

from maya import cmds

""" 
Listing all interesting joints labells:

side_jnt_dic = {0: 'center', 1: 'left', 2: 'right', 3: 'none'}

type_jnt_dic = {'none': 0, 'root': 1, 'hip': 2, 'knee': 3,
                'foot': 4,             'spine': 6, 'neck': 7,
                'head': 8, 'collar': 9, 'shoulder': 10, 'elbow': 11,
                'hand': 12,             'thumb': 14, 'propA': 15,
                'propB': 16, 'propC': 17, 'other': 18, 'indexFinger': 19,
                'middleFinger': 20, 'ringFinger': 21, 'pinkyFinger': 22,
                'extraFinger': 23, 'bigToe': 24, 'indexToe': 25,
                'middleToe': 26, 'ringToe': 27, 'pinkyToe': 28 ,
                'footThumb': 29}
"""

def joint_labeller():
    joint_list = cmds.ls(selection = True)
    
    # Defining joint side
    for side_jnt in joint_list:
        try:
            if side_jnt[0:2] == 'l_':
                cmds.setAttr(side_jnt + '.side', 1)
            elif side_jnt[0:2] == 'r_':
                cmds.setAttr(side_jnt + '.side', 2)
            else:
                cmds.setAttr(side_jnt + '.side', 0)
        except:
            pass

    # Defining joint type:
    for type_jnt in joint_list:
        try:
            if 'root' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 1)
            elif 'hip' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 2)
            elif 'knee' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 3)
            elif 'foot' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 4)
            elif 'spine' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 6)
            elif 'neck' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 7)
            elif 'head' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 8)
            elif 'shoulder' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 10)
            elif 'elbow' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 11)
            elif 'wrist' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 12)
            elif 'thumb' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 14)
            elif 'indexFinger' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 19)
            elif 'middleFinger' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 20)
            elif 'ringFinger' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 21)
            elif 'pinkyFinger' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 22)
            elif 'bigToe' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 24)
            elif 'indexToe' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 25)
            elif 'middleToe' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 26)
            elif 'ringToe' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 27)
            elif 'pinkyToe' in type_jnt:
                cmds.setAttr(type_jnt + '.type', 28)
            else: # other
                label = type_jnt.lower()
                cmds.setAttr(type_jnt + '.type', 18)
                cmds.setAttr(type_jnt + '.otherType', label, type = 'string')
        except:
            pass

joint_labeller()