x = 50

def func(x):
	print('x is' ,x)
	x = 1000
	print('local x changed to' ,x)
	
func(x)