__author__ = 'Jonathan'
import pifacecad
import requests

one_diary_bearer_token = "irqghKXqA3nV978Z6Fq8qsFKZorlH3oD"

headers = {'Authorization': "Bearer " + one_diary_bearer_token }
calendars_response = requests.get("https://api.onediary.com/v1/calendars",headers=headers)

#name = request.json().calendar_name
calendars_json = calendars_response.json()
calendars = calendars_json['calendars']
calendar = calendars[0]

events_response = requests.get("https://api.onediary.com/v1/events", headers=headers)
print(events_response.text)
#events_json = events_response.json()
#print (events_json)
pfc = pifacecad.PiFaceCAD()
pfc.lcd.clear()
#pfc.lcd.write(calendar['calendar_name'])
