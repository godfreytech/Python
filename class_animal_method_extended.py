#INHERITANCE IN PYTHON

class Animal():

	def __init__(self):
		print("ANIMAL CREATED")
		
	def whoAmI(self):
		print("ANIMAL")
		
	def eat(self):
		print('EATING')
		
class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("DOG CREATED")

	
mydog = Dog()
mydog.whoAmI()
mydog.eat()

#THE RESULT ON THE SCREEN WILL BE 
#ANIMAL CREATED
#DOG CREATED 
#ANIMAL 
#EATING