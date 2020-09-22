# coding=utf-8
#
# Here only considering csv and xlsx 2 formats
# More MIME Types Refer: https://developers.google.com/drive/api/v3/ref-export-formats
#
# @author: Zhu Xu
# @date: 2020-09-21
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


class GdriveAPI(object):
    """
    Call Google Drive API - v3
    """

    def __init__(self, drive_scopes = ["https://www.googleapis.com/auth/drive"]):
        self.scopes = drive_scopes
        self.creds = None
        self.upload_to = None
        self.download_from = None
        self.uploaded_files = []
        self.downloaded_files = []


    def get_creds(self, credential_folder,
        credential_filename = "Gdrive_py3_credentials.json",
        token_filename = "Gdrive_py3_token.pickle"):

        creds = None
        credential_path = os.path.join(credential_folder, credential_filename)
        token_path = os.path.join(credential_folder, token_filename)

        if os.path.exists(token_path):
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credential_path, self.scopes)
                creds = flow.run_local_server(port=0)

            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)

        if creds:
            self.creds = creds
            print("* Got Google Drive API Credentials")
        else:
            print("x Get Credentials FAIL!")


    def upload(self, files, grive_folder_id,
        new_folder = False, show_info = True,
        **kwargs):
        """
        ------------------------------------------------------------------------------------------
        Parameters
            gdriveCreds:
                - GDrive API Crendentials
            grive_folder_id: str_like
                - The GDrive Folder ID
                - Need to upload files into it
                - Or create a new sub folder in it
            files: list_like
                - Absolute Paths of all local files that need to be uploaded
            new_folder: boolean (default is False)
                - Decide whether to create a new subfolder
                - NOTE: This function only considers level2 folders structure
                - which means parent_folder --> new_sub_folder
            show_info: boolean (default is True)
                - Decide whether to print outputs
            kwargs: dict_like (optional)
                - If you choose new_folder = True
                - Should pass another parameter into kwargs as the new subfolder's name

        Returns:
            uploadedFiles: list_like
                - Names of all uploaded files
        ------------------------------------------------------------------------------------------
        """

        # uploaded_files = []
        self.upload_to = 'https://drive.google.com/drive/u/0/folders/{0}'.format(grive_folder_id)
        service = build('drive', 'v3', credentials = self.creds)

        if new_folder == True:
            if 'folder_name' in kwargs.keys():
                folder_name = kwargs['folder_name']
            else:
                folder_name = kwargs[list(kwargs.keys())[0]]

            folder_meta_data = {'name': str(folder_name), 
                                'mimeType': 'application/vnd.google-apps.folder', 
                                'parents': [grive_folder_id]}

            folder_object = service.files().create(body = folder_meta_data, fields = 'id').execute()
            folder_id = folder_object['id']
        else:
            folder_id = grive_folder_id

        for file_path in files:
            filename = file_path.split('/')[-1]
            file_meta_data = {"name": filename, "parents": [folder_id]}

            # Here only considering csv and xlsx 2 formats
            # More MIME Types Refer: https://developers.google.com/drive/api/v3/ref-export-formats
            file_format = filename.split('.')[-1]
            if file_format == 'csv':
                upload_type = 'text/csv'
            elif file_format == 'xlsx':
                upload_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            else:
                print("x Upload FAIL, please check file type is 'csv' or 'xlsx'.")
                print("\t- Failed file: {0}".format(filename))
                return None
            
            media = MediaFileUpload(file_path, mimetype = upload_type)
            file = service.files().create(body = file_meta_data,
                                        media_body = media,
                                        fields = 'id').execute()
            self.uploaded_files.append(filename)
        
        if show_info == True:
            print("----- AUTO UPLOAD")
            print("* Upload Files To Gdrive: {0}".format(self.upload_to))
            print("* Create New Folder Option: {0}".format("True\n* New Folder Name: {0}".format(folder_name) if new_folder == True else "False"))
            print("* Uploaded {0} Files:\n\t{1}".format(len(self.uploaded_files), self.uploaded_files))
        else:
            pass



# TEST
start_time = datetime.datetime.now()
today = datetime.datetime.today().strftime('%F')

root_path = os.path.dirname(os.path.abspath(__file__))
credential_folder = "/Users/xu.zhu/Desktop/Data/Keys/GoogleAPI/credentials"
download_folder = '/Users/xu.zhu/Desktop/Test/GoogleAPI_Test'
output_folder = '/Users/xu.zhu/Desktop/Test/GoogleAPI_Test'


upload_files = [os.path.join(output_folder, 'Test1.csv'), os.path.join(output_folder, 'Test2.xlsx')]
test_folder_id = '1HY79S20FC3xC3GMhPM1VmVMG0XRVpXA0'

gdrive_object = GdriveAPI()
gdrive_object.get_creds(credential_folder)
gdrive_object.upload(upload_files, test_folder_id)


end_time = datetime.datetime.now()
run_time = str(end_time - start_time)
print("")
print("----- COST TIME")
print("* Start Time: {0}".format(str(start_time)))
print("* End Time: {0}".format(str(end_time)))
print("* Run Time: {0}".format(str(run_time)))
