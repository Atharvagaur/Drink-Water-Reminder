# importing modules for the program
import time
import pyttsx3
from plyer import notification
speak=pyttsx3.init()
while True:
    # gives a notification on your laptop
    notification.notify(
    title = "Drink Water ",
    message="Drink water, stay hydrated" ,)
    # gives a voice message for your reminder
    speak.say(f"......Its time to Drink water, Stay hydrated")
    speak.runAndWait()
    # the time for the sleep function will be the time interval for which you need to be reminded for water
    time.sleep(3600)