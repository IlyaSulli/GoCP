def myLogger(self) :
	if None == self.logger :
		self.logger = logging.getLogger('ProvisioningPython')
		self.logger.setLevel(logging.DEBUG)
		now = datetime.datetime.now()
		handler = logging.FileHandler('ProvisioningPython' + now.strftime("%Y-%m-%d") + '.log')
		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
	return self.logger


def myLogger(name) :
	global loggers
	if loggers.get(name) :
		return loggers.get(name)
	else :
		logger = logging.getLogger(name)
		logger.setLevel(logging.DEBUG)
		now = datetime.datetime.now()
		handler = logging.FileHandler(
		'/root/credentials/Logs/ProvisioningPython'
		+ now.strftime("%Y-%m-%d")
		+ '.log')
		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		handler.setFormatter(formatter)
		logger.addHandler(handler)
		loggers [name] = logger
		return logger

