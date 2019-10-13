from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from config import *

import os
import sys
import pprint


def get_cli():
    print('Count:', len(sys.argv))
    print('Type:', type(sys.argv))

    for arg in sys.argv:
        print('Argument:', arg)

    if len(sys.argv) != 3:
        print(f'Please enter two items.  First item is file location.  Second is URL')
        return False
    else:
        return sys.argv


def login_to_google():
    # Login to Google Drive and create drive object
    g_login = GoogleAuth()

    g_login.LoadCredentialsFile(MY_CARD)

    if g_login.credentials is None:
        # Authenticate if they're not there
        g_login.LocalWebserverAuth()
    elif g_login.access_token_expired:
        # Refresh them if expired
        g_login.Refresh()
    else:
        # Initialize the saved creds
        g_login.Authorize()
    # Save the current credentials to a file
    g_login.SaveCredentialsFile(MY_CARD)

    return GoogleDrive(g_login)


def upload(test_file: str = None, test_url: str = None):
    """
    Main driver to run the upload of the file to URL
    :param test_file: the file that will be used
    :param test_url: location of the URL
    :return: object
    """
    drive = login_to_google()
    failed = {}

    if test_url is None:
        test_url = FOLDER_ID

    if not test_file:
        arg = get_cli()
        if arg:
            test_file = arg[1]
            test_url = arg[2]
        else:
            failed['status_code'] = 403
            return failed

    try:
        with open(test_file, "r") as f:
            fn = os.path.basename(f.name)
            file_object = drive.CreateFile({'title': fn, "parents": [{"kind": "drive#fileLink", 'id': test_url}]})
    except Exception as e:
        print(e)
        failed['status_code'] = 404
        return failed

    try:
        file_object.SetContentFile(test_file)
        file_object.Upload()  # Upload file.

        # Print the return value for debug purposes
        file_object['status_code'] = 200
        pprint.pprint(file_object.metadata)
    except Exception as e:
        failed['status_code'] = 404
        print(e)
        return failed

    return file_object


if __name__ == '__main__':
    upload()
