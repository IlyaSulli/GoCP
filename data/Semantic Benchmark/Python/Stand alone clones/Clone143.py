def _safe_eval(expr, functions_and_constants = {}, check_compiling_input = True) :
	assert len(expr) < 1024
	if check_compiling_input :
		check_for_pow(expr)
	code = compile(expr, '', 'eval')
	ops = disassemble(code)
	assert len(ops) < 1024
	stack = []
	for op in ops :
		value = op.touch_value(stack, functions_and_constants)
	return value


def _safe_eval(node, variables, functions) :
	if isinstance(node, ast.Num) :
		return node.n
	elif isinstance(node, ast.Name) :
		return variables [node.id]
	elif isinstance(node, ast.BinOp) :
		op = _operations [node.op.__class__]
		left = _safe_eval(node.left, variables, functions)
		right = _safe_eval(node.right, variables, functions)
		if isinstance(node.op, ast.Pow) :
			assert right < 100
		return op(left, right)
	elif isinstance(node, ast.Call) :
		assert not node.keywords and not node.starargs and not node.kwargs
		assert isinstance(node.func, ast.Name), 'Unsafe function derivation'
		func = functions [node.func.id]
		args = [_safe_eval(arg, variables, functions) for arg in node.args]
		return func(* args)
	assert False, 'Unsafe operation'

