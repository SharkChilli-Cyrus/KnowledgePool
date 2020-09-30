# coding=utf-8
#
# @author: Zhu Xu
# @date: 2020-09-24
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

class GsheetAPI(object):
    """
    Call Google Sheet API - v4
    """

    def __init__(self, credential_path, token_path):
        self.credential_path = credential_path
        self.token_path = token_path
        self.scopes = None
        self.creds = None

        self.update_to = None
        self.read_from = None


    def get_creds(self, sheet_scopes = ['https://www.googleapis.com/auth/spreadsheets']):
        self.scopes = sheet_scopes

        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credential_path, self.scopes)
                self.creds = flow.run_local_server()

            with open(self.token_path, 'wb') as token:
                pickle.dump(self.creds, token)
            
        if self.creds:
            print("* Got Google Sheet API Credentials")
        else:
            print("x Get Google Sheet Credentials FAIL!")

        
    def read(self, sheet_id, sheet_range, 
        read_type = 'DataFrame', show_info = True):
        """
        ------------------------------------------------------------------------------------------
        Parameters
        
        Returns:
        ------------------------------------------------------------------------------------------
        """

        self.read_from = 'https://docs.google.com/spreadsheets/d/{0}'.format(sheet_id)

        service = build('sheets', 'v4', credentials = self.creds)
        sheet_object = service.spreadsheets()
        request = sheet_object.values().get(spreadsheetId = sheet_id, range = sheet_range)
        response = request.execute()
        values = response['values']

        if read_type.lower() == 'list':
            # result = [value[0] for value in values if value != []]
            result = []
            for value in values:
                if value == []:
                    continue
                else:
                    result.append(value[0])

        elif read_type.lower() == 'string':
            py_version = int(sys.version_info[0])
            if py_version == 2:
                result_temp = [str(value[0]).encode('utf-8') for value in values if value != []]
            else:
                result_temp = [str(value[0]) for value in values if value != []]

            result_temp_v2 = ["'{0}'".format(_) for _ in result_temp]
            result = "(" + ",".join(result_temp_v2) + ")"

        else:
            cols = values.pop(0)
            result = pd.DataFrame(data = values, columns = cols)

        if show_info == True:
            print("----- AUTO READ")
            print("* Read Data From: {0}".format(self.read_from))
            print("* Read Type: {0}".format(read_type.lower()))
            print("* Read Range: {0}".format(sheet_range))
        else:
            pass

        return result
    

    def update(self, sheet_id, sheet_range, data,
        update_type = "overwrite", show_info = True):

        self.update_to = "https://docs.google.com/spreadsheets/d/{0}".format(gsheetID)

        service = build('sheets', 'v4', credentials = self.creds)
        sheet_object = service.spreadsheets()

        if update_type.lower() == "overwrite":
            clear_body = {}
            clear_execute = sheet_object.values().clear(spreadsheetId = sheet_id,
                                                        range = sheet_range,
                                                        body = clear_body).execute()

            data = data.replace(np.nan, 'NA')
            update_body = {'values': data.values.tolist()}
            update_execute = sheet_object.values().update(spreadsheetId = sheet_id,
                                                        range = sheet_range,
                                                        valueInputOption = 'RAW',
                                                        body = update_body).execute()
        else:
            pass # TBC

        if show_info == True:
            print("----- AUTO UPDATE")
            print("* Update Data To: {0}".format(self.update_to))
            print("* Update Type: {0}".format(update_type).lower())
            print("* Update Range: {0}".format(sheet_range))
        else:
            pass