__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
import time

class ClockModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)

    def enter(self):
        timestr = time.strftime("%H:%M:%S")
        datestr = time.strftime("%a %d-%m-%y")
        self.update_display(timestr+"\n"+datestr)
