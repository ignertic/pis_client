import logging
import time
import re
import enum
import requests
import ast
name = "bluedot"
data = '{"ErrorCode":"000","ErrorMessage":"Done","JobId":"20047","MessageData":[{"Number":"91989xxxxxxx","MessageId":"mvHdpSyS7UOs9hjxixQLvw"},{"Number":"917405080952","MessageId":"PfivClgH20iG6G5R3usHwA"}]}'



class DataParse(object):
    """docstring for DataParse."""
    def __init__(self):
        # super(DataParse, self).__init__()
        self.arg = 'lol'
        self.fdata =[]
        # self.data = ast.literal(data)

    def _get_status_codes(self):
        try:
            status_code = self.data['ErrorCode']
            status = self.data['ErrorMessage']
            return {status_code : status}
        except KeyError:
            logging.error("Invalid Data")
            return None

    def _extract_sms_data(self,data, **kwargs):
        sms_data = {}
        self.data = ast.literal(data)
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
            logging.error("Invalid Data")
            return sms_data

    def _extract_delivery_data(self, data):
        d_data = {}
        self.data = ast.literal(data.replace("null", '"null"'))

        try:
            d_data['status'] = self.__get_status_codes()
            for message_id, delivery_status, delivery_date in [i.items() for i in self.data['DeliveryReports']]:
                d_data[delivery_date[1]] = {"delivered" : True if delivery_status == "Delivered" else False, "mid" : message_id[1]}
            return d_data
        except KeyError as e:
            # print(e)
            return None

    def _extract_balance(self, data):
        b_data = dict()
        self.data = ast.literal(str(data))

        try:
            b_data['status'] = self.__get_status_codes()[1]
            b_data['balance'] = self.data['Balance']
            return b_data
        except KeyError as e:
            print(e)
            return None





















class Bluedot(DataParse):
    """Bluedot.


     -params
        *Username & Password
        *Profile load file

    //Tasks:
        -Obtain credentials
        -Check if valid by checking balance
        -Log successful login
        -Send msgs



    """

    BALANCE = None
    content = None
    error = None

    HOME = "http://127.0.0.1/"
    CHECK_BALANCE_URL = "http://www.bluedotsms.com/api/mt/GetBalance?User={username}&Password={password}"
    CHECK_DELIVERY_URL = HOME+"delivery"
    SEND_SMS_URL = "http://www.bluedotsms.com/api/mt/SendSMS?user={username}&password={password}&senderid={sender_id}&channel=Normal&DCS=0&flashsms={flash}&number={numbers}&text={text}"

    SEND_MULTIPLE_SMS_URL = HOME+"send_m"
    FLASH = 0
    SENDER = "SuperCode"


    def __init__(self, username, password, **kwargs):
        super(Bluedot, self).__init__()
        self.kwargs = kwargs
        self.password = password
        self.username = username
        self.requests = requests
        # print(self._extract_sms_data)
        # self.sender_name = if kwargs.get("sender_name") else "Bluedot"


    @staticmethod
    def __clean_number(contact):
        #remove symbols
        #approaching with this technique for learning purp
        if type(contact) is list:
            return [c.replace("+", "").strip() for c in contact]
        return contact.replace("+", "").strip()
    def _send_sms(self,msg,contacts):
        if type(contacts) is str:
            #Check number validity (NoB)
            contact = self.__clean_number(contacts)
            data =""# self.requests.get(SEND_SMS_URL.format(sender_id=SENDER, self.username=self.username,password=self.password,flash=FLASH))
            return self._extract_sms_data(data)
        elif type(contacts) is list:
            contacts = self.__clean_number(contacts)
            #send the sms
            numbers = ",".join(contacts)
            data = self.requests.get(SEND_SMS_URL.format(text=msg,numbers=numbers,username=self.username,password=self.password,flash=FLASH))
            return self._extract_sms_data(data)



    def test(self):
        # print self.__get_status_codes(data)
        pass
    def __date_transform(self, stamp):
        #return a datetime obj
        pattern = re.compile(r"d+/d+/d+") #bad practise of extracting dates with "re"
        res = pattern.search(stamp)
        y,m,d = [int(i) for i in res.group()]
        return datetime.date(y,m,d)
    def _schedule_sms(self,contacts, sms, to_send):
        #schedule sms
        #check if date is not previous
        if self.__date_transform(to_send) > datetime.date.today():
            req = self.requests.get(SEND_SMS_URL.format(username=self.username,password=self.password,flash=FLASH)+"schedtime="+to_send)
            return self._extract_sms_data(req.content)

        logging.error("Invalid date supplied")
        return None

    def _get_balance(self):
        # extract balance
        URL = self.CHECK_BALANCE_URL.format(username=self.username, password=self.password)


            #make rquest to API

        #try:
        req = self.requests.get(URL)
        data = self._extract_balance(req.content)
        print(req.content)
        #self.BALANCE = data['balance']
        return self._extract_balance(data)

        #except:
        #    logging.debug("Make sure you are connected")
        #    print("Error occured checking balance")










    def __repr__(self):
        return "<Bluedot 'class'>SuperCode"
    def __call__(self):
        return self.username

    def __len__(self):
        return balance

    def __getitem__(self, item):
        return self.test[item]

    def __str__(self):
        if self.username is None:
            return self.__class__.__name__






class client(Bluedot):
    """docstring for client."""
    def __init__(self, username, password):
        super(client, self).__init__(username, password)
        self.username = username
        self.password = password
    """
    //send sms
    //SEND_MULTIPLE_SMS
    //get balance
    //scehdule sms
    //deliery reports"""
    def send_sms(msg,contacts):
        #send text
        logging.info("SMS Sent")
        return self._send_sms(msg, contacts)
    def check_balance(self):
        return self._get_balance()
    def schedule_sms(msg, contacts, to_send):
        return self._schedule_sms(msg, contacts, to_send)
