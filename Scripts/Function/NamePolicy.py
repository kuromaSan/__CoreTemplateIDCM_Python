from . import NameStrategy

class NamePolicy:
    def __init__(self, name_strategy: NameStrategy):
        self.name_strategy = name_strategy

    def add_name(self, name: str) -> bool:
        return self.name_strategy.add_name(name)

    def get_names(self) -> list:
        return self.name_strategy.get_names()

    def clear_names(self) -> None:
        self.name_strategy.clear_names()