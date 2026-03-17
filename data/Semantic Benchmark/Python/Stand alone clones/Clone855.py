def censor(text, word) :
	length_of_word = len(word)
	word_now_censored = '*' * length_of_word
	wordlist = text.split()
	new_words_list = []
	for item in wordlist :
		if item == word :
			new_words_list.append(word_now_censored)
		else :
			new_words_list.append(item)
	return " ".join(new_words_list)


def censor(text, word) :
	text = list(text)
	for n in range(0, len(text)) :
		i = 0
		while 1 == 1 :
			for i in range(0, len(word)) :
				if text [n + i] == word [i] :
					i += 1
				else :
					break
			if i == len(word) :
				for m in range(0, i) :
					text [n + m] = '*'
			else :
				break
		n += i
	return "".join(text)

