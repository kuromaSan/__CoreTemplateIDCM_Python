from .L01_Variable import NameConfig
from .L02_Function import NamePolicy

class NameModel:
    def __init__(self, name_config: NameConfig, name_policy: NamePolicy):
        self.name_config = name_config
        self.name_policy = name_policy

    def Model(self):
        pass