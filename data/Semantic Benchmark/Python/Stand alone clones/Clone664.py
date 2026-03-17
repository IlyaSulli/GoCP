def list_routes() :
	import urllib
	output = []
	for rule in app.url_map.iter_rules() :
		methods = ','.join(rule.methods)
		line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
		output.append(line)
	for line in sorted(output) :
		print (line)


def list_routes() :
	import urllib
	output = []
	for rule in app.url_map.iter_rules() :
		options = {}
		for arg in rule.arguments :
			options [arg] = "[{0}]".format(arg)
		methods = ','.join(rule.methods)
		url = url_for(rule.endpoint, ** options)
		line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
		output.append(line)
	for line in sorted(output) :
		print line

