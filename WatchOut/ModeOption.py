__author__ = 'Jonathan'
import pifacecad


class ModeOption(object):
    def __init__(self,watch):
        self.watch = watch

    def enter(self):
        pass

    def exit(self):
        pass

    def next(self):
        pass

    def previous(self):
        pass

    def option1(self):
        pass

    def option2(self):
        pass

    def option3(self):
        pass

    def option4(self):
        pass

    def update_display(self, text=""):
        clear_display()
        self.watch.pfc.lcd.write(text)

    def clear_display(self):
        self.watch.pfc.lcd.clear()
