__author__ = 'Jonathan'
from WatchOut.Screen import Screen
from WatchOut.ModeOption import ModeOption

class MenuModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)

    def enter(self):
        Screen().clear_display()
        Screen().update_display("CLK NXT NEW PII "," v   v   v   v")

    def option1(self):
        self.watch.switch_mode('clock')

    def option2(self):
        self.watch.switch_mode('nextevent')

    def option3(self):
        self.watch.switch_mode('newevent')

    def option4(self):
        self.watch.switch_mode('pii')