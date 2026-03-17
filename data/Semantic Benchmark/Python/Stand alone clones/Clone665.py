def brute_force_crack(hashed_pass) :
	char_list = create_possible_chars()
	def build_combos(curr_str = "") :
		if len(curr_str) == 4 :
			return None
		for letter in char_list :
			guess = curr_str + letter
			if is_password(guess, hashed_pass) :
				return guess
			else :
				result = build_combos(guess)
				if result is not None :
					return result
		return None
	return build_combos()


def brute_force_crack(hashed_pass) :
	char_list = create_possible_chars()
	def build_combos(curr_str) :
		if is_password(curr_str, hashed_pass) :
			return curr_str
		if len(curr_str) > = 4 :
			return
		for letter in char_list :
			password = build_combos(curr_str + letter)
			if password :
				return password
	return build_combos("")

