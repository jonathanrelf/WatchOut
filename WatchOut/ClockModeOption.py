__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
import time

class ClockModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)

    def enter(self):

        self.clear_display()
        self.update_display(self.update_time())

    def update_time(self):
        dt_hour = time.strftime("%H")
        dt_min = time.strftime("%M")
        dt_sec = time.strftime("%S")

        dt_day = time.strftime("%a")
        dt_date = time.strftime("%d")
        dt_mon = time.strftime("%m")
        dt_year = time.strftime("%Y")

        date_time_str = dt_hour+":"+dt_min+":"+dt_sec+":\n"+dt_day+" "+dt_date+"-"+dt_mon+"-"+dt_year
        return date_time_str
