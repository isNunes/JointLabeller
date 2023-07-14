'''
A python script for setting joint labels
'''

from imp import reload

import JointLabeller.common.ui.joint_labeller_ui as jlui
reload(jlui)


if __name__ == '__main__':

    try:
        joint_labeller_ui.close() # pylint: disable=E0601
        joint_labeller_ui.deleteLater()
    except:
        pass

    joint_labeller_ui = jlui.JointLabellerUI()
    joint_labeller_ui.show()



""" Continue from:
How to make Get Children button works? """