from vehicle_type import VehicleType
from spot_type import SpotType
class Vehicle:
    def __init__(self, vehicle_type, plate):
        self._type = vehicle_type
        self.plate = plate
    def get_type(self):
        return self._type
    def get_plate(self):
        return self.plate
    def find_spot(self):
        if self._type == VehicleType.BIKE:
            return SpotType.SMALL
        elif self._type == VehicleType.CAR:
            return SpotType.MEDIUM
        elif self._type == VehicleType.TRUCK:
            return SpotType.LARGE