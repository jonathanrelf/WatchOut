__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption

class ClockModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)

    def enter(self):
        self.update_display("hello world")
        pass
    