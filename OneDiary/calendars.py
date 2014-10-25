__author__ = 'Jonathan'
# Retrieves the Calendars
import requests


class Calendars(object):
    def __init__(self,bearer_key=''):
        self.bearer_key = bearer_key
        self.endpoint = "https://api.onediary.com/v1/calendars"
        self.headers = {'Authorization': "Bearer " + bearer_key }

    def retrieve(self):
        calendars_response = requests.get("https://api.onediary.com/v1/calendars", headers=self.headers)
        calendars_json = calendars_response.json()
        calendars = calendars_json['calendars']
        return calendars[0]