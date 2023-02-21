# Exercise 09 Shoutout to Everyone.

# Python program to convert
# text to speech

# import the required module from text to speech conversion
import win32com.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak


speaker = win32com.client.Dispatch("SAPI.SpVoice")

namesList = ["Himanshu Soni", "Kanika Sabharwal",
             "Shrasti Soni", "Vijay Kumar Soni"]

speaker.Speak(namesList)
