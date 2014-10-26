__author__ = 'Jonathan'
import datetime
from WatchOut.ModeOption import ModeOption
from OneDiary.Events import Events
from WatchOut.Screen import Screen


class CalendarModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.one_diary_bearer_token = "irqghKXqA3nV978Z6Fq8qsFKZorlH3oD"

    def enter(self):
        event = Events(self.one_diary_bearer_token).retrieve_first()
        Screen().update_display(event['summary'], event['start'])


