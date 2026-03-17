def strtr(strng, replace) :
	if replace and strng :
		s, r = replace.popitem()
		return r.join(strtr(subs, dict(replace)) for subs in strng.split(s))
	return strng


def strtr(strng, replace) :
	buffer = []
	i, n = 0, len(strng)
	while i < n :
		match = False
		for s, r in replace.items() :
			if strng [i : len(s) + i] == s :
				buffer.append(r)
				i = i + len(s)
				match = True
				break
		if not match :
			buffer.append(strng [i])
			i = i + 1
	return ''.join(buffer)

