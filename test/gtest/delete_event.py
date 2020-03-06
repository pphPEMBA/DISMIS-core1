from cal_setup import get_calendar_service

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pytz
import subprocess

def main():
    # Delete the event
    service = get_calendar_service()
    try:
        service.events().delete(
            calendarId='primary',
            eventId='4qnt0okd4dmr0hik3mh073qnls',
        ).execute()
    except googleapiclient.errors.HttpError:
        print("Failed to delete event")
    
    print("Event deleted")

if __name__ == '__main__':
    main()
