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

