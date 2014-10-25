import pifacecad
import time

class Clock:
        def getTime(self):
            return time.strftime("%H:%M:%S")
        def getDate(self):
            return time.strftime("%d-%m-%Y")

