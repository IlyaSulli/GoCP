def searchWordlist() :
	path = str(raw_input(PATH))
	word = str(raw_input(WORD))
	loc = - 1
	with open(path) as f :
		for i, line in enumerate(f) :
			if word in line :
				loc = i
				break
	if loc > = 0 :
		print ("Word found at line {}".format(loc))
	else :
		print ("Word not found")


def searchWordlist() :
	path = str(raw_input(PATH))
	word = str(raw_input(WORD))
	with open(path) as f :
		if any(word in line for line in f) :
			print ('Word found')
		else :
			print ('Word not found')

