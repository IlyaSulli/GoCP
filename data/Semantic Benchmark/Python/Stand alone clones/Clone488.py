def next_bigger(a) :
	a = map(int, str(a))
	tmp = list(reversed(a))
	for i, item_a in enumerate(reversed(a)) :
		for j in (range(i)) :
			if item_a < tmp [j] :
				tmp [i] = tmp [j]
				print (list(reversed(tmp [i :])))
				tmp [j] = item_a
				fin = list(reversed(tmp [i :])) + sorted(tmp [: i])
				return functools.reduce(lambda x, y : x * 10 + y, fin)
	return - 1


def next_bigger(n) :
	arr = [int(x) for x in str(n)]
	i = len(arr) - 1
	while i > 0 and arr [i - 1] > = arr [i] :
		i -= 1
	if i < = 0 :
		return - 1
	j = len(arr) - 1
	while arr [j] < = arr [i - 1] :
		j -= 1
	arr [i - 1], arr [j] = arr [j], arr [i - 1]
	arr [i :] = arr [len(arr) - 1 : i - 1 : - 1]
	return int(''.join(str(x) for x in arr))

