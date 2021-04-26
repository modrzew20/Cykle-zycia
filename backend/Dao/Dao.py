from abc import ABC, abstractmethod


class Dao(ABC):
    # writes one object to database
    @abstractmethod
    def write(self, obj):
        pass

    # reads all objects from database
    @abstractmethod
    def read(self):
        pass

    # deleted one record or object from database by Id
    @abstractmethod
    def delete(self, Id):
        pass

    # reads one object or record from database by Id
    @abstractmethod
    def readOne(self, Id):
        pass

