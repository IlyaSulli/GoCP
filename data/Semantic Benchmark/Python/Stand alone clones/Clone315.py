def records(currentTime = Decimal('1.00')) :
	first = True
	while True :
		token = lexer.get_token()
		if token :
			token = token.strip()
			if not token :
				break
		else :
			break
		token = token.replace('\n', '')
		if Decimal(token) == currentTime :
			if first :
				first = False
			else :
				yield record
			currentTime += Decimal('0.1')
			record = [float(token)]
		else :
			record.append(float(token))
	yield record


def records(currentTime = Decimal('1.00')) :
	first = True
	previousChunk = ''
	exhaustedInput = False
	while True :
		chunk = sample.read(50)
		if not chunk :
			exhaustedInput = True
			chunk = previousChunk
		else :
			chunk = (previousChunk + chunk).replace('\n', '')
		items = chunk.split()
		for number in items [: len(items) if exhaustedInput else - 1] :
			if Decimal(number) == currentTime :
				if first :
					first = False
				else :
					yield record
				record = [number]
				currentTime += Decimal('0.1')
			else :
				record.append(number)
		if exhaustedInput :
			yield record
			break
		else :
			previousChunk = chunk.split() [- 1]

