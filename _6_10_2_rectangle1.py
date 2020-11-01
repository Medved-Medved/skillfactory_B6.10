class Rectangle1:
    def __init__(self,wdt, hgt):
        self.wdt = wdt
        self.hgt = hgt

    def get_width(self):
        return self.wdt
    def get_height(self):
        return self.hgt
    def get_area(self):
        return self.wdt * self.hgt