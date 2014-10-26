__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
from OneDiary.Events import Events
from WatchOut.Screen import Screen


class CalendarModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.one_diary_bearer_token = "irqghKXqA3nV978Z6Fq8qsFKZorlH3oD"
        self.events = Events(self.one_diary_bearer_token).retrieve_all()
        self.event_index = 0

    def enter(self):
        self.display_event()

    def option1(self):
        self.display_event()

    def option2(self):
        Screen().clear_display()
        Screen().update_display("Events next 30 days ",len(self.events).__str__())

    def option4(self):
        Screen().clear_display()
        Screen().update_display("EVT SUM ___"," v   v   v")

    def option6(self):
        self.event_index += 1
        self.display_event()

    def option7(self):
        self.event_index -= 1
        self.display_event()

    def display_event(self):
        event = self.events[self.event_index]
        Screen().update_display(event['summary'], event['start'])



