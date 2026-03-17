def roman_int(user_choice) :
	ix = 0
	iy = 0
	result = 0
	while ix < len(user_choice) :
		while iy < len(roman_numerals) and not user_choice.startswith(roman_numerals [iy] [0], ix) :
			iy += 1
		if iy < len(roman_numerals) :
			result += roman_numerals [iy] [1]
			ix += len(roman_numerals [iy] [0])
		else :
			raise ValueError('Invalid Roman numeral')
	return result


def roman_int(user_roman) :
	user_roman = user_roman.upper()
	resultI = 0
	while user_roman :
		if user_roman [: 2] in roman_numerals :
			resultI += roman_numerals [user_roman [: 2]]
			user_roman = user_roman [2 :]
		elif user_roman [: 1] in roman_numerals :
			resultI += roman_numerals [user_roman [: 1]]
			user_roman = user_roman [1 :]
		else :
			print ('No roman number')
			return
	print (resultI)

