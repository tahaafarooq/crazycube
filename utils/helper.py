from random import randint
import requests


class SMS:
    def __init__(self, username, api_key, msisdn):
        self.username = username
        self.api_key = api_key
        self.msisdn = msisdn

    def generate_otp(self):
        otp = randint(11111, 99999)
        return otp

    def send_otp(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "apiKey": "23cae3551a66a8f2b4d7d10cd389817d9595b0206f19d21a1e1a3db5b70c4afb"
        }
        data = {
            "username": "sandbox",
            "to": self.msisdn,
            "message": f"Here is your OTP : {self.generate_otp()}",
            "from": "83213"
        }

        req = requests.post('https://api.sandbox.africastalking.com/version1/messaging', headers=headers, data=data)
        # print(req.status_code)
        # print(req.text)

        return req.text
