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
		print("DOG CREATED")

	def bark(self):
		print("WOOF")
		
	
		
mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()

#THE RESULT ON THE SCREEN WILL BE 
#DOG CREATED 
#ANIMAL 
#EATING