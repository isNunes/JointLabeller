
![joint_labeller_ui](https://github.com/isNunes/JointLabeller/assets/139524834/442f50a9-99a5-4827-a614-339815f70872)

# Joint Labeller
 A python script for setting joints labells inside maya software 2020


# How to use it:
Inside maya 2023+ run the following python code:


import importlib
import os
import sys

file_path = r'Z:\CB_Repository\Maya\Scripts\RiggingDepartment\100 - Scripts\100 - Tools'
if file_path not in sys.path:
    sys.path.append(file_path)

from JointLabeller.common import joint_labeller as label
label.jlui.JointLabellerUI.show_ui()
