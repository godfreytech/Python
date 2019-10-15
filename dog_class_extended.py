class Dog():
	
	def __init__(self,breed): #the def enclosed function must always be followed by a space character
		self.breed = breed
		
mydog = Dog(breed = "Lab")
otherdog = Dog(breed="Huskie")
print(mydog.breed)
print(otherdog.breed)
