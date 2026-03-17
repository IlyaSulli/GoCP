def outer() :
	def setlist(newlist) :
		mylist = newlist
	mylist = []
	def inner() :
		setlist(['new_list'])
	inner()


def outer() :
	global mylist
	mylist = []
	def inner() :
		global mylist
		mylist += [1]
	inner()

