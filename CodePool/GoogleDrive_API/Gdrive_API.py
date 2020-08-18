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


def gdrive_get_credentials(scopes, credentialsFolderPath):
    creds = None
    crendentialPath = os.path.join(credentialsFolderPath, 'Gdrive_py3_credentials.json')
    tokenPath = os.path.join(credentialsFolderPath, 'Gdrive_py3_token.pickle')

    if os.path.exists(tokenPath):
        with open(tokenPath, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(crendentialPath, scopes)
            creds = flow.run_local_server(port=0)

        with open(tokenPath, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def gdrive_download(gdriveCreds, gdriveFolderID, downloadFolderPath, gdriveFileMatchKeys,
                    printInfo = True):
    """
    Parameters
        gdriveCreds:
            - GDrive API Crendentials
        gdriveFolderID: str_like
            - The GDrive Folder ID
            - Download files from it
        downloadFolderPath:
            - Absolute Paths of the local folders to save all downloaded files
        gdriveFileMatchKeys: list_like
            - Includes key words to match file names
        printInfo: boolean (default is FALSE)
            - Decide whether to print outputs

    Returns:
        downloadedFiles: list_like
            - Names of all downloaded files
    """

    matchedFiles = []
    downloadedFiles = []
    gdriveURL = 'https://drive.google.com/drive/u/0/folders/{0}'.format(gdriveFolderID)

    gdriveService = build('drive', 'v3', credentials = gdriveCreds)
    gdriveSearchQuery = "'{0}' in parents".format(gdriveFolderID)
    listedResponse = gdriveService.files().list(q = gdriveSearchQuery).execute()

    listedFiles = listedResponse['files']
    for gdriveFile in listedFiles:
        gdirveFileID = gdriveFile['id']
        gdriveFileName = gdriveFile['name']

        for _ in gdriveFileMatchKeys:
            if "translated" in gdriveFileName and _ in gdriveFileName: # 
                matchedFiles.append(gdriveFileName)
                request = gdriveService.files().get_media(fileId = gdirveFileID)
                
                # Method I
                with open(os.path.join(downloadFolderPath, gdriveFileName), 'wb') as f:
                    downloader = MediaIoBaseDownload(f, request)
                    done = False
                    while done is False:
                        status, done = downloader.next_chunk()
                downloadedFiles.append(gdriveFileName)

                # Method II
                # fh = io.BytesIO(request.execute())
                # with io.open(os.path.join(downloadFolderPath, gdriveFileName), 'wb') as f:
                #     fh.seek(0)
                #     f.write(fh.read())
                # print("Downloaded {0}".format(gdriveFileName))
            else:
                pass

    if printInfo == True:
        print("----- AUTO DOWNLOAD")
        print("* Downloade Gdrive Files From: {0}".format(gdriveURL))
        print("* Matching Keys: {0}".format(gdriveFileMatchKeys))
        print("* Matched {0} Files:\n\t{1}".format(len(matchedFiles), matchedFiles))
        print("* Downloaded {0} Files:\n\t{1}".format(len(downloadedFiles), downloadedFiles))
    else:
        pass

    return downloadedFiles


def gdrive_upload(gdriveCreds, gdriveFolderID, allFilePaths,
                  newFolderOption = True, printInfo = True,
                  **kwargs):
    """
    Parameters
        gdriveCreds:
            - GDrive API Crendentials
        gdriveFolderID: str_like
            - The GDrive Folder ID
            - Need to upload files into it
            - Or create a new sub folder in it
        allFilePaths: list_like
            - Absolute Paths of all local files that need to be uploaded
        newFolderOption: boolean (default is TRUE)
            - Decide whether to create a new subfolder
            - NOTE: This function only considers level2 folders structure
            - which means parent_folder --> new_sub_folder
        printInfo: boolean (default is FALSE)
            - Decide whether to print outputs
        kwargs: dict_like (optional)
            - If you choose newFolderOption = True
            - Should pass another parameter into kwargs as the new subfolder's name

    Returns:
        uploadedFiles: list_like
            - Names of all uploaded files
    """

    uploadedFiles = []
    gdriveService = build('drive', 'v3', credentials = gdriveCreds)
    gdriveURL = 'https://drive.google.com/drive/u/0/folders/{0}'.format(gdriveFolderID)

    if newFolderOption == True:
        if 'newFolderName' in kwargs.keys():
            newFolderName = kwargs['newFolderName']
        else:
            newFolderName = kwargs[list(kwargs.keys())[0]]

        folderMetaData = {'name': str(newFolderName), 
                          'mimeType': 'application/vnd.google-apps.folder', 
                          'parents': [gdriveFolderID]}

        newFolderObject = gdriveService.files().create(body = folderMetaData,
                                                       fields = 'id').execute()
        folderID = newFolderObject['id']
    else:
        folderID = gdriveFolderID

    for filePath in allFilePaths:
        uploadedFileName = filePath.split('/')[-1]
        fileMetaData = {"name": uploadedFileName, "parents": [folderID]}

        # Here only considering csv and xlsx 2 formats
        # More MIME Types Refer: https://developers.google.com/drive/api/v3/ref-export-formats
        uploadedFileFormat = uploadedFileName.split('.')[-1]
        if uploadedFileFormat == 'csv':
            uploadedFileType = 'text/csv'
        else:
            uploadedFileType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        
        media = MediaFileUpload(filePath, mimetype = uploadedFileType)
        file = gdriveService.files().create(body = fileMetaData,
                                            media_body = media,
                                            fields = 'id').execute()
        uploadedFiles.append(uploadedFileName)
    
    if printInfo == True:
        print("----- AUTO UPLOAD")
        print("* Upload Files To Gdrive: {0}".format(gdriveURL))
        print("* Create New Folder Option: {0}".format("True\n* New Folder Name: {0}".format(newFolderName) if newFolderOption == True else "False"))
        print("* Uploaded {0} Files:\n\t{1}".format(len(uploadedFiles), uploadedFiles))
    else:
        pass

    return uploadedFiles


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

home_path = os.path.dirname(os.path.abspath(__file__))
credentialsFolder = "/Users/xu.zhu/Desktop/Data/Keys/GoogleAPI/credentials"
downloadFolder = '/Users/xu.zhu/Desktop/Test/GoogleAPI_Test'
outputFolder = '/Users/xu.zhu/Desktop/Test/GoogleAPI_Test'
# credential_folder = os.path.join(home_path, 'credentials')
# download_path = '/ldap_home/xu.zhu/Downloads/' # change
# output_folder = '/ldap_home/xu.zhu/Crontab_Output/' # change

gdriveScopes = ['https://www.googleapis.com/auth/drive']
gdriveCreds = gdrive_get_credentials(gdriveScopes, credentialsFolder)
gdriveService = build('drive', 'v3', credentials = gdriveCreds)


# gdriveFolderID = '15aCgr10Hjx0IAiTtufa6IOQa7RJ_n0yD'
# allFilePaths = [os.path.join(outputFolder, 'Test1.csv'), os.path.join(outputFolder, 'Test2.xlsx')]
# uploadedFiles = gdrive_upload(gdriveCreds, gdriveFolderID, allFilePaths, newFolderOption = False)

"""
# ----------------------------------------------------------------------------------------------------
# I: Upload
allFilePaths = [os.path.join(outputFolder, 'Test1.csv'), os.path.join(outputFolder, 'Test2.xlsx')]
# allFilePaths = [os.path.join(outputFolder, 'Test1.csv')]

gdriveFolderID = '15aCgr10Hjx0IAiTtufa6IOQa7RJ_n0yD'
gdriveURL = 'https://drive.google.com/drive/u/0/folders/{0}'.format(gdriveFolderID)

newFolderOption = False #

if newFolderOption == True:
    # create a subfolder in google_folder (google_folder_id)
    newFolderName = today
    folder_metadata = {
        'name': str(newFolderName), 
        'mimeType': 'application/vnd.google-apps.folder', 
        'parents': [gdriveFolderID]}

    newFolderObject = gdriveService.files().create(body = folder_metadata, fields = 'id').execute()
    # newFolderObject should be like:
    # {'id': '1vd48ok5jG09FLvfFb3Vr_vTdA1EiwHu0'}

    folderID = newFolderObject['id']
else:
    folderID = gdriveFolderID

uploadedFiles = []
for filePath in allFilePaths:
    uploadedFileName = filePath.split('/')[-1]
    fileMetaData = {"name": uploadedFileName, "parents": [folderID]}

    # More MIME Types Refer: https://developers.google.com/drive/api/v3/ref-export-formats
    uploadedFileFormat = uploadedFileName.split('.')[-1]
    if uploadedFileFormat == 'csv':
        uploadedFileType = 'text/csv'
    else:
        uploadedFileType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    
    media = MediaFileUpload(filePath, mimetype = uploadedFileType)
    file = gdriveService.files().create(body = fileMetaData,
                                        media_body = media,
                                        fields = 'id').execute()
    
    uploadedFiles.append(uploadedFileName)
"""

"""
# ----------------------------------------------------------------------------------------------------
# II: Download
gdriveFolderID = '1E7NUXhpxCZMQoG0D1_5e2PDFkXxpsjfN'
gdriveURL = 'https://drive.google.com/drive/u/0/folders/{0}'.format(gdriveFolderID)

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
# ----------------------------------------------------------------------------------------------------
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
print("Credentials Folder: {0}".format(credentialsFolder))
print("Download Folder: {0}".format(downloadFolder))
print("Output Folder: {0}".format(outputFolder))
# print("")
# print("----- AUTO UPLOAD")
# print("* Upload Files To Gdrive: {0}".format(gdriveURL))
# print("* Uploaded {0} Files:\n\t{1}".format(len(uploadedFiles), uploadedFiles))
# print("")
# print("----- AUTO DOWNLOAD")
# print("* Downloade Gdrive Files From: {0}".format(gdriveURL))
# print("* Matched {0} Files:\n\t{1}".format(len(matchedFiles), matchedFiles))
# print("* Downloaded {0} Files:\n\t{1}".format(len(downloadedFiles), downloadedFiles))
print("")
print("----- COST TIME")
print("* Start Time: {0}".format(str(start_time)))
print("* End Time: {0}".format(str(end_time)))
print("* Run Time: {0}".format(str(run_time)))