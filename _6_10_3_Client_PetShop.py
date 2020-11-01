class Client:
    def __init__(self,name, secname, balance):
        self.name=name
        self.secname = secname
        self.balance = balance

    def __str__(self):
        return 'Клиент "{0} {1}". Баланс: {2}'.format(self.name, self.secname, self.balance)