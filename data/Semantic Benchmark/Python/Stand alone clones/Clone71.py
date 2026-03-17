def getVerb() :
	correctAnswers = 0
	for level in (level1, level2) :
		level_name, choices = level [0], level [1 :]
		random.shuffle(choices)
		for choice in choices :
			prefix, suffix = choice.split(' ', 2)
			print (prefix, blanks, level_name)
			ans = raw_input('Answer: ')
			while True :
				if ans == suffix :
					correctAnswers += 1
					print ("Nice one!")
					print (correctAnswers)
					break
				else :
					print ("Bad luck!")
					ans = raw_input('Try again: ')


def getVerb() :
	level1 = ["(manger)", "je mange", "tu manges", "il mange", "elle mange", "nous mangeons", "vous mangez", "ils mangent", "elles mangent"]
	level2 = ["(boire)", "je bois", "tu bois", "il boit", "elle boit", "nous buvons", "vous buvez", "ils boivent", "elles boivent"]
	blanks = '_' * 8
	correctAnswers = 0
	randomElement = random.choice(level1)
	print (randomElement.split() [0], blanks, level1 [0])
	ans = input()
	while True :
		if ans == randomElement.split() [1] :
			correctAnswers += 1
			print ("Nice one!")
			print (correctAnswers)
		else :
			print ("Bad luck!")
		ans = input()

