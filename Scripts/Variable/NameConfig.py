class NameConfig:
    def __init__(self, name_length: int, name_format: str, name_prefix: str, name_suffix: str):
        self.name_length = name_length
        self.name_format = name_format
        self.name_prefix = name_prefix
        self.name_suffix = name_suffix

    def __str__(self):
        return f"NameConfig(name_length={self.name_length}, name_format='{self.name_format}', name_prefix='{self.name_prefix}', name_suffix='{self.name_suffix}')"