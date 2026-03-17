def signal_handler(helloProcess, counterProcess, signum, frame) :
	print multiprocessing.active_children()
	print "helloProcess: ", helloProcess
	print "counterProcess: ", counterProcess
	print "current_process: ", multiprocessing.current_process()
	if signum == 17 :
		for signame in [SIGINT, SIGTERM, SIGQUIT, SIGCHLD] :
			signal(signame, SIG_DFL)
		print "helloProcess: ", helloProcess.is_alive()
		if not helloProcess.is_alive() :
			print "Restarting helloProcess"
			helloProcess = HelloWorld()
			helloProcess.start()
		print "counterProcess: ", counterProcess.is_alive()
		if not counterProcess.is_alive() :
			print "Restarting counterProcess"
			counterProcess = Counter()
			counterProcess.start()
		for signame in [SIGINT, SIGTERM, SIGQUIT, SIGCHLD] :
			signal(signame, partial(signal_handler, helloProcess, counterProcess))
	else :
		signal(SIGCHLD, SIG_IGN)
		if helloProcess.is_alive() :
			print "Stopping helloProcess"
			helloProcess.terminate()
		if counterProcess.is_alive() :
			print "Stopping counterProcess"
			counterProcess.terminate()
		sys.exit(0)


def signal_handler(signum, _) :
	global helloProcess, counterProcess
	if signum == SIGCHLD :
		pid, status = os.waitpid(- 1, os.WNOHANG | os.WUNTRACED | os.WCONTINUED)
		if os.WIFCONTINUED(status) or os.WIFSTOPPED(status) :
			return
		if os.WIFSIGNALED(status) or os.WIFEXITED(status) :
			if helloProcess.pid == pid :
				print ("Restarting helloProcess")
				helloProcess = HelloWorld()
				helloProcess.start()
			elif counterProcess.pid == pid :
				print ("Restarting counterProcess")
				counterProcess = Counter()
				counterProcess.start()
	else :
		signal(SIGCHLD, SIG_DFL)
		if helloProcess.is_alive() :
			print ("Stopping helloProcess")
			helloProcess.terminate()
		if counterProcess.is_alive() :
			print ("Stopping counterProcess")
			counterProcess.terminate()
		sys.exit(0)

