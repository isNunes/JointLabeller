""" A python script for setting labels side, type and string
for joints within maya scene.
"""

from importlib import reload

from JointLabeller.common.ui import joint_labeller_ui as jlui
reload(jlui)

def run():
    joint_labeller_ui = jlui.JointLabellerUI()
    joint_labeller_ui.show()