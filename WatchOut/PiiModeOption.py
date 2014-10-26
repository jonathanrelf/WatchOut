__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
from WatchOut.Screen import Screen

import pifacecad



class PiiModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.custom_chars = [Screen().pfc_base.LCDBitmap([31,31,31,31,31,31,31,31]),
                             Screen().pfc_base.LCDBitmap([0,0,0,0,0,0,0,0])]
        Screen.pfc.lcd.store_custom_bitmap(4, self.custom_chars[0])
        Screen.pfc.lcd.store_custom_bitmap(5, self.custom_chars[1])

    def enter(self):
        Screen().clear_display()
        for i in range(1,15):
            self.animate(i,0)

        for i in range (15,0,-1):
            self.animate(i,0)

    def animate(self,x_axis,y_axis):
        Screen().clear_display()
        Screen.pfc.lcd.set_cursor(x_axis,y_axis)
        Screen.pfc.lcd.write_custom_bitmap(4)
        Screen.pfc.lcd.write_custom_bitmap(5)


