def run(self) :
	self.process = subprocess.Popen(self.cmd, stdout = self.outFile, stderr = self.errFile)
	while (self.process.poll() is None and self.timeout > 0) :
		time.sleep(1)
		self.timeout -= 1
	if not self.timeout > 0 :
		self.process.terminate()
		self.timed_out = True
	else :
		self.timed_out = False


def run(self, timeout) :
	def target() :
		print 'Thread started'
		self.process = subprocess.Popen(self.cmd, shell = True)
		self.process.communicate()
		print 'Thread finished'
	thread = threading.Thread(target = target)
	thread.start()
	thread.join(timeout)
	if thread.is_alive() :
		print 'Terminating process'
		self.process.terminate()
		thread.join()
	print self.process.returncode

