__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
from WatchOut.Screen import Screen
import random

import pifacecad

class PiiModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        Screen.pfc.lcd.cursor_off()
        self.custom_chars = [Screen().pfc_base.LCDBitmap([0,3,7,31,31,7,3,0]),   #4 - player ship
                             Screen().pfc_base.LCDBitmap([0,8,28,14,14,28,8,0]), #5 - hostile
                             Screen().pfc_base.LCDBitmap([0,0,0,14,14,0,0,0])]   #6 - projectile
        Screen.pfc.lcd.store_custom_bitmap(4, self.custom_chars[0])
        Screen.pfc.lcd.store_custom_bitmap(5, self.custom_chars[1])
        Screen.pfc.lcd.store_custom_bitmap(6, self.custom_chars[2])

    def enter(self):
        Screen().clear_display()
        self.draw_player()

    def exit(self):
        pass

    def draw_player(self):
        Screen.pfc.lcd.set_cursor(15, 1)
        Screen.pfc.lcd.write_custom_bitmap(4)


        #for i in range(1,15):
        #    self.animate(i,0)

        #for i in range (15,0,-1):
        #    self.animate(i,0)

    #def animate(self,x_axis,y_axis):
    #    Screen().clear_display()
    #    Screen.pfc.lcd.set_cursor(x_axis,y_axis)
    #    Screen.pfc.lcd.write_custom_bitmap(4)
    #    Screen.pfc.lcd.write_custom_bitmap(5)


