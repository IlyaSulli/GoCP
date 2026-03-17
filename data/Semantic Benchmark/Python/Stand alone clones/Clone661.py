def increasing(fn, left, right) :
	left_items = [next(left)]
	right_items = [next(right)]
	heap = []
	def add_value(left_index, right_index) :
		value = fn(left_items [left_index], right_items [right_index])
		heapq.heappush(heap, (value, left_index, right_index))
	add_value(0, 0)
	while True :
		value, left_index, right_index = heapq.heappop(heap)
		yield value
		if left_index + 1 == len(left_items) :
			left_items.append(next(left))
		add_value(left_index + 1, right_index)
		if left_index == 0 :
			right_items.append(next(right))
			add_value(0, right_index + 1)


def increasing(fn, left, right) :
	left_items = [next(left)]
	right_items = [next(right)]
	columns = [(fn(left_items [0], right_items [0]), 0)]
	while True :
		min_col_index = min(xrange(len(columns)), key = lambda i : columns [i] [0])
		while right_items [0] < = columns [min_col_index] [0] and left_items [- 1] < = columns [min_col_index] [0] :
			next_left = next(left)
			left_items.append(next_left)
			columns.append((fn(next_left, right_items [0]), 0))
			if columns [- 1] [0] < columns [min_col_index] [0] :
				min_col_index = len(columns) - 1
		yield columns [min_col_index] [0]
		val, right_index = columns [min_col_index]
		while right_index + 1 > = len(right_items) :
			right_items.append(next(right))
		columns [min_col_index] = (fn(left_items [min_col_index], right_items [right_index + 1]),
		right_index + 1)

