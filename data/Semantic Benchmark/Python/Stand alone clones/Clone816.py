def printTable(mylist) :
	maxLength = 0
	for item in mylist :
		for i in item :
			if len(i) > maxLength :
				maxLength = len(i)
			else :
				maxLength = maxLength
	for item in mylist :
		for i in range(len(item)) :
			item [i] = (item [i].rjust(maxLength))
	myNewlist = {0 : [], 1 : [], 2 : [], 3 : []}
	for i in range(len(item)) :
		for u in tableData :
			myNewlist [i].append(u [i])
	for key, value in myNewlist.items() :
		print (''.join(value))


def printTable(table) :
	colWidths = [0] * len(table)
	for y in range(len(table)) :
		for x in table [y] :
			if colWidths [y] < len(x) :
				colWidths [y] = len(x)
	for x in range(len(table [0])) :
		for y in range(len(table)) :
			print(table [y] [x].rjust(colWidths [y]), end = ' ')
		print ()
		x += 1

