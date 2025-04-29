import abc
from . import NameRepository

class INameRepository(abc.ABC):
    @abc.abstractmethod
    def add_name(self, name: str) -> bool:
        pass

    @abc.abstractmethod
    def get_names(self) -> list:
        pass

    @abc.abstractmethod
    def clear_names(self) -> None:
        pass