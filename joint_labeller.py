'''
A python script to set joints labelling accordingly to its side and name
'''


from maya import cmds


def joint_labeller():
    #Listing all interesting joints labells:
    joint_region_dic = {0: 'center', 1: 'left', 2: 'right', 3: 'none'}

    type_joint_dic = {'none': 0, 'root': 1, 'hip': 2, 'knee': 3,
                    'foot': 4,             'spine': 6, 'neck': 7,
                    'head': 8, 'collar': 9, 'shoulder': 10, 'elbow': 11,
                    'hand': 12,             'thumb': 14, 'propA': 15,
                    'propB': 16, 'propC': 17, 'other': 18, 'indexFinger': 19,
                    'middleFinger': 20, 'ringFinger': 21, 'pinkyFinger': 22,
                    'extraFinger': 23, 'bigToe': 24, 'indexToe': 25,
                    'middleToe': 26, 'ringToe': 27, 'pinkyToe': 28 ,
                    'footThumb': 29}

    # Defining joint side
    for selected_joint in cmds.ls(selection = True):
        try:
            if selected_joint[0:2].lower() == 'l_':
                cmds.setAttr(selected_joint + '.side', 1)
            elif selected_joint[0:2].lower() == 'r_':
                cmds.setAttr(selected_joint + '.side', 2)
            else:
                cmds.setAttr(selected_joint + '.side', 0)
        except:
            pass

    # Defining joint type:
    for type_jnt in cmds.ls(selection = True):
        cmds.setAttr(type_jnt + '.type', 18)
        cmds.setAttr(type_jnt + '.otherType', type_jnt, type = 'string')


joint_labeller()
