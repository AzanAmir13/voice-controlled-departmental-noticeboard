import pyttsx3
from functions import * 
# Imports {
    # sys 
    # textToSpeech {speech_recognition as sr}
    # BOOT {os, pandas as pd, PasswordGenerator}
    # BootMails {SendMails}
    # OpenFile
# }
if os.path.exists(os.getcwd(), "LOCAL"):
    Boot()
else:
    Bool = input("Do you want to reboot the system (Y/N): ").lower()
    if Bool == "y":
        Boot()
# Boot()


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def Start():
    engine.say("Waiting for you command!")
    engine.runAndWait()
    text = speak(engine)
    # text = "scan"
    print(text)
    Command(engine, text)
    
if __name__ == '__main__':
    while True:
        c = input("Enter space to start or any other character to exit: ")
        if c == " ":
            Start()
        else:
            exit()
