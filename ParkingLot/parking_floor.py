class ParkingFloor:
    def __init__(self, spots_available):
        self.spots_available = spots_available
    def get_spotAvailability(self, spot_type):
        return self.spots_available[spot_type]
    def decrease_spotAvailability(self, spot_type):
        self.spots_available[spot_type] -= 1
    def increase_spotAvailability(self, spot_type):
        self.spots_available[spot_type] += 1