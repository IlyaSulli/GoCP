def urls() :
	conn = sqlite3.connect('C:\Users\username\Desktop\History.sql')
	c = conn.cursor()
	query = "SELECT url, title FROM urls"
	c.execute(query)
	data = c.fetchall()
	if data :
		with open("C:\Users\username\Desktop\\historyulrs.csv", 'w') as outfile :
			writer = csv.writer(outfile)
			writer.writerow(['URL', 'Title'])
			for entry in data :
				writer.writerow([str(entry [0]), str(entry [1])])


def urls() :
	urls = []
	titles = []
	counts = []
	last = []
	conn = sqlite3.connect('C:\Users\username\Desktop\History.sql')
	cursor = conn.execute("SELECT url, title, visit_count, last_visit_time from urls")
	for row in cursor :
		urls.append(row [0])
		titles.append(row [1])
		counts.append(row [2])
		last.append(row [3])
	df = pandas.DataFrame({'URL' : urls,
	'Title' : titles,
	'Visit Count' : counts,
	'Last visit Time' : last})
	df.to_csv('historyulrs.csv', encoding = 'utf-8', index = False)
	conn.close()

