import sys
#Create function "Maxmatch"
def maxmatch(sentence, dictionary):
	#if sentence is empty, return empty list
	if sentence == '':
		return []
	#Try to find the longest match possible in dictionary
	for i in range(0, len(sentence)):
		firstword = sentence[0:-i]
		remainder = sentence[-i:]
		#if there's a match in the dictionary, print
		if firstword in dictionary:
			return [firstword] + maxmatch(remainder, dictionary)
	#if firstword not in dictionary,print first character of line
	firstword = sentence[0]
	remainder = sentence[1:]
	return [firstword] + maxmatch(remainder, dictionary)

dictionary = [line.strip() for line in open("japanese.txt").readlines()]

fd = open(sys.argv[1])
line = fd.readline()
while line != '':
	print(' '.join(maxmatch(line.strip('\n'), dictionary)))
	line = fd.readline()
