def printFigure(rows) :
	for x in range(rows) :
		items = [str(i) for i in range(1, x + 1)]
		if x % 2 == 0 :
			items = items [: : - 1]
		print (''.join(items))


def printFigure(rows) :
	if rows > 0 :
		printFigure(rows - 1)
		if rows % 2 == 0 :
			while (rows > 0) :
				print(str(rows) [: : - 1], end = '')
				rows -= 1
			print ('')
		else :
			i = 1
			while (i < = rows) :
				print(str(i), end = '')
				i += 1
			print ('')

