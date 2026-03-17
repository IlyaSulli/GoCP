def _get_modules_from_db(dictionary) :
	leaves = []
	for k, v in dictionary.iteritems() :
		if (isinstance(v, dict) and
		not sorted(v.keys()) == ['path_to_file', 'sha512sum']) :
			leaves.extend(_get_modules_from_db(v))
		else :
			leaves.append(v)
	return leaves


def _get_modules_from_db(db, leaves = None) :
	if leaves is None :
		leaves = []
	if not isinstance(db, dict) :
		return leaves
	if 'path_to_file' in db and 'checksum' in db :
		leaves.append(db)
	else :
		for v in db.values() :
			_get_modules_from_db(v, leaves)
	return leaves

