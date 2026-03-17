def evaluate(exp) :
	for oplist in precedence :
		idx = 0
		while idx < len(exp) :
			op = exp [idx]
			if op in oplist :
				result = ops [op](exp [idx - 1], exp [idx + 1])
				exp [idx - 1 : idx + 2] = [result]
				idx -= 1
			else :
				idx += 1
	return exp [0]


def evaluate(tokens, ops, precedence) :
	for prec in precedence :
		index = find_op(tokens, prec)
		while index > = 0 :
			tokens = reduce_binary_infix(tokens, index, ops)
			index = find_op(tokens, prec)
	return tokens

