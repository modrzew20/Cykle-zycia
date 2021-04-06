from abc import ABC, abstractmethod


class Dao(ABC):
    @abstractmethod
    def write(self, obj):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def delete(self, Id):
        pass
