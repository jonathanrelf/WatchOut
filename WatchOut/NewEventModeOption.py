__author__ = 'Jonathan'
from WatchOut.ModeOption import ModeOption
from pifacecad.tools.question import LCDQuestion
from WatchOut.Screen import Screen
from OneDiary.calendars import Calendars
import datetime


class NewEventModeOption(ModeOption):
    def __init__(self,*args):
        super().__init__(*args)
        self.one_diary_bearer_token = "irqghKXqA3nV978Z6Fq8qsFKZorlH3oD"
        self.week = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
    def enter(self):
        what_answers = ("Meeting","Breakfast","Lunch","Dinner","Party")
        what_question = LCDQuestion(question="Meeting type?",
                               answers=what_answers,
                               selector="#",
                               cad=Screen().pfc)

        what_answer = what_answers[what_question.ask()]

        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        three_days = tomorrow + datetime.timedelta(days=1)
        four_days = three_days + datetime.timedelta(days=1)
        five_days = four_days + datetime.timedelta(days=1)

        # which_day_answers = (today.day,tomorrow.day,three_days.day,four_days.day,five_days.day)
        # which_day_question = LCDQuestion(question="Which day?",
        #                                   answers=which_day_answers,
        #                                   selector="#",
        #                                   cad=Screen().pfc)
        # which_day_answer = which_day_answers[which_day_question.ask()]

        when_answers = ("08", "09", "10", "11", "12", "13",
                        "14", "15", "16", "17", "18", "19", )
        when_question = LCDQuestion(question="Meeting time?",
                                    answers=when_answers,
                                    selector='#',
                                    cad=Screen().pfc)
        when_answer = when_answers[when_question.ask()]

        calendars = Calendars(self.one_diary_bearer_token)
        calendar = calendars.retrieve()

        hour = int(when_answer)
        start_time = datetime.time(hour=hour)
        start_date = datetime.datetime.combine(datetime.date.today(),start_time)
        end_date = start_date + datetime.timedelta(hours=1)
        print(start_date)
        subject = what_answer
        calendars.create_event(calendar['calendar_id'],subject,"World",start_date,end_date)

        self.watch.switch_mode('menu')

    def exit(self):
        Screen().hide_cursors()