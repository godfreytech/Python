x = 50

def func():
	global x
	x = 1000
	
print("Before function call, x is ",x)
func()
print("After function call, x is ",x)
