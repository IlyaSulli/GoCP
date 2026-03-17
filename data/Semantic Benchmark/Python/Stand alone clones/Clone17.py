def __init__(self, opt_name, dest = None, default = True, required = False, help = None) :
	super(ActionFlagWithNo, self).__init__(
	[
	'--' + opt_name [0],
	'--no-' + opt_name [0],
	] + opt_name [1 :],
	dest = (opt_name [0].replace('-', '_') if dest is None else dest),
	nargs = 0, const = None, default = default, required = required, help = help,
	)


def __init__(self, option_strings, dest, default = None, required = False, help = None) :
	if default is None :
		raise ValueError('You must provide a default with Yes/No action')
	if len(option_strings) ! = 1 :
		raise ValueError('Only single argument is allowed with YesNo action')
	opt = option_strings [0]
	if not opt.startswith('--') :
		raise ValueError('Yes/No arguments must be prefixed with --')
	opt = opt [2 :]
	opts = ['--' + opt, '--no-' + opt]
	super(ActionNoYes, self).__init__(opts, dest, nargs = 0, const = None,
	default = default, required = required, help = help)

