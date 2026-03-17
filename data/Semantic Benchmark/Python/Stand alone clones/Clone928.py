def unescape(text) :
	def fixup(m) :
		text = m.group(0)
		if text [: 2] == "&#" :
			try :
				if text [: 3] == "&#x" :
					return unichr(int(text [3 : - 1], 16))
				else :
					return unichr(int(text [2 : - 1]))
			except ValueError :
				pass
		else :
			try :
				text = unichr(htmlentitydefs.name2codepoint [text [1 : - 1]])
			except KeyError :
				pass
		return text
	return re.sub("&#?\w+;", fixup, text)


def unescape(text) :
	def fixup(m) :
		text = m.group(0)
		if text [: 2] == "&#" :
			try :
				if text [: 3] == "&#x" :
					return unichr(int(text [3 : - 1], 16))
				else :
					return unichr(int(text [2 : - 1]))
			except ValueError :
				print "Value Error"
				pass
		else :
			try :
				if text [1 : - 1] == "amp" :
					text = "&amp;amp;"
				elif text [1 : - 1] == "gt" :
					text = "&amp;gt;"
				elif text [1 : - 1] == "lt" :
					text = "&amp;lt;"
				else :
					print text [1 : - 1]
					text = unichr(htmlentitydefs.name2codepoint [text [1 : - 1]])
			except KeyError :
				print "keyerror"
				pass
		return text
	return re.sub("&#?\w+;", fixup, text)

