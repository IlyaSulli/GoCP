def transitive_closure(a) :
	closure = set()
	for x, _ in a :
		closure |= set((x, y) for y in dfs(x, a))
	return closure


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

