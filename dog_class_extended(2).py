class Dog():
	
	def __init__(self,breed,name): #the def enclosed function must always be followed by a space character
		self.breed = breed
		self.name = name
		
mydog = Dog(breed = "Lab",name = "Sammy")
print(mydog.breed)
print(mydog.name)
