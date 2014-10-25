__author__ = 'Jonathan'
import pifacecad
import clock
import splash
import threading

pfc = pifacecad.PiFaceCAD()
piClock = clock.Clock()
piSplash = splash.Splash

pfc.lcd.clear()
pfc.lcd.blink_off()
pfc.lcd.cursor_off()

def showClock(event):
    piClock.showClock()

def showClock():
    piClock.showClock()

listener = pifacecad.SwitchEventListener(chip=pfc)
listener.register(0, pifacecad.IODIR_ON, showClock)
listener.activate()

showClock()

#global shouldExit
#shouldExit = threading.Barrier(2)
#listener.activate()
#shouldExit.wait()
#listener.deactivate()