import sys
import os

sys.path.append("/Users/xu.zhu/Desktop/KnowledgePool/1_Python/lib/GoogleAPI/")
from GoogleDriveAPI import GdriveAPI

if __name__ == "__main__":
    credentials_folder = "/Users/xu.zhu/Desktop/Data/Keys/GoogleAPI/credentials/"
    gdrive_credential_path = os.path.join(credentials_folder, "Gdrive_py3_credentials.json")
    gdrive_token_path = os.path.join(credentials_folder, "Gdrive_py3_token.pickle")

    gdrive_object = GdriveAPI(credential_path=gdrive_credential_path,
                              token_path=gdrive_token_path)