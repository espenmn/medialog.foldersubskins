
Changelog
=========

This product adds a field to folders so you can define **extra.css** you want to load for content in **that folder**. Requires medialog.subskins 4.1b3 or higher and Products.PloneSubSkins >= 4.5. You have to enable the subskinsloader viewlet by going to /@@manage-viewlets. Send a mail to espen at medialog dot no for help.
After you have installed the product, you should comment out some lines at:
http://yoursite/portal_skins/plonesubskins_scripts/get_base_properties/manage_main
if you want to use the "subskinscolor" option for folders (or the color settings etc. will have no effect but use the colors in the subskins control panel)

0.4.1
----------------------
A few typos

0.4
----------------------
Added name to adapter so it is possible to extend the folder from other products too.
Moved fields to new schemata.

0.3.5
----------------------
using browserlayer instead of install.py

0.3.3
----------------------
tried to install medialog.subskins and smartcolourwidget automatically

0.3.2
----------------------
Changed to using SmartColourWidget

0.3
----------------------
Added properties to "site" so you get a "default" setting 

0.2
----------------------
Added settings for all subskins colours and widths

0.1
----------------------
First version