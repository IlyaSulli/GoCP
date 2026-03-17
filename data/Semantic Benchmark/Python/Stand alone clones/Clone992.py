def rec(chk, i) :
	print (locals())
	i += 1
	chk = chk + [i]
	if i ! = 4 :
		rec(chk, i)
		print (locals())


def rec(chk, i) :
	global flag
	print (locals())
	i += 1
	chk.append(i)
	if (i == 4) :
		flag = 1
	if (flag == 1) :
		return
	else :
		rec(chk [:], i)
	print (locals())

