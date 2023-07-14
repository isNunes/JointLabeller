'''
A python script for setting joint labels

How to import:
import sys
file_path = r'C:\Users\israel.nunes\OneDrive\PRO\Dev\Maya\100 - Tools'
if file_path not in sys.path:
    sys.path.append(file_path)

import JointLabeller.common.joint_labeller as label
reload(label)

label.jlui.JointLabellerUI.show_ui()

TO-DO:
Preparing this to drag'n drop python file and
python fyle as exe
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
