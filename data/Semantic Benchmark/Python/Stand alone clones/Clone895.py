def int_to_roman(num) :
	_values = [
	1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	_strings = [
	'M', 'C', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	result = ""
	decimal = num
	while decimal > 0 :
		for i in range(len(_values)) :
			if decimal > = _values [i] :
				if _values [i] > 1000 :
					result += u'\u0304'.join(list(_strings [i])) + u'\u0304'
				else :
					result += _strings [i]
				decimal -= _values [i]
				break
	return result


def int_to_roman(a) :
	all_roman_digits = []
	digit_lookup_table = [
	"", "0", "00", "000", "01",
	"1", "10", "100", "1000", "02"]
	for i, c in enumerate(reversed(str(a))) :
		roman_digit = ""
		for d in digit_lookup_table [int(c)] :
			roman_digit += ("IVXLCDM" [int(d) + i * 2])
		all_roman_digits.append(roman_digit)
	return "".join(reversed(all_roman_digits))

