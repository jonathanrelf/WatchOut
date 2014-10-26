__author__ = 'Jonathan'
from OneDiary.calendars import Calendars
from OneDiary.Events import Events


def initialise(bearer_key=''):
    global calendars
    calendars = Calendars(bearer_key)

    global events
    events = Events(bearer_key)
