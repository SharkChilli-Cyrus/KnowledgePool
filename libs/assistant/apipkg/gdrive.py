# coding=utf-8
#
# Here only considering csv and xlsx 2 formats
# More MIME Types Refer: https://developers.google.com/drive/api/v3/ref-export-formats
#
# @author: Zhu Xu
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
            pass
        else:
            print("[WARNING] Get Google Drive Credentials FAILED!")


    def create_folder(self,
        parent_folder_id,
        folder_name
    ):
        service = build("drive", "v3", credentials=self.creds, cache_discovery=False)

        folder_meta_data = {
            "name": folder_name, 
            "mimeType": "application/vnd.google-apps.folder", 
            "parents": [parent_folder_id]
        }
        response = service.files().create(body=folder_meta_data, fields="id").execute()
        return response


    def upload(self,
        filepaths,
        folder_id,
        new_folder=False,
        show_info=True,
        **kwargs
    ):
        """
        ------------------------------------------------------------------------------------------
        Parameters:
            @ folder_id: str_like
                - The GDrive Folder ID
                - Need to upload files into it
                - or create a new sub folder in it
            @ filepaths: list_like
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
            response_info
        ------------------------------------------------------------------------------------------
        """
        service = build("drive", "v3", credentials=self.creds, cache_discovery=False)

        response_info = {
            "upload_to": "",

        }
        response_info["upload_to"] = "https://drive.google.com/drive/u/0/folders/{0}".format(folder_id)

        if new_folder == True:
            if "folder_name" in kwargs.keys():
                folder_name = kwargs["folder_name"]
            else:
                folder_name = kwargs[list(kwargs.keys())[0]]

            # folder_meta_data = {"name": str(folder_name), 
            #                     "mimeType": "application/vnd.google-apps.folder", 
            #                     "parents": [folder_id]}

            # new_folder_response = service.files().create(body = folder_meta_data, fields = "id").execute()
            # new_folder_id = new_folder_response["id"]

        else:
            folder_id = gdrive_folder_id

        for file_path in files:
            filename = file_path.split("/")[-1]
            file_meta_data = {"name": filename, "parents": [folder_id]}

            # Here only considering csv and xlsx 2 formats
            # More MIME Types Refer: https://developers.google.com/drive/api/v3/ref-export-formats
            file_format = filename.split(".")[-1]
            if file_format == "csv":
                upload_type = "text/csv"
            elif file_format == "xlsx":
                upload_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
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
            print("-- AUTO UPLOAD")
            print("+ Upload Files To Gdrive: {0}".format(self.upload_to))
            print("+ Create New Folder Option: {0}".format("True\n* New Folder Name: {0}".format(folder_name) if new_folder == True else "False"))
            print("+ Uploaded {0} Files:\n\t{1}".format(len(self.uploaded_files), "\n\t".join(self.uploaded_files)))
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
        
        service = build('drive', 'v3', credentials=self.creds, cache_discovery=False)
        self.download_from = "https://drive.google.com/drive/u/0/folders/{0}".format(gdrive_folder_id)

        search_query = "'{0}' in parents and trashed = false".format(gdrive_folder_id)
        listed_response = service.files().list(q = search_query).execute()
        listed_files_raw = listed_response["files"]
        listed_files = [i for i in listed_files_raw if i["mimeType"].split(".")[-1] != "folder"]
        matched_files = []

        if match_keys == "":
            for gdrive_file in listed_files:
                file_id = gdrive_file["id"]
                filename = gdrive_file["name"]

                if required_key in filename:
                    matched_files.append(filename)
                    request = service.files().get_media(fileId = file_id)

                    # Method I
                    with open(os.path.join(download_folder, filename), 'wb') as f:
                        downloader = MediaIoBaseDownload(f, request)
                        done = False
                        while done is False:
                            status, done = downloader.next_chunk()

                    self.downloaded_files.append(filename)

        elif type(match_keys) is str:
            for gdrive_file in listed_files:
                file_id = gdrive_file["id"]
                filename = gdrive_file["name"]

                if required_key in filename and match_keys in filename:
                    matched_files.append(filename)
                    request = service.files().get_media(fileId = file_id)

                    # Method I
                    with open(os.path.join(download_folder, filename), 'wb') as f:
                        downloader = MediaIoBaseDownload(f, request)
                        done = False
                        while done is False:
                            status, done = downloader.next_chunk()

                    self.downloaded_files.append(filename)

        else: # list-like
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
            
        if show_info == True:
            print("-- AUTO DOWNLOAD")
            print("+ Downloaded Gdrive Files From: {0}".format(self.download_from))
            if match_keys == "" and required_key == "":
                print("+ Downloaded All Files")
            elif required_key == "":
                print("+ Matching Keys: {0}".format(match_keys))
            else:
                print("+ Matching Keys: {0} & {1}".format(match_keys, required_key))
            print("+ Matched {0} Files:\n\t{1}".format(len(matched_files), matched_files))
            print("+ Downloaded {0} Files:\n\t{1}".format(len(self.downloaded_files), "\n\t".join(self.downloaded_files)))
        else:
            pass
        
        # self.log.append({"download_from": self.download_from, "downloaded_files": self.downloaded_files})


    def clean(self,
        gdrive_folder_id,
        match_keys="",
        show_info=True
    ):

        service = build('drive', 'v3', credentials=self.creds, cache_discovery=False)
        self.target_folder = "https://drive.google.com/drive/u/0/folders/{0}".format(gdrive_folder_id)

        search_query = "'{0}' in parents and trashed = false".format(gdrive_folder_id)
        listed_response = service.files().list(q=search_query).execute()
        listed_files_raw = listed_response["files"]
        listed_files = [i for i in listed_files_raw if i["mimeType"].split(".")[-1] != "folder"]
        matched_files = []

        if match_keys == "":
            for gdrive_file in listed_files:
                file_id = gdrive_file["id"]
                filename = gdrive_file["name"]

                service.files().delete(fileId=file_id).execute()
                matched_files.append(filename)
        else:
            pass #TODO
            

        if show_info == True:
            print("++ AUTO CLEAN UP")
            print("+ Target Google Drive Folder: {0}".format(self.target_folder))
            if match_keys != "":
                print("* Match Key: {0}".format(match_keys))
            print("+ Deleted {0} Files:\n\t{1}".format(len(matched_files), matched_files))
        else:
            pass
    

    def archive(self,
        gdrive_folder_id,
        show_info=True
    ):
        info = ["\n===== ARCHIVE FILES"]
        service = build('drive', 'v3', credentials=self.creds, cache_discovery=False)

        def move(listed_files, new_folder_id):
            count = 0
            for drive_file in listed_files:
                file_name = drive_file["name"]
                file_id = drive_file["id"]
                previous_parents = gdrive_folder_id

                file_info = service.files().update(
                    fileId=file_id,
                    addParents=new_folder_id,
                    removeParents=previous_parents,
                    fields="id, parents"
                ).execute()
                
                count += 1
                info.append("\t- {0}".format(file_name))

            info.append("* Archived {0} files".format(count))
            return info

        
        self.target_folder = "https://drive.google.com/drive/u/0/folders/{0}".format(gdrive_folder_id)
        info.append("* Target Folder: {0}".format(self.target_folder))

        search_query = "'{0}' in parents and trashed = false".format(gdrive_folder_id)
        listed_response = service.files().list(q=search_query).execute()
        listed_files_raw = listed_response["files"]

        listed_files = [i for i in listed_files_raw if i["mimeType"].split(".")[-1] != "folder"]
        archived_folders = [i for i in listed_files_raw if i["mimeType"].split(".")[-1] == "folder" and i["name"].lower()=="archived"]

        if len(archived_folders) > 0:
            archived_folder = archived_folders[0]
            archived_folder_id = archived_folder["id"]
            move(listed_files, archived_folder_id)
        
        else:
            folder_metadata = {
                "name": "Archived",
                "mimeType": "application/vnd.google-apps.folder",
                "parents": [gdrive_folder_id]
            }
            archived_folder = service.files().create(
                body=folder_metadata,
                fields="id").execute()
            archived_folder_id = archived_folder.get("id")
            move(listed_files, archived_folder_id)
        
        if show_info==True:
            print("\n".join(info))
        else:
            pass