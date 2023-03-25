class Person:
	def __init__(self, name, surname, place_of_birth, year_of_birth):
		self.name = name
		self.surname = surname
		self.place_of_birth = place_of_birth
		self.year_of_birth = year_of_birth

	def print_info(self, n):
		for i in range(n):
			print(f'Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}')


	def getAge(self, current_year):
		return current_year - self.year_of_birth


p1 = Person("Elon", "Musk", "ЮАР", 1971)
# p1.name = "Elon"
# p1.surname = "Musk"
# p1.place_of_birth = "ЮАР"
# p1.year_of_birth = 1971

p2 = Person("Sergey", "Korolev", "Российская федерация", 1907)
# p2.name = "Sergey"
# p2.surname = "Korolev"
# p2.place_of_birth = "Российская федерация"
# p2.year_of_birth = 1907

p1.print_info(1)
p2.print_info(1)
print(p1.getAge(2023))
print(p2.getAge(2023))

p3 = Person("Albert", "Einstein", "Germany", 1879)
# p3.name = "Albert"
# p3.suname = "Einstein"
# p3.year_of_birth = 1879
# забыли назначить поле place_of_birth

print(True + 1)
print(False + 0)
