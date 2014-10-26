__author__ = 'Jonathan'
import requests


class Events(object):
    def __init__(self,bearer_key=''):
        self.bearer_key = bearer_key
        self.events_filter = "from=2014-10-26&to=2014-11-25&tzid=Europe%2FLondon"
        self.endpoint = "https://api.onediary.com/v1/events?" + self.events_filter
        self.headers = {'Authorization': "Bearer " + bearer_key }

    def retrieve_first(self):
        print('retrieving first event')
        events_response = requests.get(self.endpoint, headers=self.headers)
        events_json = events_response.json()
        print(events_json)
        events = events_json['events']
        return events[0]
