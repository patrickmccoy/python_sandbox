class People:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def get_first_name(self):
        return self.name.split(' ')[0]
    
    def get_last_name(self):
        return self.name.split(' ')[1]

    def set_name(self, new_name):
        self.name = new_name
        return self.name
