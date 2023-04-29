from random import randint
import africastalking


class SMS:
    def __init__(self, username, api_key, msisdn):
        self.username = username
        self.api_key = api_key
        self.msisdn = msisdn

    @staticmethod
    def generate_otp():
        otp = randint(11111, 99999)
        return otp

    def send_otp(self):
        africastalking.initialize(
            username=self.username,
            api_key=self.api_key
        )

        sms = africastalking.SMS

        msisdn = [self.msisdn]
        message = f"Hello {self.msisdn}, Your OTP is {self.generate_otp()}! Please Do Not Share!"
        sender = "INFORM"

        try:
            response = sms.send(message, msisdn, sender)
            return response
        except Exception as e:
            return f"There was an Error]n {e}"

    def send_withdraw(self, amount: int):
        africastalking.initialize(
            username=self.username,
            api_key=self.api_key
        )

        sms = africastalking.SMS

        msisdn = [self.msisdn]
        message = f"{self.msisdn}! You have withdrawn and received {amount} as airtime!"
        sender = "INFORM"

        try:
            response = sms.send(message, msisdn, sender)
            return response
        except Exception as e:
            return f"There was an Error\n {e}"
