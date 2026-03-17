def solve(stickers) :
	i = 1
	while lowest_state(str(i), stickers) > = 0 :
		i *= 2
	top = i
	bottom = 0
	center = 0
	while top - bottom > 1 :
		center = (top + bottom) / 2
		if lowest_state(str(center), stickers) > = 0 :
			bottom = center
		else :
			top = center
	if lowest_state(str(top), stickers) > = 0 :
		return top
	else :
		return bottom


def solve(stickers) :
	i = 0
	stickers_left = 0
	while stickers_left > = 0 :
		i += best_jump(i, stickers_left)
		stickers_left = min(map(
		lambda x : how_many_have(x, i, stickers) - how_many_used(str(x), str(i)),
		NUMBERS))
	return i - 1

