# viberwrapper-indicator
Wrapper Indicator for Viber Icon for Ubuntu 14.04

Hides the top left Viber icon and adds a unity indicator that provides the same functionalities of the original icon.

# Prerequisites
- Appindicator for python: sudo apt-get install python-appindicator
- Xlib for python: sudo apt-get install python-xlib

# Installation
- Put 'viberwrapper-indicator.py' somewhere in a location of your liking
- Merge the 'icon' folder with the one in /usr/share/icons
- Update icon cache:
    - sudo gtk-update-icon-cache /usr/share/icons/ubuntu-mono-dark/
    - sudo gtk-update-icon-cache /usr/share/icons/ubuntu-mono-light/
    - sudo gtk-update-icon-cache /usr/share/icons/ubuntu-mono-hicolor/
