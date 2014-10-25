__author__ = 'Jonathan'
import pifacecad
import clock

piClock = clock.Clock()
pfc = pifacecad.PiFaceCAD()

pfc.lcd.write(piClock.getTime().__str__())
