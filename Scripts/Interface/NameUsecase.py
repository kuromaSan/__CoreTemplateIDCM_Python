from ..NameCrafter import NameCrafter
from ..NameModel import NameModel

class NameUsecase:
    def __init__(self, name_crafter: NameCrafter, name_model: NameModel):
        self.name_crafter = name_crafter
        self.name_model = name_model

    def Execute(self):
        # Use the name_crafter and name_model to execute the use case
        pass