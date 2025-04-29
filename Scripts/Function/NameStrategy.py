from . import INameRepository

class NameStrategy:
    def __init__(self, name_repository: INameRepository):
        self.name_repository = name_repository

    def add_name(self, name: str) -> bool:
        return self.name_repository.add_name(name)

    def get_names(self) -> list:
        return self.name_repository.get_names()

    def clear_names(self) -> None:
        self.name_repository.clear_names()