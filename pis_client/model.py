import requests as rs
# from . import config
from pathlib import Path
import os
log =logger


class Client(object):

    def __init__(self, key, server="http://localhost:8000"):
        self.SERVER = server
        self.key = key
        self.client = rs.Session()

    def search_patient(self, patient_id):
        pass

    def get_medical_record(self, record_id):
        response = self.client.get(self.SERVER+f'/api/records/{record_id}')
        record = eval(response.content)
        return record

    def get_medical_records(self):
        response = self.client.get(self.SERVER+'/api/records')
        return eval(response.content)

    def get_card(self, record_id, path):
        # get patient card in pdf form
        response = self.client.get(self.SERVER+f'/generate_pdf/{record_id}')
        _file = Path(os.path.join(path, str(record_id)+".pdf"))
        _file.write_bytes(response.content)

        return path+f'{record_id}.pdf'
