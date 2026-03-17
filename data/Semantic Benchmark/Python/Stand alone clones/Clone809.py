def turns(NumOfTries, word) :
	score = 0
	guesses = set()
	for i in range(len(w)) :
		guess = str(raw_input('Guess a letter (caps only): '))
		guesses.add(guess)
		if guess in word :
			score += 1
		print [c if c in guesses else "_" for c in w]
	return score


def turns(NumOfTries, w, score) :
	UI = str(raw_input('Guess a letter (caps only): '))
	j = 0
	for i in w :
		if UI == i :
			score.append('Yes')
			UserGuesses [j] = UI
		j = j + 1
	print UserGuesses
	while NumOfTries > 0 :
		turns(NumOfTries - 1, w, score)
		break

