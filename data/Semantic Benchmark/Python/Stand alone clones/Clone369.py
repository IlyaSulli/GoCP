def cumulative_sum(l) :
	total = 0
	cumulative = []
	for num in l :
		total += num
		cumulative.append(total)
	return cumulative


def cumulative_sum(a_list) :
	list_2 = []
	list_2.append(a_list [0])
	x = 1
	y = 0
	for i in a_list :
		print x, y, i
		if len(a_list) == x :
			break
		else :
			var1 = list_2 [y]
			var2 = a_list [x]
			var3 = var1 + var2
			list_2.append(var3)
			x += 1
			y += 1
	return list_2

