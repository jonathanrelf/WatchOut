__author__ = 'Jonathan'
import datetime
from WatchOut.ModeOption import ModeOption
from OneDiary.calendars import Calendars
from OneDiary.Events import Events
from WatchOut.Screen import Screen


class CalendarModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.one_diary_bearer_token = "irqghKXqA3nV978Z6Fq8qsFKZorlH3oD"

    def enter(self):
        event = Events(self.one_diary_bearer_token).retrieve_first()
        Screen().update_display(event['summary'], event['start'])

    def option3(self):
        calendars = Calendars(self.one_diary_bearer_token)
        calendar = calendars.retrieve()
        print(calendar)
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(hours=1)
        calendars.create_event(calendar['calendar_id'],"Hello","World",start_date,end_date)
