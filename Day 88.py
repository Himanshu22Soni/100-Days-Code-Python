# Solution Exercise 09 Day 83.

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

namesList = ["Himanshu Soni", "Kanika Sabharwal",
             "Shrasti Soni", "Vijay Kumar Soni"]

for name in namesList:
    speaker.Speak(f"Hello {name}")
