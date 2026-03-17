def getPrint(thefun, * a, ** k) :
	savstdout = sys.stdout
	sys.stdout = cStringIO.StringIO()
	try :
		thefun(* a, ** k)
	finally :
		v = sys.stdout.getvalue()
		sys.stdout = savstdout
	return v


def getPrint(func, * args, ** kwds) :
	old_stdout = sys.stdout
	sys.stdout = StringIO()
	try :
		func(* args, ** kwds)
	except :
		raise
	else :
		return sys.stdout.getvalue()
	finally :
		sys.stdout = old_stdout

