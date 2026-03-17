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


def execute(cmd) :
	popen = subprocess.Popen(cmd, stdout = subprocess.PIPE, universal_newlines = True)
	for stdout_line in iter(popen.stdout.readline, "") :
		yield stdout_line
	popen.stdout.close()
	return_code = popen.wait()
	if return_code :
		raise subprocess.CalledProcessError(return_code, cmd)

