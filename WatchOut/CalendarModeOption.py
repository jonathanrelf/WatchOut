__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
from OneDiary.Calendars import Calendars
from WatchOut.Screen import Screen


class CalendarModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)

    def enter(self):
        one_diary_bearer_token = "irqghKXqA3nV978Z6Fq8qsFKZorlH3oD"
        calendar = Calendars(one_diary_bearer_token).retrieve()
        Screen().update_display(calendar['calendar_name'])
        pass