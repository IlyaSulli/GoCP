def __call__(self, parser, namespace, values, option_string = None) :
	for value in values :
		try :
			n, v = value.split('=')
			setattr(namespace, n, v)
		except ValueError :
			setattr(namespace, '_unrecognized_args', values [values.index(value) :])


def __call__(self, parser, namespace, values, option_string = None) :
	def all_opt_strings(parser) :
		nested = (x.option_strings for x in parser._actions
		if x.option_strings)
		return itertools.chain.from_iterable(nested)
	all_opts = list(all_opt_strings(parser))
	eaten = []
	while len(values) > 0 :
		if values [0] in all_opts :
			break
		eaten.append(values.pop(0))
	setattr(namespace, self.dest, eaten)
	_, extras = parser._parse_known_args(values, namespace)
	try :
		getattr(namespace, argparse._UNRECOGNIZED_ARGS_ATTR).extend(extras)
	except AttributeError :
		setattr(namespace, argparse._UNRECOGNIZED_ARGS_ATTR, extras)

