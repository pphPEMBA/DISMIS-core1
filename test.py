from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime


SCOPES = "https://www.googleapis.com/auth/calendar"
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

calendar_list_entry = service.calendarList().get(calendarId='primary').execute()
if calendar_list_entry['accessRole']:
    # This next section's code will be here

    startTime = datetime.strptime(input("Please enter in the start time for the event in this format: (ex. September 02, 2018, 09:00PM) "), '%B %m, %Y, %I:%M%p').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    endTime = datetime.strptime(input("Please enter in the end time for the event in this format: (es. September 03, 2018, 11:25AM) "), '%B %m, %Y, %I:%M%p').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    