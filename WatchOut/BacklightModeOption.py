from WatchOut.ModeOption import ModeOption
from WatchOut.Screen import Screen

class BacklightModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.active = False

    def enter(self):
        print("ENTERED BACKLIGHT")
        if self.active == False:
            Screen.pfc.lcd.backlight_on()
            self.active = True
        else:
            Screen.pfc.lcd.backlight_off()
            self.active = False
        print(self.active)