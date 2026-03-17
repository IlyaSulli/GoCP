def evaluate(tokens, ops, precedence) :
	for prec in precedence :
		index = find_op(tokens, prec)
		while index > = 0 :
			tokens = reduce_binary_infix(tokens, index, ops)
			index = find_op(tokens, prec)
	return tokens


def evaluate(expr) :
	if len(expr) == 3 :
		l, op, r = expr
		return ops [op](l, r)
	else :
		for op_list in precedence :
			for op in expr :
				if op in op_list :
					idx = expr.index(op) - 1
					result = evaluate([expr.pop(idx) for i in range(3)])
					expr.insert(idx, result)
					return evaluate(expr)

