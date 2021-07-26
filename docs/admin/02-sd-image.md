# Creating a League SD Image

Many times teams will not have the time to build their own image during the time allocated for an event.  It typically takes 2-4 hours to create a DonkeyCar image that is ready to drive.  To get around this problem, leagues frequently create their own "reference image" that are given to teams.

## Checklist for the League Image

1. Bookmark bar in the browser is visible (check Show Bookmarks Bar)
2. Bookmark bar is populated with:
   1. You League Homepage (use GitHub Pages and mkdocs for best pratices)
   2. Links to Team pages with sample myconfig.py files for each team's car
   3. Link to the AI Racing League site (https://www.coderdojotc.org/ai-racing-league/)
   4. Links to the DonkeyCar site
   5. Links to the Raspberry Pi or NVIDIA Nano site
3. All operating system files updates before match
4. Auto-update disabled - you don't what gigabyte uploads when people insert their image
5. All Python libraries Updates
   1. Verify Python release such as Python 3.7 using ```python --version```
   2. Run "pip freeze" to get a list of the libraries you have tested on
6. All DonkeyCar libraries updated
   1. In the "donkeycar" repo run a "git pull" to update the latest code
   2. Make sure you ONLY change the myconfig.py - changes to config.py will be lost
   
   ## Things to Remove from your Image

   1. Personal information (from your github file in .gitinfo)
   2. Change Hostname to be Generic (arl)
   3. Remove your home or school default wifi settings

## Burning an League Reference Image

1. Take the image out of your car
2. Take it to a Mac/PC and copy the image to your harddrive using the dd Command
3. Insert a black MicroSD card
4. Copy the image on your PC's Harddrive to the new MicroSD Using DD or a GUI tool like belana Etcher

## Using the GNome Partition Editor (gpartd)

[](https://gparted.org/)

## Reference

1. [DonkeyCar Release Process](https://docs.donkeycar.com/release.html)