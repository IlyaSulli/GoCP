def run(self) :
	while self.fileNames :
		print (self.fileNames)
		time.sleep(2)
		name = self.fileNames.pop(0)
		s = 'uploaded file: ' + name + '\n'
		print (s)
		self.sig.strSig.emit(s)
		self.uploaded.append(name)
		if len(self.fileNames) == 0 :
			self.sig.strSig.emit("files transmitted: %s" % str(self.uploaded))
	else :
		time.sleep(1)


def run(self) :
	while not self.stoprequest.isSet() :
		try :
			num = self.input_q.get(True, 0.1)
			print 'In thread, processing', num
			time.sleep(0.5)
			self.result_q.put(True)
		except Queue.Empty as e :
			continue

