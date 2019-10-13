import pytest
import hashlib
import os
from lib.run_upload import upload
from resource.resource_file import *


def __upload(filename: str = None, url: str = None):
    """
    Private method to upload the file and the url location
    :param filename: name of the file
    :param url: url of the location
    :return: dictionary of the object returned back from the upload
    """
    return upload(filename, url)


@pytest.mark.parametrize('filename', file_list, ids=[f"file_location {file['file_name']}" for file in file_list])
def test_mimetype(filename):
    """
    Loop through the list to check to match up with the mimetype
    :param filename: dictionary
    :return:
    """
    r = __upload(filename['file_name'])

    assert filename['mimetype'] == r['mimeType']


@pytest.mark.parametrize('filename', file_list, ids=[f"file_location {file['file_name']}" for file in file_list])
def test_filename(filename):
    """
    Loop through the list to check the file name matches
    :param filename: dictionary
    :return:
    """
    r = __upload(filename['file_name'])
    with open(filename['file_name'], "r") as f:
        fn = os.path.basename(f.name)

    assert fn == r['title']


@pytest.mark.parametrize('filename', file_list, ids=[f"file_location {file['file_name']}" for file in file_list])
def test_url(filename):
    """
    Loop through the list to check the file name matches
    :param filename: dictionary
    :return:
    """
    r = __upload(filename['file_name'], valid_url)

    assert 200 == r['status_code']


@pytest.mark.parametrize('filename', file_list, ids=[f"file_location {file['file_name']}" for file in file_list])
def test_checksum(filename):
    """
    Loop through the list to check the checksum matches
    :param filename: dictionary
    :return:
    """
    r = __upload(filename['file_name'])

    checksum = hashlib.md5(open(filename['file_name'], 'rb').read()).hexdigest()

    assert checksum == r['md5Checksum']


@pytest.mark.parametrize('filename', file_list, ids=[f"file_location {file['file_name']}" for file in file_list])
def test_status_code(filename):
    """
    Loop through the list to check the status of 200
    :param filename: dictionary
    :return:
    """
    r = __upload(filename['file_name'])
    assert 200 == r['status_code']


def test_invalid_no_file():
    """
    Negative test for file name is incorrect or none
    """
    r = __upload(invalid_file)
    assert 404 == r['status_code']


def test_no_file():
    """
    Negative test for no file
    """
    r = __upload('')
    assert 404 == r['status_code']


def test_invalid_url():
    """
    Negative test for invalid url
    :return:
    """
    r = __upload(file_png, invalid_url)
    assert 404 == r['status_code']


def test_empty_url():
    """
    Negative test for invalid url
    :return:
    """
    r = __upload(file_png, '')
    assert 404 == r['status_code']
