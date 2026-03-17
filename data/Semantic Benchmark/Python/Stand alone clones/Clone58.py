def query_yes_no(question, default = True) :
	yes_list = ["yes", "y"]
	no_list = ["no", "n"]
	default_dict = {
	None : "[y/n]",
	True : "[Y/n]",
	False : "[y/N]",
	}
	default_str = default_dict [default]
	prompt_str = "%s %s " % (question, default_str)
	while True :
		choice = input_(prompt_str).lower()
		if not choice and default is not None :
			return default
		if choice in yes_list :
			return True
		if choice in no_list :
			return False
		notification_str = "Please respond with 'y' or 'n'"
		print (notification_str)


def query_yes_no(question, default = "yes") :
	valid = {"yes" : True, "y" : True, "ye" : True,
	"no" : False, "n" : False}
	if default is None :
		prompt = " [y/n] "
	elif default == "yes" :
		prompt = " [Y/n] "
	elif default == "no" :
		prompt = " [y/N] "
	else :
		raise ValueError("invalid default answer: '%s'" % default)
	while True :
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if default is not None and choice == '' :
			return valid [default]
		elif choice in valid :
			return valid [choice]
		else :
			sys.stdout.write("Please respond with 'yes' or 'no' "
			"(or 'y' or 'n').\n")

