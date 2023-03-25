class Point:
    "Класс для представления координат на плоскости"
    color = 'red'
    circle = 2

    def __init__(self, x = 0, y = 0):
        print('Вызов __init__')
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление экземпляра: ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point(10, 20 )
pt2 = Point()
# pt.set_coords(1, 2)
print(pt.__dict__)
print(pt2.__dict__)