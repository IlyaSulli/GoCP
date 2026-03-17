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


def run(cmd, timeout_sec) :
	proc = subprocess.Popen(shlex.split(cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	timeout = {"value" : False}
	timer = Timer(timeout_sec, kill_proc, [proc, timeout])
	timer.start()
	stdout, stderr = proc.communicate()
	timer.cancel()
	return proc.returncode, stdout.decode("utf-8"), stderr.decode("utf-8"), timeout ["value"]

