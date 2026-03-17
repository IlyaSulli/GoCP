def awesome(my_string) :
	if is_substr(my_string, ["A", "B", "C"]) :
		x = do_something() + complicated_thing()
	elif is_substr(my_string, ["1", "2", "3"]) :
		x = do_something_else() + complicated_thing()
	elif is_substr(my_string, ["!", "#", "$"]) :
		x = do_another_thing() + complicated_thing()
	return x + ("Hello" if some_condition(x) else "World")


def awesome(somestring) :
	x = some_default_value
	vals = [do_something, do_something_else, do_another_thing]
	subs = [['AB', 'CD', 'EF'], ['12', '34', '56'], ['!@', '@#', '#$']]
	for val, substrings in zip(vals, subs) :
		if check(substrings, somestring) :
			x = val()
			break
	x += complicated_thing()
	if some_condition(x) :
		x += "Hello"
	else :
		x += "World"
	return x

