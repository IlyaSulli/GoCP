def findmax(s) :
	matches = []
	current = [s [0]]
	for index, character in enumerate(s [1 :]) :
		if character > = s [index] :
			current.append(character)
		else :
			matches.append(current)
			current = [character]
	matches.append(current)
	maxlen = len(max(matches, key = len))
	return ["".join(match) for match in matches if len(match) == maxlen]


def findmax(input_string, tempbuffer = defaultdict(list), temp = '') :
	if len(input_string) == 0 :
		tempbuffer [len(temp)].append(temp)
		output = tempbuffer [maxkey(tempbuffer)]
		tempbuffer.clear()
		return output
	else :
		first_char = input_string [0]
		if len(temp) == 0 or first_char > temp [- 1] :
			temp = temp + first_char
		else :
			tempbuffer [len(temp)].append(temp)
			temp = first_char
		return findmax(input_string [1 :], tempbuffer, temp)

