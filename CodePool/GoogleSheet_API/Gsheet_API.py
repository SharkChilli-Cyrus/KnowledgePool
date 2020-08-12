# -*- coding: utf-8-sig -*-
#
# |-- home_path
# |       `-- xxx.py
# |       |-- credentials
#
# ====================================================================================================

import sys
import os
import datetime
import time

import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pandas as pd
import numpy as np

# Google Sheet API v4: Get Credential
def gsheet_GetCredentials(SCOPES, folder_path):
    creds = None
    crendential_path = os.path.join(folder_path, 'Gsheet_credentials_Eric.json')
    token_path = os.path.join(folder_path, 'Gsheet_token_Eric_py3.pickle')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(crendential_path, SCOPES)
            creds = flow.run_local_server()
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

# ====================================================================================================




# ====================================================================================================
home_path = os.path.dirname(os.path.abspath(__file__))
credential_folder = os.path.join(home_path, 'credentials')
input_folder = os.path.join(home_path, 'InputFolder')
print('')
print("-------------------- Basic Info --------------------")
print("* Credentials Folder Path: {0}".format(credential_folder))
print("* Input Folder Path: {0}".format(input_folder))


all_files = []
add_text = []


# Test
gsheet_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# gsheet_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
gsheet_creds = gsheet_GetCredentials(gsheet_SCOPES, credential_folder)
service = build('sheets', 'v4', credentials=gsheet_creds)
sheet = service.spreadsheets()
# I:
# 