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

def option4off(event):
    global watch
    watch.current_mode['option'].option4()

def option5(event):
    global watch
    watch.current_mode['option'].option5()

def option6(event):
    global watch
    watch.current_mode['option'].option6()

def option7(event):
    global watch
    watch.current_mode['option'].option7()

def show_menu(event):
    global watch
    watch.show_menu()

def start_watch(start_mode='splash'):
    pfc = pifacecad.PiFaceCAD()
    pfc.lcd.clear()

    pfc.lcd.blink_off()
    pfc.lcd.cursor_off()

    switch_listener = pifacecad.SwitchEventListener(chip=pfc)
    switch_listener.register(0,pifacecad.IODIR_ON,option1)
    switch_listener.register(1,pifacecad.IODIR_ON,option2)
    switch_listener.register(2,pifacecad.IODIR_ON,option3)
    switch_listener.register(3,pifacecad.IODIR_ON,option4)
    switch_listener.register(4,pifacecad.IODIR_ON,show_menu)
    switch_listener.register(5,pifacecad.IODIR_ON,option5)
    switch_listener.register(6,pifacecad.IODIR_ON,option6)
    switch_listener.register(7,pifacecad.IODIR_ON,option7)

    global watch
    watch = Watch(pfc, start_mode)

    switch_listener.activate()
