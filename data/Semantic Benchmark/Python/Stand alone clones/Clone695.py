def GetTheSentences(infile) :
	with open(infile) as fp :
		for result in re.findall('DELIMITER1(.*?)DELIMITER2', fp.read(), re.S) :
			print result


def GetTheSentences(file) :
	start_rx = re.compile('DELIMITER')
	end_rx = re.compile('DELIMITER2')
	start = False
	output = []
	with open(file, 'rb') as datafile :
		for line in datafile.readlines() :
			if re.match(start_rx, line) :
				start = True
			elif re.match(end_rx, line) :
				start = False
			if start :
				output.append(line)
	return output

