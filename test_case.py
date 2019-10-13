import slash
import slash.log

from libs.file_upload import file_upload


def test_upload_status():
    r = file_upload()
    slash.logger.info(f'Return status is [{r.status_code}]')
    assert r.status_code == 200
