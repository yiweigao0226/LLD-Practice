from parking_floor import ParkingFloor
from spot_type import SpotType
from payment_machine import PaymentMachine
from parking_lot import ParkingLot
from vehicle import Vehicle
from vehicle_type import VehicleType
class main:
    def main():
        floor1 = ParkingFloor({
            SpotType.SMALL: 2,
            SpotType.MEDIUM: 3,
            SpotType.LARGE: 1
        })
        floor2 = ParkingFloor({
            SpotType.SMALL: 4,
            SpotType.MEDIUM: 4,
            SpotType.LARGE: 2
        })
        payment_machine = PaymentMachine(5)
        parking_lot = ParkingLot()
        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)
        parking_lot.add_paymentMachine(payment_machine)

        car1 = Vehicle(VehicleType.CAR, "ABC1122")
        bike1 = Vehicle(VehicleType.BIKE, "AACC13")
        truck1 = Vehicle(VehicleType.TRUCK, "1234567")
        car2 = Vehicle(VehicleType.CAR, "AAA1111")

        parking_lot.park_vehicle(car1)
        parking_lot.park_vehicle(bike1)
        parking_lot.park_vehicle(truck1)
        parking_lot.park_vehicle(car2)

        parking_lot.unpark_vehicle(car1)

    if __name__ == "__main__":
        main()