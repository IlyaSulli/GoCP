def run_command(cmd) :
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	return subprocess.Popen(cmd,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	stdin = subprocess.PIPE,
	startupinfo = startupinfo).communicate()


def run_command(command) :
	p = subprocess.Popen(command,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	shell = True)
	for line in iter(p.stdout.readline, b'') :
		if line :
			yield line
	while p.poll() is None :
		sleep(.1)
	err = p.stderr.read()
	if p.returncode ! = 0 :
		print ("Error: " + str(err))

