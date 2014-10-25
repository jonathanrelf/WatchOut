import pifacecad
import time

pfc = pifacecad.PiFaceCAD()

class Clock:
        def getTime(self):
            return time.strftime("%H:%M:%S")
        def getDate(self):
            return time.strftime("%d-%m-%Y")
        def showClock(self):
            pfc.lcd.clear()
            pfc.lcd.write("     CLOCK")
            time.sleep(1)
            pfc.lcd.clear()
            pfc.lcd.set_cursor(0,0)
            pfc.lcd.write(self.getTime()+"\n"+"      "+self.getDate())