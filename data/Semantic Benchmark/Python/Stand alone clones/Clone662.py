def print_list(the_list, indent_level = 0) :
	stack = [iter(the_list)]
	while stack :
		try :
			item = stack [- 1].next()
		except StopIteration :
			stack.pop()
			indent_level -= 1
			continue
		if isinstance(item, list) :
			indent_level += 1
			stack.append(iter(item))
		else :
			print "\t" * indent_level, item


def print_list(the_list) :
	stack = [iter(the_list)]
	while stack :
		for item in stack [- 1] :
			if isinstance(item, (list, tuple)) :
				stack.append(iter(item))
				break
			else :
				print '\t' * (len(stack) - 1), item
		else :
			stack.pop()

