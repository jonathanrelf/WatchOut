__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
from WatchOut.Screen import Screen
import time
import threading
import pifacecad

class UpdateThread(threading.Thread):
    pfc = pifacecad.PiFaceCAD()
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        print("RUN")
        while not self.stopped.wait(1):
            Screen().update_display(self.update_time())
        print("STOP LOOP")

    def update_time(self):
        dt_hour = time.strftime("%H")
        dt_min = time.strftime("%M")
        dt_sec = time.strftime("%S")

        dt_day = time.strftime("%a")
        dt_date = time.strftime("%d")
        dt_mon = time.strftime("%m")
        dt_year = time.strftime("%Y")

        date_time_str = dt_hour+":"+dt_min+":"+dt_sec+"\n"+dt_day+" "+dt_date+"-"+dt_mon+"-"+dt_year
        print("OUTPUT: " + date_time_str)
        return date_time_str

class ClockModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)

    def enter(self):
        self.stopFlag = threading.Event()
        thread = UpdateThread(self.stopFlag)
        thread.start()

        print("ENTER")

        Screen().clear_display

    def exit(self):
        print("EXIT")
        self.stopFlag.set()
