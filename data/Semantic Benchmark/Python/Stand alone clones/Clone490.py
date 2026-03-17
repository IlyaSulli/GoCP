def repeat(a, n) :
	def rep(a, c) :
		if c > 0 :
			print (a)
			rep(a, c - 1)
	return rep(a * n, n)


def repeat(a, n, already_ran = 0) :
	if n == 0 :
		print (a * (n + already_ran))
	else :
		print (a * (n + already_ran))
		repeat(a, n - 1, already_ran + 1)

