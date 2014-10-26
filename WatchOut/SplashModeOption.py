from WatchOut.ModeOption import ModeOption
from WatchOut.Screen import Screen
import time

class SplashModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.custom_chars = [Screen().pfc_base.LCDBitmap([1,3,7,15,30,28,24,16]),
                             Screen().pfc_base.LCDBitmap([24,16,0,0,0,0,1,3]),
                             Screen().pfc_base.LCDBitmap([0,0,0,0,1,3,7,15]),
                             Screen().pfc_base.LCDBitmap([7,15,30,28,24,16,0,0])]

    def enter(self):
        Screen.pfc.lcd.store_custom_bitmap(0, self.custom_chars[0])
        Screen.pfc.lcd.store_custom_bitmap(1, self.custom_chars[1])
        Screen.pfc.lcd.store_custom_bitmap(2, self.custom_chars[2])
        Screen.pfc.lcd.store_custom_bitmap(3, self.custom_chars[3])

        Screen.pfc.lcd.set_cursor(0,0)
        Screen.pfc.lcd.write_custom_bitmap(0)
        Screen.pfc.lcd.write_custom_bitmap(1)
        Screen.pfc.lcd.write_custom_bitmap(0)
        Screen.pfc.lcd.write_custom_bitmap(1)
        Screen.pfc.lcd.write_custom_bitmap(0)
        Screen.pfc.lcd.write_custom_bitmap(1)
        Screen.pfc.lcd.write("HACK")
        Screen.pfc.lcd.write_custom_bitmap(0)
        Screen.pfc.lcd.write_custom_bitmap(1)
        Screen.pfc.lcd.write_custom_bitmap(0)
        Screen.pfc.lcd.write_custom_bitmap(1)
        Screen.pfc.lcd.write_custom_bitmap(0)
        Screen.pfc.lcd.write_custom_bitmap(1)

        Screen.pfc.lcd.set_cursor(0,1)
        Screen.pfc.lcd.write_custom_bitmap(2)
        Screen.pfc.lcd.write_custom_bitmap(3)
        Screen.pfc.lcd.write_custom_bitmap(2)
        Screen.pfc.lcd.write("MANCHESTER")
        Screen.pfc.lcd.write_custom_bitmap(3)
        Screen.pfc.lcd.write_custom_bitmap(2)
        Screen.pfc.lcd.write_custom_bitmap(3)

        time.sleep(2)
        self.watch.switch_mode('menu')

    def exit(self):
        None