__author__ = 'Jonathan'
# Lovingly inspired by picamera
import pifacecad
from WatchOut.Watch import Watch

def option1(event):
    global watch
    watch.current_mode['option'].option1()

def option2(event):
    global watch
    watch.current_mode['option'].option2()

def option3(event):
    global watch
    watch.current_mode['option'].option3()

def option4(event):
    global watch
    watch.current_mode['option'].option4()

def switch_mode(event):
    global watch
    watch.switch_mode()

def start_watch(start_mode='clock'):
    pfc = pifacecad.PiFaceCAD()
    pfc.lcd.clear()

    switch_listener = pifacecad.SwitchEventListener(chip=pfc)
    switch_listener.register(0,pifacecad.IODIR_ON,option1)
    switch_listener.register(1,pifacecad.IODIR_ON,option2)
    switch_listener.register(2,pifacecad.IODIR_ON,option3)
    switch_listener.register(3,pifacecad.IODIR_ON,option4)
    switch_listener.register(4,pifacecad.IODIR_ON,switch_mode)

    global watch
    watch = Watch(pfc, start_mode)

    switch_listener.activate()
