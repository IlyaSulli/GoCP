def transitive_closure(elements) :
	edges = defaultdict(set)
	for x, y in elements : edges [x].add(y)
	for _ in range(len(elements) - 1) :
		edges = defaultdict(set, (
		(k, v.union(* (edges [i] for i in v))) for (k, v) in edges.items()
		))
	return set((k, i) for (k, v) in edges.items() for i in v)


def transitive_closure(elements) :
	elements = set([(x, y) if x < y else (y, x) for x, y in elements])
	relations = {}
	for x, y in elements :
		if x not in relations :
			relations [x] = []
		relations [x].append(y)
	closure = set()
	def build_closure(n) :
		def f(k) :
			for y in relations.get(k, []) :
				closure.add((n, y))
				f(y)
		f(n)
	for k in relations.keys() :
		build_closure(k)
	return closure

