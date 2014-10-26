__author__ = 'Jonathan'
# Retrieves the Calendars
import requests
import uuid
import datetime


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

    def create_event(self,calendar_id='',summary='',description='',
                     start_date=datetime.datetime.now(),end_date=datetime.datetime.now()):
        create_url = self.endpoint + "/" + calendar_id + "/events"

        event = {'event_id': uuid.uuid4(),
                 'summary':summary,
                 'description':description,
                 'start':start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                 'end': end_date.strftime("%Y-%m-%dT%H:%M:%SZ")}
        create_response = requests.post(create_url,data=event,headers=self.headers)
        print(create_response.text)