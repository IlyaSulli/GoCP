def ping(host, n = 0) :
	if (n > 0) :
		avg = 0
		for i in range(n) :
			avg += ping(host)
		avg = avg / n
	mp = MultiPing([host])
	mp.send()
	responses, no_responses = mp.receive(1)
	for addr, rtt in responses.items() :
		RTT = rtt
	if no_responses :
		mp.send()
		responses, no_responses = mp.receive(1)
		RTT = - 1
	return RTT


def ping(host) :
	import subprocess, platform
	ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
	args = "ping " + " " + ping_str + " " + host
	need_sh = False if platform.system().lower() == "windows" else True
	return subprocess.call(args, shell = need_sh) == 0

