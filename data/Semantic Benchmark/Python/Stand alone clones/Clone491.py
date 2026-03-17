def repeat(a, n) :
	def rep(a, c) :
		if c > 0 :
			print (a)
			rep(a, c - 1)
	return rep(a * n, n)


def repeat(string, times, lines_left = None) :
	print (string * times)
	if (lines_left is None) :
		lines_left = times
	lines_left = lines_left - 1
	if (lines_left > 0) :
		repeat(string, times, lines_left)

