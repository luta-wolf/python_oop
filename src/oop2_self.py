class Point:
    "Класс для представления координат на плоскости"
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        # print('Вызов метода set_coords ' + str(self))

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
# pt2 = Point()
pt.set_coords(1, 2)
print(pt.get_coords())
# pt2.set_coords(10, 20)
# print(pt2.get_coords())
# print(pt.__dict__)
# print(pt2  .__dict__)

f = getattr(pt, 'get_coords')
print(f)
print(f())