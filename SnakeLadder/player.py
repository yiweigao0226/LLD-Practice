class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1
    def get_name(self):
        return self.name
    def get_position(self):
        return self.position
    def set_position(self, position):
        self.position = position