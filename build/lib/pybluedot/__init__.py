name = "bluedot"
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

    balance = None
    content = None
    error = None

    def __init__(self, **kwargs):
        super(Bluedot, self).__init__()
        self.kwargs = kwargs
        self.password = kwargs.get("password")
        self.username = kwargs.get("username")
        print(self._extract_sms_data)
        # self.sender_name = if kwargs.get("sender_name") else "Bluedot"


    @staticmethod
    def __clean_number(contact):
        #remove symbols
        return contact.replace("+", "").strip()
    def send_sms(self,msg,contacts):
        if type(contacts) is str:
            #Check number validity (NoB)
            contact = self.__clean_number(contacts)
    def test(self):
        # print self.__get_status_codes(data)
        pass


    def __dir__(self):
        return [i for i in dir(self) if i[0] is not '_']
    def __repr__(self):
        return "SuperCode"
    def __call__(self):
        return self.username

    def __len__(self):
        return len(self.username)

    def __getitem__(self, item):
        return self.test[item]

    def __str__(self):
        if self.username is None:
            return self.__class__.__name__
