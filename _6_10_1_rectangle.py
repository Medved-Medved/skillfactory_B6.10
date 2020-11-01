class Rectangle:
    def __init__(self,x, y, wdt, hgt):
        self.x = x
        self.y = y
        self.wdt = wdt
        self.hgt = hgt

    def __str__(self):
        return 'Rectangle({}, {}, {}, {})'.format(self.x, self.y, self.wdt, self.hgt)