class Student:
    def __init__(self, netid, name):
        self._name = name
        self._netid = netid
    
    @property
    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_netid(self):
        return self._netid
    
    def add_course(self, course):
        pass

class Faculty:
    pass


