#SPECIAL METHODS

class Book():
	
		def __init__(self,title,author,pages):
			self.title = title
			self.author = author
			self.pages = pages
			
		def __str__(self):
			return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
			
		def __del__(self):
			print("a book is destroyed!")
b = Book("Python","Jose",200)
del b
			
mylist = [1,2,3]
print(mylist)