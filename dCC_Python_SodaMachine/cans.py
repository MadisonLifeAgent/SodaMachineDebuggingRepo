class Can:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price


class Cola(Can):
    def __init__(self):
        super(Cola, self).__init__("Cola", 0.60, 0)


class OrangeSoda(Can):
    def __init__(self):
        super(OrangeSoda, self).__init__("Orange Soda", 0.40, 0)


class RootBeer(Can):
    def __init__(self):
        super(RootBeer, self).__init__("Root Beer", 0.50, 0)
