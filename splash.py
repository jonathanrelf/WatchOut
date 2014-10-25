import pifacecad
import time

pfc = pifacecad.PiFaceCAD()

class Splash:
    def showSplash(self):
        pfc.lcd.clear()
        pfc.lcd.write(" HACKMANCHESTER\n    WATCHOUT")
        time.sleep(2)