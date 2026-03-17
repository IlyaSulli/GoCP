def test() :
	fn = 'users.txt.txt'
	f = open(fn)
	output = []
	changeuser = 'peterpeter'
	userinfo = 'HeIsTall'
	for line in f :
		if line.strip().split(':') [0] ! = changeuser :
			output.append(line)
		else :
			output.append(changeuser + ":" + userinfo + "\n")
	f.close()
	f = open(fn, 'w')
	f.writelines(output)
	f.close()


def test() :
	fn = 'users.txt'
	changeuser = 'peterpeter'
	newinfo = 'HeIsTall'
	for line in fileinput.input(fn, inplace = 1) :
		user, oldinfo = line.split(':')
		print '%s:%s' % (user, newinfo if user == changeuser else oldinfo.replace('\n', ''))

