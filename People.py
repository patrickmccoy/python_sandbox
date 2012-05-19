import string
import uuid

class People:
    def __init__(self, name):
        (self.first, self.last) = name.split(' ')
        self._id = uuid.uuid4()
    
    def get_id(self, string=False):
        if (string):
            return str(self._id)
        else:
            return self._id

    def get_name(self):
        return string.join((self.first, self.last))

    def get_first_name(self):
        return self.first
    
    def get_last_name(self):
        return self.last

    def set_name(self, new_name):
        (self.first, self.last) = new_name.split(' ')
        return self.get_name()
    
    def set_first_name(self, new_first):
        self.first = new_first
        return self.first
