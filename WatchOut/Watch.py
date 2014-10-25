from WatchOut.ClockModeOption import ClockModeOption


class Watch(object):
    def __init__(self, pfc, start_mode='clock'):
        self.pfc = pfc
        possible_modes = ('clock')

        self.current_mode_index = possible_modes.index(start_mode)
        self.modes = ({'name': 'clock', 'option': ClockModeOption(self)},)
        self.current_mode['option'].enter()

    def switch_mode(self):
        self.current_mode['option'].exit()
        self.current_mode_index = (self.current_mode_index + 1) % len(self.modes)

    @property
    def current_mode(self):
        return self.modes[self.current_mode_index]
