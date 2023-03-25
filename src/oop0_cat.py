class Cat:
	def __init__(self, breed, name, age):
		self.breed = breed
		self.name = name
		self.age = age

	def miau(self):
		print(f'{self.breed} - miau, miau')

	def voice(self):
		print(f'My name is {self.name}, i\'m {self.age} yars old.')


cat1 = Cat('Бурма', 'Васька', 3)
cat2 = Cat('Савана', 'Красик', 5)
cat3 = Cat('Русская', 'Рыжик', 2)

cat1.miau()
cat1.voice()
cat2.miau()
cat2.voice()
cat3.miau()
cat3.voice()
