def __init__(self, name, mode) :
	self.fl = open(name, mode)
	self.fl.write('\n')
	self.stdout = sys.stdout
	self.stdout.write('\n')
	self.stderr = sys.stderr
	sys.stdout = self
	sys.stderr = self


def __init__(self, aName, aCmd, logFileName = '', outFileName = '') :
	baseFormatter = logging.Formatter("%(asctime)s \t %(levelname)s \t %(name)s:%(module)s:%(lineno)d \t %(message)s")
	errorFormatter = logging.Formatter(LOG_IDENTIFIER + "%(asctime)s \t %(levelname)s \t %(name)s:%(module)s:%(lineno)d \t %(message)s")
	if logFileName :
		fl = logging.FileHandler("%s.log" % aName)
	else :
		fl = logging.FileHandler("%s.log" % aName, 'w')
	fl.setLevel(logging.DEBUG)
	fl.setFormatter(baseFormatter)
	if outFileName :
		teeFile = PyExec.SuperTee("%s_out.log" % aName)
	else :
		teeFile = PyExec.SuperTee("%s_out.log" % aName, 'w')
	fl_out = logging.StreamHandler(teeFile)
	fl_out.setLevel(logging.CRITICAL)
	fl_out.setFormatter(errorFormatter)
	self.log = logging.getLogger('pyExec_main')
	log = self.log
	log.addHandler(fl)
	log.addHandler(fl_out)
	print "Test print statement."
	log.setLevel(logging.DEBUG)
	log.info("Starting %s", ME)
	log.critical("Critical.")
	try :
		raise Exception('Exception test.')
	except Exception, e :
		log.exception(str(e))
	a = 2 / 0

