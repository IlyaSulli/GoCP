def getName(self, name) :
	listy = []
	splitName = name.split(' ')
	for i in range(len(splitName)) :
		if i == (len(splitName) - 1) :
			listy.append('Surname: ' + splitName [i])
		else :
			listy.append('Name: ' + splitName [i])
	return listy


def getName(self, name) :
	splitName = [i.strip() for i in name.split(' ') if i.strip()]
	try :
		surname = splitName.pop()
	except IndexError :
		print "Exception Name for processing in empty."
		return ""
	user_name = ""
	for i in splitName :
		user_name = "%s Name: %s," % (user_name, i)
	user_name = user_name.strip()
	user_name = "%s Surname: %s" % (user_name, surname)
	return user_name

