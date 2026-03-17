def write(self, data) :
	if data [0 : LOG_IDR_LENGTH] == LOG_IDENTIFIER :
		self.fl.write("%s\n" % data [LOG_IDR_LENGTH :])
		self.stdout.write(data [LOG_IDR_LENGTH :])
	else :
		timestamp = str(datetime.datetime.now())
		if 'Traceback' == data [0 : 9] :
			data = '%s: %s' % (timestamp, data)
			self.fl.write(data)
		else :
			self.fl.write(data)
		self.stdout.write(data)


def write(self, data) :
	self.stream.write(data)
	self.stream.flush()
	self.data += data
	tmp = str(self.data)
	if '\x0a' in tmp or '\x0d' in tmp :
		tmp = tmp.rstrip('\x0a\x0d')
		log.info('%s%s' % (self.prefix, tmp))
		self.data = ''

