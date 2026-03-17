def postalValidate(S) :
	S = S.replace(" ", "")
	if len(S) ! = 6 or S.isalpha() or S.isdigit() :
		return False
	if not S [0 : 5 : 2].isalpha() :
		return False
	if not S [1 : 6 : 2].isdigit() :
		return False
	return S.upper()


def postalValidate(S) :
	S = S.upper().replace(" ", "")
	if len(S) == 6 :
		for i in range(len(S)) :
			if i % 2 == 0 :
				if not (S [i].isalpha()) :
					return False
			else :
				if not (S [i].isdigit()) :
					return False
	else :
		return False
	return S

