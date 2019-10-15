import re

def multi_re_find(patterns,phrase):

	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')
		
test_phrase = 'This is a string!'#NOW I WANT TO REMOVE THE CAPITAL LETTER T

test_patterns = ['[a-z]+']

multi_re_find(test_patterns,test_phrase)