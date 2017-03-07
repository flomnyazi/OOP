class Person:
	def _init_(self, name,surname):
		self.name = name
		self.surname = surname

class staff(Person):
	Entrylevel, Midlevel, Seniorlevel = range(2)
	def _init_(self,employment_level,):
		self.employment_level = employment_level
 