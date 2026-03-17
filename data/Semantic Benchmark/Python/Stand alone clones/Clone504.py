def execute(command) :
	process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	while True :
		nextline = process.stdout.readline()
		if nextline == '' and process.poll() is not None :
			break
		sys.stdout.write(nextline)
		sys.stdout.flush()
	output = process.communicate() [0]
	exitCode = process.returncode
	if (exitCode == 0) :
		return output
	else :
		raise ProcessException(command, exitCode, output)


def execute(command) :
	popen = subprocess.Popen(command, stdout = subprocess.PIPE, bufsize = 1)
	lines_iterator = iter(popen.stdout.readline, b"")
	while popen.poll() is None :
		for line in lines_iterator :
			nline = line.rstrip()
			print(nline.decode("latin"), end = "\r\n", flush = True)

