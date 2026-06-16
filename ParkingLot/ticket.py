class Ticket:
    def __init__(self, time, vehicle):
        self.enter_time = time
        self.vehicle = vehicle
        self.leave = False
    def get_enterTime(self):
        return self.enter_time
    def get_vehicle(self):
        return self.vehicle
    def is_leave(self):
        return self.leave
    def set_leave(self):
        self.leave = True