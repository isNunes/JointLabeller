"""
A module for creating and managing Joint Labeller functionalities.
"""

from maya import cmds


class LabellerCore():

    def __init__(self):
        self.joints_list = []

        self.joint_side = {
            'l':1, 'r':2,
            }
        self.joint_type = {
            'none': 0, 'root': 1, 'hip': 2, 'knee': 3,
            'foot': 4, 'toe': 5, 'spine': 6, 'neck': 7,
            'head': 8, 'collar': 9, 'shoulder': 10, 'elbow': 11,
            'hand': 12, 'finger': 13, 'thumb': 14, 'propA': 15,
            'propB': 16, 'propC': 17, 'other': 18, 'indexFinger': 19,
            'middleFinger': 20, 'ringFinger': 21, 'pinkyFinger': 22,
            'extraFinger': 23, 'bigToe': 24, 'indexToe': 25,
            'middleToe': 26, 'ringToe': 27, 'pinkyToe': 28 ,
            'footThumb': 29
            }


    ####################################################################
    # Getter methods
    ####################################################################
    def get_all_joints_in_the_scene(self):
        self.joints_list = [jnt for jnt in cmds.ls(type='joint')]

        if self.joints_list:
            cmds.select(self.joints_list)
            print('\nThe following joints have been selected:')
            for joint in self.joints_list:
                print(f'\t | {joint}')
            print('')
            return self.joints_list
        else:
            cmds.warning('Could not find any joint in the current scene.')
            return None


    def get_joints_in_the_hierarchy(self):
        all_joints = {node for node in cmds.ls(selection=True)
                    if cmds.nodeType(node) == 'joint'}

        all_joints.update(
            joint
            for node in cmds.ls(selection=True)
            for joint in cmds.listRelatives(
                node, type='joint', allDescendents=True)
                or [])
        self.joints_list = list(all_joints)

        if self.joints_list:
            cmds.select(self.joints_list)
            print('\nThe following joints have been selected:')
            for joint in self.joints_list:
                print(f'\t | {joint}')
            print('')
            return self.joints_list
        else:
            cmds.warning(
                '\nPlease select a group with joints or a joint in the scene.')
            return None


    def get_side_info(self, name):
        name_parts = name.split('_')
        side_info = [self.joint_side[part.lower()] for part in name_parts
                    if part.lower() in self.joint_side.keys()]
        return side_info[0] if side_info else 0


    def get_local_value(self, name):
        name_parts = name.split('_')

        lower_types = {key.lower(): value
            for key, value in self.joint_type.items()}

        for local in name_parts:
            local_lower = local.lower()
            if local_lower in lower_types:
                return lower_types[local_lower]
        return 18


    def get_joints_data(self):
        selection = {node for node in cmds.ls(selection=True)
            if cmds.nodeType(node) == 'joint'}
        return selection if selection else self.joints_list


    ####################################################################
    # Setter methods
    ####################################################################
    def set_labels(self):
        data = self.get_joints_data()
        if data:
            print('\nLabelling the following joints:')

            for joint in self.get_joints_data():
                side_data = self.get_side_info(joint)
                joint_type = self.get_local_value(joint)

                cmds.setAttr(f'{joint}.side', side_data)
                cmds.setAttr(f'{joint}.type', joint_type)
                cmds.setAttr(
                    f'{joint}.otherType', joint, type='string') \
                    if joint_type == 18 else None
                print(f'\t | {joint} has been succesfully labelled.')

            print(f'\n Setting complete.\n')
            return data
        else:
            cmds.warning('No joint data has been provided.')
            return None


if __name__ == '__main__':
    label = LabellerCore()
    label.get_all_joints_in_the_scene()
    label.set_labels()