def transitive_closure(elements) :
	edges = defaultdict(set)
	for x, y in elements : edges [x].add(y)
	for _ in range(len(elements) - 1) :
		edges = defaultdict(set, (
		(k, v.union(* (edges [i] for i in v))) for (k, v) in edges.items()
		))
	return set((k, i) for (k, v) in edges.items() for i in v)


def transitive_closure(a) :
	closure = set()
	for x, _ in a :
		closure |= set((x, y) for y in dfs(x, a))
	return closure

