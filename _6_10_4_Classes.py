class Employee:
    def __init__(self, name, secname, town, status):
        self.name = name
        self.secname = secname
        self.town = town
        self.status = status

    def __str__(self):
        return '{0} {1}, г. {2}, статус "{3}"'.format(self.name, self.secname, self.town, self.status)

class EmployeeList(list):

    def __str__(self):
        srez = ''
        for empl in self:
            srez += str(empl) + '\n'
        return srez