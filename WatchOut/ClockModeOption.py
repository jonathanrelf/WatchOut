__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
from WatchOut.Screen import Screen
import time
import threading


def update_time():
    dt_hour = time.strftime("%H")
    dt_min = time.strftime("%M")
    dt_sec = time.strftime("%S")

    dt_day = time.strftime("%a")
    dt_date = time.strftime("%d")
    dt_mon = time.strftime("%m")
    dt_year = time.strftime("%Y")

    date_time_str = dt_hour+":"+dt_min+":"+dt_sec+"\n"+dt_day+" "+dt_date+"-"+dt_mon+"-"+dt_year
    #print("OUTPUT: " + date_time_str)
    return date_time_str


class UpdateThread(threading.Thread):

    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.01):
            Screen().update_display(update_time())

class ClockModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.stopFlag = threading.Event()

    def enter(self):
        Screen().clear_display()
        self.thread = UpdateThread(self.stopFlag)
        self.thread.start()

        print("ENTER")

    def exit(self):
        print("EXITING")
        self.stopFlag.set()
        self.thread.join()
        self.stopFlag.clear()
        print("exited")
