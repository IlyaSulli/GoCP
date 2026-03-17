def trans(transition, input, final, state) :
	for each in transition [state] [int(input [0])] :
		if each < 4 :
			state = each
			if len(input) == 1 :
				if (str(state) in final) :
					print "accepted"
					sys.exit()
				else :
					continue
			trans(transition, input [1 :], final, state)


def trans(transition, input, final, state, i) :
	for j in range(len(input)) :
		for each in transition [state] [int(input [j])] :
			if each < 4 :
				state = each
				if j == len(input) - 1 and (str(state) in final) :
					print "accepted"
					sys.exit()
				trans(transition, input [i + 1 :], final, state, i)
		i = i + 1

