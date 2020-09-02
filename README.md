# Patient API

Patient Information System

Requirements:
  Python 3

Installation:

>  pip install pis_client

Usage
```python

from pis_client import Client

client = Client("KEY", server="http://149.28.192.223:8000")
records = client.get_medical_records()
for record in records:
    print(record['patient_name'])

record_id = 1
# get record object by id
record = client.get_medical_record(record_id)
# get pdf document
client.get_card(record['id'], "/home/user/Desktop")



```
