from abc import ABC


class ClientType(ABC):
    def __init__(self):
        pass


class Default(ClientType):
    def __init__(self):
        self.discount = 0.0
        super().__init__()


class Silver(ClientType):
    def __init__(self):
        self.discount = 0.1
        super().__init__()


class Gold(ClientType):
    def __init__(self):
        self.discount = 0.2
        super().__init__()


class Platinum(ClientType):
    def __init__(self):
        self.discount = 0.3
        super().__init__()
