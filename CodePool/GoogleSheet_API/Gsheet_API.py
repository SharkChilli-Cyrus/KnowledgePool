# -*- coding: utf-8-sig -*-
# Created Time: 19th Aug, 2020
#
# ====================================================================================================

__author__ = 'ZHU Xu'

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


def gsheet_get_credentials(scopes, credsFolder):
    creds = None
    crendentialPath = os.path.join(credsFolder, 'Gsheet_py3_credentials.json')
    tokenPath = os.path.join(credsFolder, 'Gsheet_py3_token.pickle')

    if os.path.exists(tokenPath):
        with open(tokenPath, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(crendentialPath, scopes)
            creds = flow.run_local_server()
        with open(tokenPath, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def gsheet_read_data(gsheetCreds, gsheetID, gsheetReadRange,
                     outputOption = 'DataFrame', printInfo = True):
    gsheetService = build('sheets', 'v4', credentials = gsheetCreds)
    sheet = gsheetService.spreadsheets()
    request = sheet.values().get(spreadsheetId = gsheetID, range = gsheetReadRange)
    response = request.execute()
    values = response['values']

    if outputOption.lower() == 'list':
        # result = [value[0] for value in values if value != []]
        result = []
        for value in values:
            if value == []:
                continue
            else:
                result.append(value[0])

    elif outputOption.lower() == 'string':
        pyVersion = int(sys.version_info[0])
        if pyVersion == 2:
            resultTemp = [str(value[0]).encode('utf-8') for value in values if value != []]
        else:
            resultTemp = [str(value[0]) for value in values if value != []]
        result = "(" + ",".join(resultTemp) + ")"

    else:
        cols = values.pop(0)
        result = pd.DataFrame(data = values, columns = cols)

    if printInfo == True:
        gsheetURL = 'https://docs.google.com/spreadsheets/d/{0}'.format(gsheetID)
        print("----- AUTO READ")
        print("* Read Data From: {0}".format(gsheetURL))
        print("* Read Range: {0}".format(gsheetReadRange))
        print("* Output Option: {0}".format(outputOption.lower()))
    else:
        pass

    return result


def gsheet_update(gsheetCreds, gsheetID, gsheetUpdateRange, df,
                  printInfo = True):
    gsheetService = build('sheets', 'v4', credentials = gsheetCreds)
    sheet = gsheetService.spreadsheets()
    clearBody = {}
    clearExecute = sheet.values().clear(spreadsheetId = gsheetID,
                                        range = gsheetUpdateRange,
                                        body = clearBody).execute()

    df = df.replace(np.nan, 'NA')
    updateBody = {'values': df.values.tolist()}
    updateExecute = sheet.values().update(spreadsheetId = gsheetID,
                                          range = gsheetUpdateRange,
                                          valueInputOption = 'RAW',
                                          body = updateBody).execute()

    if printInfo == True:
        gsheetURL = 'https://docs.google.com/spreadsheets/d/{0}'.format(gsheetID)
        print("----- AUTO UPDATE")
        print("* Update Data To: {0}".format(gsheetURL))
        print("* Update Range (Overwrite): {0}".format(gsheetUpdateRange))
    else:
        pass


# TEST
# ====================================================================================================
credsFolder = '/Users/xu.zhu/Desktop/Data/Keys/GoogleAPI/credentials'
homePath = os.path.dirname(os.path.abspath(__file__))
outputFolder = '/Users/xu.zhu/Desktop/Test/GoogleAPI_Test'

start_time = datetime.datetime.now()
today = datetime.datetime.today().strftime('%F')

scriptAbsPath = sys.argv[0]
scriptFileName = scriptAbsPath.split('/')[-1]
scriptEncoding = sys.getdefaultencoding()
scriptVersion = sys.version_info
pyVersion = "{major}.{minor}.{micro}".format(major = scriptVersion[0],
                                             minor = scriptVersion[1],
                                             micro = scriptVersion[2])

gsheetScopes = ['https://www.googleapis.com/auth/spreadsheets']
gsheetCreds = gsheet_get_credentials(gsheetScopes, credsFolder)


gsheetService = build('sheets', 'v4', credentials = gsheetCreds)
sheet = gsheetService.spreadsheets()
"""
# ----------------------------------------------------------------------------------------------------
# I: Read 
gsheetID = "1dh9wv93ELGgkWH2qCRjbYLws_esLLqmGfuLb8aM47cc"
gsheetURL = "https://docs.google.com/spreadsheets/d/{0}".format(gsheetID)
gsheetReadRange = "'Test 1'!A1:C"

request = sheet.values().get(spreadsheetId = gsheetID, range = gsheetReadRange)
response = request.execute()
# response should be like
# {'range': "'Test 1'!A1:D1000", 
#  'majorDimension': 'ROWS', 
#  'values': [
#             ['column1', 'column2', 'column3', 'column4'],
#             ['Tom', '12.3', '56', '2020-08-01'],
#             ['Jerry', '2.6', '92', '2020-08-02']
#         ]
# }
values = response['values']
cols = values.pop(0)
df = pd.DataFrame(data = values, columns = cols)
"""



end_time = datetime.datetime.now()
run_time = str(end_time - start_time)
# ----------------------------------------------------------------------------------------------------
print("======================================== Basic Info ========================================")
print("* Script File Name: {0}".format(scriptFileName))
print("* Script Python Version: {0}".format(pyVersion))
print("* Script Default Encoding: {0}".format(scriptEncoding))
print("* Script Abs Path: {0}".format(scriptAbsPath))
print("")
print("----- PATH INFO")
print("Credentials Folder: {0}".format(credsFolder))
print("Output Folder: {0}".format(outputFolder))
# print("")
# print("----- AUTO READ")
# print("* Upload Files To Gdrive: {0}".format(gdriveURL))
# print("* Uploaded {0} Files:\n\t{1}".format(len(uploadedFiles), uploadedFiles))
# print("")
# print("----- AUTO UPDATE")
# print("* Downloade Gdrive Files From: {0}".format(gdriveURL))
# print("* Matched {0} Files:\n\t{1}".format(len(matchedFiles), matchedFiles))
# print("* Downloaded {0} Files:\n\t{1}".format(len(downloadedFiles), downloadedFiles))
print("")
print("----- COST TIME")
print("* Start Time: {0}".format(str(start_time)))
print("* End Time: {0}".format(str(end_time)))
print("* Run Time: {0}".format(str(run_time)))