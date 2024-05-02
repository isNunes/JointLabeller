'''
A python script for setting labels side, type and string
for joints within maya scene.
'''


import importlib

from JointLabeller.common.ui import joint_labeller_ui as jlui
importlib.reload(jlui)


if __name__ == '__main__':

    try:
        joint_labeller_ui.close() # pylint: disable=E0601
        joint_labeller_ui.deleteLater()
    except:
        pass

    joint_labeller_ui = jlui.JointLabellerUI()
    joint_labeller_ui.show()
