def micro_world(bacteria, K) :
	sarg = [i [0] for i in sorted(enumerate(bacteria), key = lambda x : x [1])]
	sortedbac = [bacteria [i] for i in sarg]
	diff = [j - i for i, j in zip(sortedbac [: - 1], sortedbac [1 :])] + [K + 1]
	idx = [i for i, v in enumerate(diff) if v > K]
	return [bacteria [i] for i in sorted([sarg [i] for i in idx])]


def micro_world(bacteria, k) :
	bacteria = sorted(bacteria, reverse = True)
	i = 0
	result = 0
	while i < len(bacteria) :
		bacterium_size = bacteria [i]
		bigger_bacterium_exists = False
		while i + 1 < len(bacteria) :
			difference = bacterium_size - bacteria [i + 1]
			if difference > k :
				break
			if difference == 0 and not bigger_bacterium_exists :
				break
			bacterium_size = bacteria [i + 1]
			i += 1
			bigger_bacterium_exists = True
		result += 1
		i += 1
	return result

