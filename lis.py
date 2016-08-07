def tokenize(chars):

	'''breaking a string into multiple tokens'''

    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def read_from_tokens(tokens):

	if (len(tokens) == 0):
		raise SyntaxError('Unexpected EOF while reading.')

	token  = tokens.pop(0)

	if (token == '('):
		L = []

		while()

	elif (token == ')'):

	else: 



def parse(program):
	return read_from_tokens(tokenize(program))