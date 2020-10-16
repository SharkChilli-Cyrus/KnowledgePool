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

    def __init__(self,
        credential_path, 
        token_path=None,
        drive_scopes=["https://www.googleapis.com/auth/drive"]
    ):

        self.credential_path = credential_path
        self.token_path = token_path
        self.scopes = drive_scopes
        self.creds = None
        
        self.upload_to = None
        self.download_from = None
        self.uploaded_files = []
        self.downloaded_files = []
        self.log = []

        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credential_path, self.scopes)
                self.creds = flow.run_local_server(port=0)

            with open(self.token_path, 'wb') as token:
                pickle.dump(self.creds, token)

        if self.creds:
            print("* Got Google Drive API Credentials")
        else:
            print("x Get Google Drive Credentials FAIL!")


    def upload(self,
        files,
        gdrive_folder_id,
        new_folder=False,
        show_info=True,
        **kwargs
    ):
        """
        ------------------------------------------------------------------------------------------
        Parameters:
            @ gdrive_folder_id: str_like
                - The GDrive Folder ID
                - Need to upload files into it
                - or create a new sub folder in it
            @ files: list_like
                - Absolute Paths of all local files that need to be uploaded
            @ new_folder: boolean (default is False)
                - Decide whether to create a new subfolder
                - NOTE: This function only considers level2 folders structure
                - which means parent_folder --> new_sub_folder
            @ show_info: boolean (default is True)
                - Decide whether to print outputs
            @ kwargs: dict_like (optional)
                - If you choose new_folder = True
                - Should pass another parameter into kwargs as the new subfolder's name

        Returns:
            None
        ------------------------------------------------------------------------------------------
        """

        self.upload_to = 'https://drive.google.com/drive/u/0/folders/{0}'.format(gdrive_folder_id)
        service = build('drive', 'v3', credentials = self.creds)

        if new_folder == True:
            if 'folder_name' in kwargs.keys():
                folder_name = kwargs['folder_name']
            else:
                folder_name = kwargs[list(kwargs.keys())[0]]

            folder_meta_data = {'name': str(folder_name), 
                                'mimeType': 'application/vnd.google-apps.folder', 
                                'parents': [gdrive_folder_id]}

            folder_object = service.files().create(body = folder_meta_data, fields = 'id').execute()
            folder_id = folder_object['id']
        else:
            folder_id = gdrive_folder_id

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
            file = service.files().create(
                                        body = file_meta_data,
                                        media_body = media,
                                        fields = 'id'
                                        ).execute()
            self.uploaded_files.append(filename)
        
        if show_info == True:
            print("----- AUTO UPLOAD")
            print("* Upload Files To Gdrive: {0}".format(self.upload_to))
            print("* Create New Folder Option: {0}".format("True\n* New Folder Name: {0}".format(folder_name) if new_folder == True else "False"))
            print("* Uploaded {0} Files:\n\t{1}".format(len(self.uploaded_files), self.uploaded_files))
        else:
            pass

        # self.log.append({"upload_to": self.upload_to, "uploaded_files": self.uploaded_files})
    

    def download(self,
        gdrive_folder_id,
        download_folder,
        match_keys,
        required_key="",
        show_info=True
    ):
        """
        ------------------------------------------------------------------------------------------
        Parameters:
            @ gdrive_folder_id: str_like
                - The GDrive Folder ID
                - Need to download files from it
            @ download_folder:
                - The folder path which need to save downloaded files
            @ match_keys: list_like
                - Download files which filename includes one of the matching keys
            @ required_key (default is "")
                - Required key which is included in filenames
            @ show_info: boolean (default is True)
                - Decide whether to print outputs

        Returns:
            None
        ------------------------------------------------------------------------------------------
        """
        
        service = build('drive', 'v3', credentials = self.creds)
        self.download_from = "https://drive.google.com/drive/u/0/folders/{0}".format(gdrive_folder_id)

        search_query = "'{0}' in parents".format(gdrive_folder_id)
        listed_response = service.files().list(q = search_query).execute()
        listed_files = listed_response["files"]
        matched_files = []
        for gdrive_file in listed_files:
            file_id = gdrive_file["id"]
            filename = gdrive_file["name"]

            for match_key in match_keys:
                if required_key in filename and match_key in filename:
                    matched_files.append(filename)
                    request = service.files().get_media(fileId = file_id)
            
                    # Method I
                    with open(os.path.join(download_folder, filename), 'wb') as f:
                        downloader = MediaIoBaseDownload(f, request)
                        done = False
                        while done is False:
                            status, done = downloader.next_chunk()

                    self.downloaded_files.append(filename)

                    # Method II
                    # fh = io.BytesIO(request.execute())
                    # with io.open(os.path.join(download_folder, filename), 'wb') as f:
                    #     fh.seek(0)
                    #     f.write(fh.read())
                    # print("Downloaded {0}".format(gdriveFileName))

                else:
                    pass

        if show_info == True:
            print("")
            print("----- AUTO DOWNLOAD")
            print("* Downloade Gdrive Files From: {0}".format(self.download_from))
            print("* Matching Keys: {0} & {1}".format(match_keys, required_key))
            print("* Matched {0} Files:\n\t{1}".format(len(matched_files), matched_files))
            print("* Downloaded {0} Files:\n\t{1}".format(len(self.downloaded_files), self.downloaded_files))
        else:
            pass
        
        # self.log.append({"download_from": self.download_from, "downloaded_files": self.downloaded_files})

# Test
if __name__ == "__main__":
    today = datetime.datetime.today().strftime('%F')

    root_path = os.path.dirname(os.path.abspath(__file__))
    credential_folder = "/Users/xu.zhu/Desktop/Data/Keys/GoogleAPI/credentials"
    gdrive_credential_path = os.path.join(credential_folder, "Gdrive_py3_credentials.json")
    gdrive_token_path = os.path.join(credential_folder, "Gdrive_py3_token.pickle")

    folder = '/Users/xu.zhu/Desktop/Test/GoogleAPI_Test'

    gdrive_object = GdriveAPI(credential_path = gdrive_credential_path,
                            token_path = gdrive_token_path)
    gdrive_folder_id = "1HY79S20FC3xC3GMhPM1VmVMG0XRVpXA0"
    match_keys = ["2"]
    required_key = "Test"

    gdrive_object.download(gdrive_folder_id = gdrive_folder_id,
                           download_folder = folder,
                           match_keys = match_keys,
                           required_key = required_key
                           )
