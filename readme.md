# Upload File to Google Drive

Ability to upload file to google drive by using google api and PyDrive

## SETUP DEVELOPMENT ENVIRONMENT
Goto Google Support page to Google API.  Follow this link https://support.google.com/googleapi/answer/6158841?hl=en
Which will have instruction to generate client_secerts.json.  When creating "**Create OAuth client ID**" do click on 
"**other**" and give a name.

## GETTING STARTED

#### PRE-REQUISITES

Install Python 3.6
pip install pydrive
pip install pytest
ppip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## COMMANDS

At the command line issue this command to run the program see below.  After the filename you have to enter in filename 
with a space then enter the folder patch.  Example of the ID folder path:

  https://drive.google.com/drive/folders/**1Z3dg1jkabN8QwzY0h0nXMIKzIrnuD9rX**

  > python run_upload.py ./files/hqdefault.jpg 1Z3dg1jkabN8QwzY0h0nXMIKzIrnuD9rX

To run the test cases run this command:

  > pytest -v test_cases.py

