def token_list_count(df) :
	dfIterrows = df.iterrows()
	for i, t in dfIterrows :
		list_a = 0
		list_b = 0
		tTokens = t ['tokens']
		for tok in tTokens :
			if tok in seta : list_a += 1
			elif tok in setb : list_b += 1
		df.loc [i, 'token_count'] = int(len(t ['tokens']))
		df.loc [i, 'lista_count'] = int(list_a)
		df.loc [i, 'listb_count'] = int(list_b)
		if i % 25000 == 0 : print ('25k more processed...')
	return df


def token_list_count(df) :
	for i, tok in df.tokens.iteritems() :
		list_a = sum((t in lista) for t in tok)
		list_b = sum((t in listb) for t in tok)
		df.at [i, 'token_count'] = int(len(tok))
		df.at [i, 'lista_count'] = int(list_a)
		df.at [i, 'listb_count'] = int(list_b)
		if i % 25000 == 0 : print ('25k more processed...')
	return df

