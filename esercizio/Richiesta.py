from abc import ABC, abstractmethod
class Richiesta(ABC):
    @abstractmethod
    def request(self, servizio):
        pass

