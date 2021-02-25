import sys
import os

import requests

import numpy as np
import pandas as pd

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
try:
    from email.MIMEBase import MIMEBase # python2
except:
    from email.mime.base import MIMEBase # python3


def read_data(filepath, show_info=True):
    msg = ["\n{0} {1}".format("-"*5, "READ DATA")]

    file_name = os.path.basename(filepath)
    file_type = file_name.split(".")[-1]
    msg.append("- Target File: {0}".format(file_name))

    if file_type == "csv":
        df = pd.read_csv(filepath, encoding="utf-8-sig")
    elif file_type == "xlsx":
        df = pd.read_excel(filepath, encoding="utf-8-sig")
    else:
        msg.append("- Do not support this file type '{0}'".format(file_type))
        pass #TBC

    msg.append("- Row Number: {0}".format(df.shape[0]))
    if show_info == True:
        print("\n".join(msg))
        print("- The template shows as below:\n", df.head(2))
    else:
        pass

    return df
    

def send_email(
        recipients,
        subject,
        text,
        sender,
        password,
        attachments=[]
    ): 

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(text))

    for file in attachments: # get all attachments
        filename = file.split("/")[-1]
        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(file, 'rb').read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename='%s'" % filename)
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(sender, password) # change it if you change the sender address
    mailServer.sendmail(sender, recipients, msg.as_string())
    mailServer.close()


def create_folder(folder_paths, clear_option=False, show_info=True):
    msg = []

    if type(folder_paths) == str:
        folder_paths = [folder_paths]
    elif type(folder_paths) == list:
        pass
    
    for folder_path in folder_paths:
        if os.path.exists(folder_path) == False:
            os.mkdir(folder_path)
            msg.append("- Created New Folder: {0}".format(folder_path))
        else:
            msg.append('- The Folder Existed Already: {0}'.format(folder_path))
            if clear_option == False:
                pass
            else:
                msg.append("- Clear Option: True\n\t- Cleaning...")
                filenames = os.listdir(folder_path)
                for filename in filenames:
                    os.remove(os.path.join(folder_path, filename))
                    msg.append("\t- Deleted File: {0}".format(filename))
                msg.append("\t= Cleared")
    
    if show_info == True:
        print("\n".join(msg))
    else:
        pass


def combine_files(filepaths, cols="all", show_info=True):
    conbined_df = pd.DataFrame()

    total_files = len(filepaths)
    error_files = []
    count = 0
    for filepath in filepaths:
        try:
            filetype = filepath.split("/")[-1].split(".")[-1]
            if filetype == "xlsx":
                single_df = pd.read_excel(filepath, encoding="utf-8-sig")
            elif filetype == "csv":
                single_df = pd.read_csv(filepath, encoding="utf-8-sig")
            else:
                pass #TBC
            
            if cols == "all":
                pass
            else:
                single_df = single_df[cols]

            conbined_df = pd.concat([conbined_df, single_df], ignore_index=True)
            count += 1

        except:
            error_files.append(filepath)

    if show_info == True:
        print("\n----- Combine Files")
        print("* In Total {0} Files".format(total_files))
        print("* Combined {0} Files".format(count))
        print("* Error Files: {0}\n\t{1}\n".format(len(error_files), error_files))
    else:
        pass
    
    return conbined_df


def ingest_csv(filepath, job_key, token):
    api_endpoint = "https://data-ingestion.idata.shopeemobile.com/api/csv/upload/file/{0}".format(job_key)
    headers = {"data-ingestion-token": token}
    response = requests.post(api_endpoint,
                             headers=headers,
                             files={"file": open(filepath, "rb")}
                             )
    return response