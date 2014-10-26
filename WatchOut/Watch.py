from WatchOut.ClockModeOption import ClockModeOption
from WatchOut.CalendarModeOption import CalendarModeOption
from WatchOut.MenuModeOption import MenuModeOption
from WatchOut.SplashModeOption import SplashModeOption


class Watch(object):
    def __init__(self, pfc, start_mode='menu'):
        self.pfc = pfc
        self.possible_modes = ('splash','menu','clock','calendar')

        self.current_mode_index = self.possible_modes.index(start_mode)
        self.modes = ({'name': 'splash', 'option': SplashModeOption(self)},
                      {'name': 'menu', 'option': MenuModeOption(self)},
                      {'name': 'clock', 'option': ClockModeOption(self)},
                      {'name': 'calendar', 'option': CalendarModeOption(self)},)
        self.current_mode['option'].enter()

    def switch_mode(self,mode=''):
        self.current_mode['option'].exit()
        self.current_mode_index = self.possible_modes.index(mode)
        self.current_mode['option'].enter()

    def show_menu(self):
        self.switch_mode('menu')

    @property
    def current_mode(self):
        return self.modes[self.current_mode_index]
