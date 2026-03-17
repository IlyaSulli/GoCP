def roundrobin(* iterables) :
	"roundrobin('ABC', 'D', 'EF') --> A D E B F C"
	num_active = len(iterables)
	nexts = cycle(iter(it).__next__ for it in iterables)
	while num_active :
		try :
			for next in nexts :
				yield next()
		except StopIteration :
			num_active -= 1
			nexts = cycle(islice(nexts, num_active))


def roundrobin(* iterables) :
	sentinel = object()
	from itertools import chain
	try :
		from itertools import izip_longest as zip_longest
	except :
		from itertools import zip_longest
	return (x for x in chain(* zip_longest(fillvalue = sentinel, * iterables)) if x is not sentinel)

