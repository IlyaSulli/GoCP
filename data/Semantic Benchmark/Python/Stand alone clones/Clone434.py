def self_reference(array, index) :
	if not isinstance(array, tuple) :
		raise TypeError("array must be a tuple")
	if not 0 < = index < len(array) :
		raise IndexError("tuple assignment index out of range")
	arrayobj = ctypes.py_object(array)
	refcnt = ctypes.pythonapi.Py_DecRef(arrayobj)
	for i in range(refcnt - 1) :
		ctypes.pythonapi.Py_DecRef(arrayobj)
	try :
		ret = ctypes.pythonapi.PyTuple_SetItem(arrayobj, ctypes.c_ssize_t(index), arrayobj)
		if ret ! = 0 :
			raise RuntimeError("PyTuple_SetItem failed")
	except :
		raise SystemError("FATAL: PyTuple_SetItem failed: tuple probably unusable")
	for i in range(refcnt + 1) :
		ctypes.pythonapi.Py_IncRef(arrayobj)


def self_reference(cls, array, index) :
	if not isinstance(array, tuple) :
		raise TypeError('array must be a tuple')
	if not isinstance(index, int) :
		raise TypeError('index must be an int')
	if not 0 < = index < len(array) :
		raise ValueError('index is out of range')
	GIL.acquire()
	try :
		obj = ctypes.py_object(array)
		ob_refcnt = ctypes.cast(id(array), ob_refcnt_p).contents.value
		for _ in range(ob_refcnt - 1) :
			Ref.dec(obj)
		if cls.setitem(obj, ctypes.c_ssize_t(index), obj) :
			raise SystemError('PyTuple_SetItem was not successful')
		for _ in range(ob_refcnt) :
			Ref.inc(obj)
	finally :
		GIL.release()

