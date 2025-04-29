from .L01_Variable import NameConfig
from .L01_Variable import NameBuilder
from .L02_Function import NamePolicy

class NameCrafter:
    def __init__(self, name_config: NameConfig, name_builder: NameBuilder, name_policy: NamePolicy):
        self.name_config = name_config
        self.name_builder = name_builder
        self.name_policy = name_policy

    def Craft(self):
        # Use the name_config, name_builder, and name_policy to create a name
        pass