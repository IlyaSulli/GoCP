def handle_request(req) :
	for i, h in enumerate(handlers) :
		if h [1].handles(req) :
			h [0] += 1
			for j in reversed(range(i + 1)) :
				if handlers [j] [0] < = h [0] :
					break
			if j < i :
				handlers [j + 1 : i + 1] = handlers [j : i]
				handlers [j] = h
			break
	else :
		return None
	return h [1]


def handle_request(req) :
	for (i, h) in enumerate(handlers) :
		if h [1].handles(req) :
			h [0] += 1
			while i > 0 and handlers [i] [0] > handlers [i - 1] [0] :
				handlers [i - 1], handlers [i] = handlers [i], handlers [i - 1]
				i -= 1
			return h [1]
	return None

