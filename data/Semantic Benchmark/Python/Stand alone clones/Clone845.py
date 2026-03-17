def __new__(mcls, name, bases, namespace) :
	cls = type.__new__(mcls, name, bases, namespace)
	abstracts = set(name for name, value in namespace.items()
	if getattr(value, "__isabstractmethod__", False))
	for base in cls.__mro__ :
		for name, value in base.__dict__.items() :
			if getattr(value, "__isabstractmethod__", False) and name not in cls.__dict__ :
				abstracts.add(name)
	cls.__abstractmethods__ = frozenset(abstracts)
	cls._abc_registry = WeakSet()
	cls._abc_cache = WeakSet()
	cls._abc_negative_cache = WeakSet()
	cls._abc_negative_cache_version = ABCMeta._abc_invalidation_counter
	return cls


def __new__(mcls, name, bases, namespace) :
	cls = super(ABCMeta, mcls).__new__(mcls, name, bases, namespace)
	abstracts = set()
	for base in bases :
		abstracts.update(getattr(base, "_all_always_override", set()))
	all_abstracts = abstracts.copy()
	for name, value in namespace.items() :
		always_override = getattr(value, '_always_override', False)
		if always_override :
			abstracts.add(name)
			all_abstracts.add(name)
		elif name in abstracts :
			abstracts.remove(name)
	cls._all_always_override = frozenset(all_abstracts)
	cls._always_override = frozenset(abstracts)
	return cls

