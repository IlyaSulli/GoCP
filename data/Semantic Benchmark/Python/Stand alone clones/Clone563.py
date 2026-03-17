def read_file() :
	fname = 'InputFile.bak'
	if os.path.exists(fname) :
		fsize = os.path.getsize(fname)
		with open(fname, 'rb') as fh :
			while fh.tell() < fsize :
				item = cPickle.load(fh)
				for k, v in item.iteritems() :
					print v [0], "\t", v [1], "\t", k
	else :
		item_name = {}


def read_file() :
	if os.path.exists('InputFile.bak') :
		with open('InputFile.bak', 'rb') as fname :
			while True :
				try :
					item_name = cPickle.load(fname)
					for k, v in item_name.iteritems() :
						print v [0], "\t", v [1], "\t", k
				except EOFError :
					break
	else :
		item_name = {}

