def __call__(self, parser, args, values, option_string = None) :
	if values is None :
		self.values += 1
	else :
		try :
			self.values = int(values)
		except ValueError :
			self.values = values.count('v') + 1
	setattr(args, self.dest, self.values)


def __call__(self, parser, args, values, option_string = None) :
	if args.verbose == None :
		base = 0
	else :
		base = args.verbose
	option_string = option_string.lstrip('-')
	if option_string [0] == 'q' :
		incr = - 1
	elif option_string [0] == 'v' :
		incr = 1
	else :
		raise argparse.ArgumentError(self,
		'Option string for verbosity must start with v(erbose) or q(uiet)')
	if values == None :
		values = base + incr
	else :
		try :
			values = int(values)
		except ValueError :
			values = values.lower()
			if not re.match('^[vq]+$', values) :
				raise argparse.ArgumentError(self,
				"Option string for -v/-q must contain only further 'v'/'q' letters")
			values = base + incr + values.count('v') - values.count('q')
	setattr(args, self.dest, values)

