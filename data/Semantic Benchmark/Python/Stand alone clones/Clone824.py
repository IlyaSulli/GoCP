def run(cmd, timeout_sec) :
	proc = Popen(shlex.split(cmd), stdout = PIPE, stderr = PIPE)
	timer = Timer(timeout_sec, proc.kill)
	try :
		timer.start()
		stdout, stderr = proc.communicate()
	finally :
		timer.cancel()


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

