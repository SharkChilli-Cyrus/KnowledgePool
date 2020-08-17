# -*- coding: utf-8-sig -*-
#
# ====================================================================================================

import sys
import os
import io
import datetime
import time
import re
import base64

import pandas as pd
import numpy as np

import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


def gdrive_get_credentials(scopes, folder_path):
    creds = None
    crendential_path = os.path.join(folder_path, 'Gdrive_py3_credentials.json')
    token_path = os.path.join(folder_path, 'Gdrive_py3_token.pickle')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(crendential_path, scopes)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds



# Test
# ====================================================================================================
start_time = datetime.datetime.now()
today = datetime.datetime.today().strftime('%F')
d1 = (datetime.datetime.today() - datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
d2 = (datetime.datetime.today() - datetime.timedelta(days = 2)).strftime("%Y-%m-%d")
d3 = (datetime.datetime.today() - datetime.timedelta(days = 3)).strftime("%Y-%m-%d")

scriptAbsPath = sys.argv[0]
scriptFileName = scriptAbsPath.split('/')[-1]
scriptEncoding = sys.getdefaultencoding()
scriptVersion = sys.version_info
pyVersion = "{major}.{minor}.{micro}".format(major = scriptVersion[0],
                                             minor = scriptVersion[1],
                                             micro = scriptVersion[2])


# Abs Path Info (Change)
credentialsFolder = "/Users/xu.zhu/Desktop/Data/Keys/GoogleAPI/credentials"
downloadFolder = '/Users/xu.zhu/Desktop/Test'
outputFolder = '/Users/xu.zhu/Desktop/Test'

home_path = os.path.dirname(os.path.abspath(__file__))
# credential_folder = os.path.join(home_path, 'credentials')
# download_path = '/ldap_home/xu.zhu/Downloads/' # change
# output_folder = '/ldap_home/xu.zhu/Crontab_Output/' # change
all_files = []
add_text = []

gdriveScopes = ['https://www.googleapis.com/auth/drive']
gdriveCreds = gdrive_get_credentials(gdriveScopes, credentialsFolder)
# ----------------------------------------------------------------------------------------------------
# II: Download
gdriveFolderID = '1E7NUXhpxCZMQoG0D1_5e2PDFkXxpsjfN'
gdriveURL = 'https://drive.google.com/drive/u/0/folders/{0}'.format(gdriveFolderID)
gdriveService = build('drive', 'v3', credentials = gdriveCreds)

# search
gdriveSearchQuery = "'{0}' in parents".format(gdriveFolderID)
listedResponse = gdriveService.files().list(q = gdriveSearchQuery).execute()
# gdriveService.files().list(q = "'{0}' in parents".format(gdriveFolderID)).execute()
# The response should be like:
# 
# {'kind': 'drive#fileList', 
#  'incompleteSearch': False, 
#  'files': [
#       {'kind': 'drive#file', 
#        'id': '1Cr1yQWn4Rg3IJqe0lsqk74yByI4by30a', 
#        'name': '2020-08-12_ID_Translation_Raw-translated.xlsx', 
#        'mimeType': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#       },
#   ]
# }

listedFiles = listedResponse['files']
gdriveFileMatchKeys = [today, d1, d2, d3, "2020-05-13", "2020-05-27"]
matchedFiles = []
downloadedFiles = []
for gdriveFile in listedFiles:
    gdirveFileID = gdriveFile['id']
    gdriveFileName = gdriveFile['name']

    for _ in gdriveFileMatchKeys[1:]:
        if "translated" in gdriveFileName and _ in gdriveFileName:
            matchedFiles.append(gdriveFileName)
            request = gdriveService.files().get_media(fileId = gdirveFileID)
            
            # Method I
            with open(os.path.join(downloadFolder, gdriveFileName), 'wb') as f:
                downloader = MediaIoBaseDownload(f, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
            downloadedFiles.append(gdriveFileName)

            # Method II
            # fh = io.BytesIO(request.execute())
            # with io.open(os.path.join(download_path, gdriveFileName), 'wb') as f:
            #     fh.seek(0)
            #     f.write(fh.read())
            # print("Downloaded {0}".format(gdriveFileName))
        else:
            pass

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
print("Credentials Folder: {0}".format(credentialsFolder))
print("Download Folder: {0}".format(downloadFolder))
print("Output Folder: {0}".format(outputFolder))
print("")
print("----- AUTO DOWNLOAD")
print("* Downloade Gdrive Files From: {0}".format(gdriveURL))
print("* Matched {0} Files:\n\t{1}".format(len(matchedFiles), matchedFiles))
print("* Downloaded {0} Files:\n\t{1}".format(len(downloadedFiles), downloadedFiles))
print("")
print("----- COST TIME")
print("* Start Time: {0}".format(str(start_time)))
print("* End Time: {0}".format(str(end_time)))
print("* Run Time: {0}".format(str(run_time)))

