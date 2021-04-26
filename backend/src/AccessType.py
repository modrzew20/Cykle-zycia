from abc import ABC


class AccessType(ABC):
    def __init__(self):
        pass


class Exclusive(AccessType):
    def __init__(self):
        self.swimmingPool = True
        self.buffet = True
        self.sauna = True
        self.gym = True
        self.beachbar = True
        super().__init__()


class VIP(AccessType):
    def __init__(self):
        self.swimmingPool = True
        self.buffet = True
        self.sauna = False
        self.gym = True
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
