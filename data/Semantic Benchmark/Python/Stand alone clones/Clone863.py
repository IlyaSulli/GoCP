def main_loop() :
	print "where are you from?"
	loc = raw_input()
	print "so your from " + loc + "?"
	ans = raw_input()
	def isittrue() :
		if ans == "yes" :
			print "We all love " + loc
		else :
			print "Where did you say you were from again?"
	isittrue()


def main_loop() :
	global ans
	print "where are you from?"
	loc = raw_input()
	print "so your from " + loc + "?"
	ans = raw_input()
	return ans, loc

