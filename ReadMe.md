# Learning and Developing in Python

Over the past couple of months after installing a fresh copy of Slackware 15, I decided to brush up on my Python knowledge. I was immediately impressed with how far along Python has come.

As usual, it meant watching and following along to a lot of YouTube video tutorials. I even went as far as to develop a Python project to manage the many videos in my wish list:

 - it transferred content from text files saved from Samsung Notes on my Android device using a 4 line format (Prgoramming Language, Description, Youtube Link, empty line) and loaded them in to sqlite tables
 - displays a browser view for retrieving filtered lists from the database
 - opens links to YouTube vidoes in the default browser and local files in a Python video player which it switches views to
 - serves the currently viewed filtered list to http clients on a single view mode. Hence once the page is loaded by a client, the web service is stopped to allow the browser to regain interactive operation

# IPI Galaxy Tab Text to Speech

After a few failed attempts, I decided to give it another go. Luckily I found a solution on StackOverFlow that offered saving and reading some hard coded text. Unfortunately the method of reading did not work because the App used was not recognised by the Python App on the Galaxy tablet. So I made the following changes:

 - Populated the text variable with clipboard text using PyQt5 widgets
 - Played the saved mp3 using the PyQt5 media player
 - Added Play, Pause, Resume and Quit controller buttons and actions
 - Added function to search Samsung Galaxy Tab S3 for all mp3 files and display as buttons, that when clicked plays the file. I was a bit disappointed that my Tab plays mp4s without problem from the My Files folders but not mp3s.
 - Added a Rich Text Editor as the Samsung Galaxy Tab S3 does not have a default editor other than Samsung Notes (which is quite good in fact), but this one allows you to copy and paste chunks of text in, and then copy the whole block to clipboard before using the Text to Speech function.

I will have to eventually learn how to display the form as a pop-up in the Android Tablet environment so that it does not fill the entire screen.

# Learn Python in 5hrs

Nana was a good tutor to start with and her suggestion of using PyCharm has made it my preferred IDE on my Linux distro https://m.youtube.com/watch?v=t8pPdKYpowI

Here is my own adaptation of the course materials. I found her pace easy to follow and I noted something about the learning experience:

 - Watching 17 seconds of a Python tutorial could actually equate to 3 hours of web searches, testing and implementing inspired concepts.

 - A lot of tutorials of late teach you certain functions and then erase them from the working document and leave you without a reminder trail. So, I had to write code to call the functions learned in each example and contain each example as functions/methods within the working document.

  - Unfortunately, my Linux distro did not have an Excel document viewer that would open Excel files saved by Python using the examples in all the videos I watched. I had no problems viewing Excel files saved by Excel. So, I opted for only saving files in a csv format.
  
