__author__ = 'Jonathan'
import requests


class Events(object):
    def __init__(self,bearer_key=''):
        self.bearer_key = bearer_key
        self.endpoint = "https://api.onediary.com/v1/events"
        self.headers = {'Authorization': "Bearer " + bearer_key }