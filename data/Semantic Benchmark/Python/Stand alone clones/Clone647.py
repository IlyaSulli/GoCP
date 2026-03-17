def get_parameters(some_file_name) :
	source = json.loads(some_file_name)
	return dict(
	mpi_nodes = source.get('mpi-nodes', 1),
	cluster_size = source ['cluster-size'],
	initial_cutoff = source ['initial-cutoff'],
	)
	controlsFileName = sys.argv [1]
	try :
		params = get_parameters(controlsFileName)
	except IOError :
		print "Could not process the file '{0}'!".format(controlsFileName)
		sys.exit(1)
	except KeyError, e :
		print "Missing control definition for '{0}'.".format(e.message)
		sys.exit(2)


def get_parameters(parameters_file_name) :
	parameterValues = json.load(open(parameters_file_name, "r"))
	Parameters = collections.namedtuple('Parameters',
	"""
	mpi_nodes
	cluster_size
	initial_cutoff
	truncation_length
	""")
	parameters = Parameters(
	parameterValues.get(Parameters._fields [0].replace('_', '-'), 1),
	parameterValues.get(Parameters._fields [1].replace('_', '-')),
	parameterValues.get(Parameters._fields [2].replace('_', '-')),
	parameterValues.get(Parameters._fields [3].replace('_', '-')))
	globals() ["ControlParameters"] = parameters

