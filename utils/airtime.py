import africastalking


class Airtime:
    def __init__(self, username, api_key, msisdn, amount):
        self.username = username
        self.api_key = api_key
        self.msisdn = msisdn
        self.amount = amount

    def send_air(self):
        africastalking.initialize(username=self.username, api_key=self.api_key)

        airtime = africastalking.Airtime

        msisdn = self.msisdn
        currency = "TZS"
        amount = self.amount

        try:
            response = airtime.send(phone_number=msisdn, amount=amount, currency_code=currency)
            return response
        except Exception as e:
            return f"There was an error sending airtime {e}"

