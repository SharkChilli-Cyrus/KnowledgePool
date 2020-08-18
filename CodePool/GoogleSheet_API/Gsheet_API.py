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
def gsheet_get_credentials(SCOPES, folder_path):
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


def gsheet_read_tab(sheet, sheet_id, read_range):
    request = sheet.values().get(spreadsheetId=sheet_id,
                                 range=read_range)

    response = request.execute()
    values = response['values']
    cols = values.pop(0)
    df = pd.DataFrame(data = values, columns = cols)

    return df


def read_Gsheet_int(sheet, spreadsheet_id, read_range):
    request = sheet.values().get(spreadsheetId=spreadsheet_id,
                                 range=read_range)
    response = request.execute()
    values = response['values']

    query_list = []
    for i in values:
        if i == []:
            i = [404404]
        else:
            i[0] = i[0].encode('utf-8')
        query_list.append(i[0])

    return query_list

def read_Gsheet_str(sheet, spreadsheet_id, read_range):
    request = sheet.values().get(spreadsheetId=spreadsheet_id,
                                 range=read_range)
    response = request.execute()
    values = response['values']

    query_list = []
    for i in values:
        if i == []:
            i = ['None']
        else:
            i[0] = i[0].encode('utf-8')
        query_list.append(i[0])

    return query_list

# Upload data to GSheet
def upload_csv(sheet, sheet_id, upload_range, df):
    print('')
    print('='*15, 'Upload csv To Google Sheet Begin', '='*15)

    # Clear the sheet
    clear_body = {}
    clear_result = sheet.values().clear(spreadsheetId=sheet_id,
                                        range=upload_range,
                                        body=clear_body).execute()

    df = df.replace(np.nan,'NA')

    print('Google Sheet ID:', sheet_id)
    print('Clear Range:', upload_range)
    print('='*5, 'Clear Google Sheet Finished')

    print('Upload DataFrame Shape:', df.shape)
    print('GSheet Range:', upload_range)

    body = {'values': df.values.tolist()}
    result = sheet.values().update(spreadsheetId = sheet_id,
                                   range = upload_range,
                                   valueInputOption = 'RAW',
                                   body = body).execute()

    print('='*15, 'Upload csv To Google Sheet Finished', '='*15)
    print('')
    
# ====================================================================================================




# ====================================================================================================
credential_folder = '/Users/xuzhu/Desktop/Keys/Gsheet_API' # AbsPath
home_path = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(home_path, 'InputFolder')
print('')
print("-------------------- Basic Info --------------------")
print("* Credentials Folder Path: {0}".format(credential_folder))
print("* Input Folder Path: {0}".format(input_folder))

all_files = []
add_text = []


# Test
gsheet_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheet_creds = gsheet_GetCredentials(gsheet_SCOPES, credential_folder)
service = build('sheets', 'v4', credentials=gsheet_creds)
sheet = service.spreadsheets()

# I: Read Data From Google Sheet
gsheet_id = "1nwnS2SeqFnym8vuuNz1Zt-HPXthvhZjHbbJiNYl9xiE"
google_sheet_url = "https://docs.google.com/spreadsheets/d/{0}".format(gsheet_id)
gsheet_read_range = "'Test 1'!A1:D"

""" df = gsheet_ReadTab(sheet, gsheet_id, gsheet_read_range)

request = sheet.values().get(spreadsheetId = gsheet_id,
                             range = gsheet_read_range)

response = request.execute()
# response = {
#     'range': "'Test 1'!A1:D1000", 
#     'majorDimension': 'ROWS', 
#     'values': [
#                 ['column1', 'column2', 'column3', 'column4'],
#                 ['Tom', '12.3', '56', '2020-08-01'],
#                 ['Jerry', '2.6', '92', '2020-08-02']
#               ]
# }

values = response['values']
cols = values.pop(0) 
df = pd.DataFrame(data = values, columns = cols)
"""

