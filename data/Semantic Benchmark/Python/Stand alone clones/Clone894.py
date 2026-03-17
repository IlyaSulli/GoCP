def int_to_roman(number) :
	result = ""
	for (arabic, roman) in ROMAN :
		(factor, number) = divmod(number, arabic)
		result += roman * factor
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

