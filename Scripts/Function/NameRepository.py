class NameRepository:
    def __init__(self):
        self.names = []

    def add_name(self, name):
        if name not in self.names:
            self.names.append(name)
            return True
        return False

    def get_names(self):
        return self.names

    def clear_names(self):
        self.names.clear()