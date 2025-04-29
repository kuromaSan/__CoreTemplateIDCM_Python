from . import NameConfig

class NameBuilder:
    def __init__(self, name_config: NameConfig):
        self.name_config = name_config

    def build_name(self) -> str:
        # Build a name based on the configuration
        name = self.name_config.name_prefix + "GeneratedName" + self.name_config.name_suffix
        return name[:self.name_config.name_length]  # Ensure the name does not exceed the specified length

    def __str__(self):
        return f"NameBuilder(name_config={self.name_config})"