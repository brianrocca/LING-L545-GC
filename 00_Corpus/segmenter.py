import sys, re
#Read in lines
line = sys.stdin.readline()
#As long as line has something in it, perform the following operations
while line != '':
	#Tokenize words by splitting lines at spaces.
	#For each token, if the word comes before a ? or !, then print that word and add a new line afterwards.
	for token in line.split(' '):
		if token[-1] in '?!':
			sys.stdout.write(token + '\n')
		#Delete empty lines
		if token.strip() == '':
			continue
		#Don't add a newline after the following abbreviations and numbers
		elif token[-1] == '.':
			if token in ['No.', 'Alm.', 'Ir.', '...', 'S.D.', 'V.R.', 'J.']:
				sys.stdout.write(token + ' ')
			elif re.findall('[0-9]+\.', token):
				sys.stdout.write(token + ' ')
			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()
