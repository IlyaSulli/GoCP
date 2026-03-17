def generate_sample(grammar, items = ["S"]) :
	frags = []
	if len(items) == 1 :
		if isinstance(items [0], Nonterminal) :
			for prod in grammar.productions(lhs = items [0]) :
				frags.append(generate_sample(grammar, prod.rhs()))
		else :
			frags.append(items [0])
	else :
		chosen_expansion = choice(items)
		frags.append(generate_sample, chosen_expansion)
	return frags


def generate_sample(grammar, prod, frags) :
	if prod in grammar._lhs_index :
		derivations = grammar._lhs_index [prod]
		derivation = random.choice(derivations)
		for d in derivation._rhs :
			generate_sample(grammar, d, frags)
	elif prod in grammar._rhs_index :
		frags.append(str(prod))

