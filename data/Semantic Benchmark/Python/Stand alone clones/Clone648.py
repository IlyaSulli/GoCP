def shift_cipher_noloop(plain, i) :
	if (plain == "") :
		return ""
	else :
		if len(plain) > 3 and i > 0 :
			return shift_cipher_noloop(plain [1 :] + plain [0], i - 1)
		else :
			return plain


def shift_cipher_noloop(original) :
	def encrypt_recursion(plain) :
		encrypted = ""
		if plain == "" :
			encrypted = ""
		elif len(plain) > 3 :
			encrypted += plain [3]
			encrypted += encrypt_recursion(plain [1 :])
		else :
			encrypted += original [3 - len(plain)]
			encrypted += encrypt_recursion(plain [1 :])
		return encrypted
	return encrypt_recursion(original)

