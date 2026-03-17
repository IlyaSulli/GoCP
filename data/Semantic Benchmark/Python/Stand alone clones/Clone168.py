def get_most_ooo_word(lines) :
	k = - 1
	most_o = []
	for line in lines :
		phrase_words = line.split()
		for word in phrase_words :
			c = word.count('o')
			if c > k :
				k = c
				most_o = [word]
			elif c == k :
				most_o.append(word)
	return most_o


def get_most_ooo_word(words) :
	if type(words) == list and len(words) > 0 :
		words = words [0].split()
	else :
		words = words.split()
	k = words [0]
	for i in range(1, len(words) - 1) :
		if words [i].count('o') > words [i - 1].count('o') :
			k = words [i]
	return (k)

