def roundrobin(* iterables) :
	"roundrobin('ABC', 'D', 'EF') --> A D E B F C"
	pending = len(iterables)
	nexts = cycle(iter(it).next for it in iterables)
	while pending :
		try :
			for next in nexts :
				yield next()
		except StopIteration :
			pending -= 1
			nexts = cycle(islice(nexts, pending))


def roundrobin(* iterables) :
	sentinel = object()
	from itertools import chain
	try :
		from itertools import izip_longest as zip_longest
	except :
		from itertools import zip_longest
	return (x for x in chain(* zip_longest(fillvalue = sentinel, * iterables)) if x is not sentinel)

