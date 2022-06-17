# Learning and Developing in Python

Over the past couple of months after installing a fresh copy of Slackware 15, I decided to brush up on my Python knowledge. I was immediately impressed with how far along Python has come.

As usual, it meant watching and following along to a lot of YouTube video tutorials. I even went as far as to develop a Python project to manage the many videos in my wish list:

 - it transferred content from text files saved from Samsung Notes on my Android device using a 4 line format (Prgoramming Language, Description, Youtube Link, empty line) and loaded them in to sqlite tables
 - displays a browser view for retrieving filtered lists from the database
 - opens links to YouTube vidoes in the default browser and local files in a Python video player which it switches views to
 - serves the currently viewed filtered list to http clients on a single view mode. Hence once the page is loaded by a client, the web service is stopped to allow the browser to regain interactive operation

# Learn Python in 5hrs

Nana was a good tutor to start with and her suggestion of using PyCharm has made it my preferred IDE on my Linux distro https://m.youtube.com/watch?v=t8pPdKYpowI

Here is my own adaptation of the course materials. I found her pace easy to follow and I noted something about the learning experience:

 - Watching 17 seconds of a Python tutorial could actually equate to 3 hours of web searches, testing and implementing inspired concepts.

 - A lot of tutorials of late teach you certain functions and then erase them from the working document and leave you without a reminder trail. So, I had to write code to call the functions learned in each example and contain each example as functions/methods within the working document.

  - Unfortunately, my Linux distro did not have an Excel document viewer that would open Excel files saved by Python using the examples in all the videos I watched. I had no problems viewing Excel files saved by Excel. So, I opted for only saving files in a csv format.

# Python - Complete Python Data Science Tutorial

Keith's example https://m.youtube.com/watch?v=vmEHCJofslg, was the 1st I had seen in the use of Jupyter Notebooks. I was a bit worried that I might not be able to follow along, but only found a few operational differences when working with PyCharm:

 - in PyCharm I had to issue a print statement with the Pandas dataframes
 - to keep a reminder trail of examples, I turned each example in to a function/method
 - created a while loop to enable an interactive approach to displaying each example


# Python - Data Analysis with Python for Excel Users

This was an interesting tutorial https://m.youtube.com/watch?v=WcDaZ67TVRo, but really, I am more than happy with Excel and VBA is the light at the end of the tunnel in my everyday working life. I was not much impressed by Jupyter Notebooks and preferred to follow the whole tutorial using PyCharm only. However, I still found that Frank's introduction on the workings of Jupyter Notebooks was very helpful and showed that this was not just about writing code, but also about giving it a well designed and formatted layout.

This tutorial again offered me the chance to:

 - turn each example in to a function/method
 - devise a way of using the import module function to display the code being used before displaying the results
 - learn more about how to get the desired results from a mix of lambdas and the map function
 - learn a lot on how to use the re module to make inputs more interactive

