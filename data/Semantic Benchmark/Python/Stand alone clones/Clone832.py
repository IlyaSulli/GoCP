def awesome(string) :
	foo = [{'subs' : ['A', 'B', 'C'], 'func' : do_something},
	{'subs' : ['1', '2', '3'], 'func' : do_something_else},
	{'subs' : ['!', '?', '.'], 'func' : do_another_thing}]
	for bar in foo :
		if any(s in string for s in bar ['subs']) :
			x = bar ['func']()
			break
	x += complicated_thing()
	if some_condition(x) :
		x += "Hello"
	else :
		x += "World"
	return x


def awesome(my_string) :
	if is_substr(my_string, ["A", "B", "C"]) :
		x = do_something() + complicated_thing()
	elif is_substr(my_string, ["1", "2", "3"]) :
		x = do_something_else() + complicated_thing()
	elif is_substr(my_string, ["!", "#", "$"]) :
		x = do_another_thing() + complicated_thing()
	return x + ("Hello" if some_condition(x) else "World")

