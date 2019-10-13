# Upload File to Google Drive

Ability to upload file to google drive by using google api and PyDrive

## SETUP DEVELOPMENT ENVIRONMENT
Goto Google Support page to Google API.  Follow this link https://support.google.com/googleapi/answer/6158841?hl=en
Which will have instruction to generate client_secerts.json.  When creating "**Create OAuth client ID**" do click on 
"**other**" and give a name.

## GETTING STARTED

#### PRE-REQUISITES

1. Install Python 3.6
2. Pip install pydrive
3. Pip install pytest

## COMMANDS

At the command line issues these command to run the program:

python tso.py ./files/hqdefault.jpg 1Z3dg1jkabN8QwzY0h0nXMIKzIrnuD9rX

To run the test cases run this command:

pytest -v cli.py

