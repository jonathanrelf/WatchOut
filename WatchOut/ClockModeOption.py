__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
import datetime

class ClockModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)

    def enter(self):
        self.clear_display()
        self.update_display(self.update_time())

    def update_time(self):
        date_time = datetime.datetime.now()
        dtv_hour = date_time.hour.__str__()
        dtv_min = date_time.minute.__str__()
        dtv_sec = date_time.second.__str__()
        dtv_day = date_time.day.__str__()
        dtv_month = date_time.month.__str__()
        dtv_year = date_time.year.__str__()
        
        date_time_str = dtv_hour+":"+dtv_min+":"+dtv_sec+"\n"+dtv_day+"-"+dtv_month+"-"+dtv_year
        return date_time_str