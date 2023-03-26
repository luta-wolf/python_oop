class Vektor:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD  <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vektor.validate(x) and Vektor.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vektor(1, 2)
print(Vektor.validate(5))
res = v.get_coords()
print(res)

v2 = Vektor(10, 20)
res = v2 .get_coords()
print(res)
print(Vektor.norm2(5, 6))