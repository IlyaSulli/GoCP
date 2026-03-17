def create_random(cls, level) :
	if level == 0 :
		is_op = True
	elif level == max_levels :
		is_op = False
	else :
		is_op = random.random() < = 1.0 - pow(level / max_levels, 2.0)
	if is_op :
		return binary_expression.create_random(level)
	else :
		return integer_expression.create_random(level)


def create_random(cls, level) :
	symbol = None
	r = random.random()
	cumulative = 0.0
	for k, v in operators.items() :
		cumulative += v ['prob']
		if r < = cumulative :
			symbol = k
			break
	assert symbol ! = None
	left = expression.create_random(level + 1)
	right = expression.create_random(level + 1)
	return binary_expression(symbol, left, right)

