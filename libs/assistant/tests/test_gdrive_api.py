# coding=utf-8

import sys
import os

WORK_PATH = os.path.dirname(os.path.abspath(__file__))
PKG_PATH = os.path.dirname(WORK_PATH)

sys.path.append(PKG_PATH)
from apipkg.gdrive import GdriveAPI


CREDENTIAL_FOLDER = "/Users/xu.zhu/Desktop/Data/Keys/GoogleAPI/credentials"

if __name__ == "__main__":
    credential_path = os.path.join(CREDENTIAL_FOLDER, "Gdrive_py3_credentials.json")
    token_path = os.path.join(CREDENTIAL_FOLDER, "Gdrive_py3_token.pickle")
    test_folder_id = "1BDs58vWcxsDpqcZkTxULGQtXQSq22mcc"

    gdrive_object = GdriveAPI(
        credential_path=credential_path,
        token_path=token_path
    )

    