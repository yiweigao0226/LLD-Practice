from payment_machine import PaymentMachine
from ticket import Ticket
from datetime import datetime

class ParkingLot:
    def __init__(self):
        self.floors = []
        self.payment = None
        self.active_tickets = {}
    def add_floor(self, floor):
        self.floors.append(floor)
    def add_paymentMachine(self, payment_machine):
        self.payment = payment_machine
    def park_vehicle(self, vehicle):
        spot_type = vehicle.find_spot()
        for floor in self.floors:
            if floor.get_spotAvailability(spot_type) != 0:
                ticket = Ticket(datetime.now(), vehicle)
                self.active_tickets[vehicle.get_plate()] = (ticket, floor)
                print(f"Vehicle {vehicle.get_plate()} entered!")
                return ticket
        print("No available spots")
        return None
    def unpark_vehicle(self, vehicle):
        plate = vehicle.get_plate()
        spot_type = vehicle.find_spot()
        ticket, floor = self.active_tickets[vehicle.get_plate()]
        parked_hour = (datetime.now() - ticket.get_enterTime()).total_seconds() / 3600
        total = self.payment.calculate_total(parked_hour)
        floor.increase_spotAvailability(spot_type)
        ticket.set_leave()
        del self.active_tickets[plate]
        print(f"Vehicle {plate} exited")
        print(f"Total payment: {total}")
    def get_ticket(self, vehicle):
        plate = vehicle.get_plate()
        return self.active_tickets.get(plate)  # returns None if not parked
