

# Joint Labeller
 A python script for setting joints labells inside maya software 2023+

![joint_labeller_ui](https://github.com/isNunes/JointLabeller/assets/139524834/442f50a9-99a5-4827-a614-339815f70872)


==================== W H A T  I S  I T  F O R ?  ====================

Joint Labeller is designed to facilitate the process of setting joint labels in Autodesk Maya.
Proper joint labeling is essential for functions such as skinning and mirroring weights in character rigging.
This script automates the process of labeling joints based on their names,
identifying the side (left or right) and type of each joint,
and assigning appropriate labels to be used for painting skin weights
and mirroring them across the character.

![image](https://github.com/isNunes/JointLabeller/assets/139524834/2b62d102-1dbb-4045-9a69-c63c0566f7a6)


======================= I N S T A L L =======================


1 - Copy and Paste "JointLabeller" folder into your Maya scripts directory:

	C:\...\MyDocuments\Maya\scripts\


-------------------------------------------------------------------


2 -  Use this text as a python script within Maya 2023+ script editor:

from JointLabeller.common import joint_labeller_run as label
label.run()


-------------------------------------------------------------------


3 - Create Button:

 This script can be entered from the script editor and can be made into a button.
 To do this, just click in scrip editor / file / save script to shelf,
 Search into the JointLabeller\common\ui\icon Folder and set the icon in your shelf editor.
