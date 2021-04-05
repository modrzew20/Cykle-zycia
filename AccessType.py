from abc import ABC


class AccessType(ABC):
    def __init__(self):
        pass

class Exclusive(AccessType):
    def __init__(self):
        self.swimmingPool = False
        self.buffet = False
        self.sauna = False
        self.gym = False
        self.beachbar = False
        super().__init__()


class VIP(AccessType):
    def __init__(self):
        self.swimmingPool = False
        self.buffet = False
        self.sauna = False
        self.gym = False
        self.beachbar = False
        super().__init__()


class Standard(AccessType):
    def __init__(self):
        self.swimmingPool = False
        self.buffet = False
        self.sauna = False
        self.gym = False
        self.beachbar = False
        super().__init__()