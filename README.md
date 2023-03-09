# Raspberry Pi Project
## Bus Alarm Project
### Student Number - 2692684

#### Introduction
The motivation for this project was my recent reliance on busses for commuting in the city of Dublin. I find myself having to check real time bus information apps every morning for my bus and it's very time consuming and redundant from day to day so I decided I wanted to automate it in a way that was convenient and fun for me.
The idea for this project was to make a Raspberry Pi scrape off information from the real time Dublin Bus website. Using that information to alarm me for when the bus is nearing my stop through different email messages and rings depending on how far away the bus is.

### SAFETY!
NOTE: There were no safety concerns for this project other than the possibility of giving away email information if not careful with github upload.

### Physical - Construction
The Raspberry Pi is a micro-computer than runs an operating system known as Raspbian (which is a Linux distro).
It was necessary to flash the SD card with Raspbian and save the wi-fi login details to the boot drive as the system would be headless.
It was rather difficult to get the pi connected to the wi-fi network but once connected it was possible to connect to the pi via the terminal.
From here the code could be uploaded and with the use of RC Local the code was set to run every time on boot.
The Pi also has a "hat" which sits on the GPIO pins and could be used as a relay switch.
A light-build socket was wired up to the replay switch and usb powered speaker was connected to the 3.5 mm audio jack with the pi's usb port powering the speaker.

### Virtual - The Code
The program utilized several functions in packages to achieve the task of sending different emails and playing different sounds as the bus approaches the desired stop. It starts with the time package which contains several functions that return the values of the current time +10,8,5 and 2 minutes which are the different times used for the alarms. The next package takes those times and checks if they're on the real time bus information webpage. Then, that information is used in the pysounds and mailer packages to play and send the appropriate sound and email respectively. Finally, the project is ran on main, constantly checking the website every minute for new information.


### Ideas for Version 2
There are several ways to improve upon the functionality of the program. The first of those would be to make the program ask the user for the link to their specific stop and tailoring the project to the user without them having to change the code. This will make the program more accessible and practical for the average user. Moreover, additional luxury features could be added to make the project more visually stimulating. This could come in the form of a connected light bulb flashing a certain number of times or different colours indicating different distances.


### Conclusion
To conclude, the program sends out emails and plays different sounds as the bus is approaching the designated stop as intended. If it's possible to leave the raspberry pi on in the mornings running the program, it is of use. However, there exists an unfixable problem with such a program and that is its reliance on accurate data from the real time Dublin bus website. Since such data is unreliable, this program would be better utilized elsewhere. Such as for something with set and reliable data like that of a train stop. The inital time to complete the program was long but editing it for different stops and uses is effortless and practical. All in all, the project was a success with just a few areas of improvement.