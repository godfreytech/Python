import re #REGULAR EXPRESSIONS

def multi_re_find(patterns,phrase):

	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')
		
test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['sd{1,3}']

multi_re_find(test_patterns,test_phrase)