# Python-EEL-with-JavaScript

Total Technology offer a good introduction to Python EEL and JavaScript GUIs at https://youtube.com/playlist?list=PLI8raxzYtfGxtQ6gPAp1qhs_Ethqo-O_o

Here is my own adaptation of the course materials for tutorials 1,2,4 and 5.

This may help me achieve transforming the Media Player Apps I have developed to use Python EEL to interact with a database stored on the device hosting the media files as opposed to using WebSQL or IndexedDb.

I managed to follow the course and build these GUIs using SLAX 9.11 linux ( https://www.slax.org/blog/download.php ), Python 3 and 3.5.3 with EEL and developed on both KDevelop and Idle for Python 3.5.3

When testing tutorial_4 on my Galaxy Tab with the files on the usb drive, I got permission errors with the plot image save. So I have amended the code to pass the plot as binary to the image source.

Please also note, that in Slax 9.11 I had to change Python eel's browsers.py 'chrome', chm to 'chromium', chm and on my Galaxy tab, I had to remove the exemption where no browser was found to use the default browser as the entry below.
