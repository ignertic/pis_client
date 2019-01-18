import logging
import time




data = '{"ErrorCode":"000","ErrorMessage":"Done","JobId":"20047","MessageData":[{"Number":"91989xxxxxxx","MessageId":"mvHdpSyS7UOs9hjxixQLvw"},{"Number":"917405080952","MessageId":"PfivClgH20iG6G5R3usHwA"}]}'

class DataParse(object):
    """docstring for DataParse."""
    def __init__(self):
        super(DataParse, self).__init__()
        self.arg = 'lol'
        self.fdata =[]
        # self.data = eval(data)

    def __get_status_codes(self):
        try:
            status_code = self.data['ErrorCode']
            status = self.data['ErrorMessage']
            return {status_code, status}
        except KeyError:
            logging.error("Invalid Data")
            return None

    def _extract_sms_data(self,data, **kwargs):
        sms_data = {}
        self.data = eval(data)
        try:
            sms_data['status'] = self._get_status_codes()
            sms_data['phone_numbers'] = [i["Number"] for i in self.data["MessageData"]]
            sms_data['message_id'] = [i['MessageId'] for i in self.data["MessageData"]]
            sms_data['flash_sms'] = False if kwargs.get("flash_sms") is None else True
            sms_data['date'] = time.time()
            sms_data['job_id'] = self.data['JobId']
            sms_data['scheduled'] = False if kwargs.get("sched") is None else True
            return sms_data
        except KeyError:
            loggin.error("Invalid Data")
            return sms_data

    def __extract_delivery_data(self, data):
        d_data = {}
        self.data = data

        try:
            d_data['status'] = self.__get_status_codes()
            for message_id, delivery_status, delivery_date in self.data['DeliveryReports'].items():
                d_data['reports'][delivery_date] = {"delivered" : True if delivery_status == "Delivered" else False, "mid" : message_id}

            return d_data
        except KeyError:
            logging.error("Invalid data")
            return None

    def __extract_balance(self, data):
        b_data = {}
        self.data = eval(data)

        try:
            b_data['status'] = self.__get_status_codes()
            b_data['balance'] = self.data['Balance']
            return b_data
        except KeyError:
            loggin.error("Invalid data")
            return None
    
