try:

	f = open('simple.txt','r')
	f.write("Test write to simple text!")
	
except IOError:
	print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
	print("SUCCESS!")
	f.close()