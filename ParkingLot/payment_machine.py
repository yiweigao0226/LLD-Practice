class PaymentMachine:
    def __init__(self, price):
        self.hourly_price = price
    def get_hourlyPrice(self):
        return self.hourly_price
    def calculate_total(self, time):
        if time > int(time):
            time = int(time) + 1
        return self.hourly_price * time