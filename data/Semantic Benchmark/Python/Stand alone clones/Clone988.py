def run_query(query, database, s3_output) :
	client = boto3.client('athena')
	response = client.start_query_execution(
	QueryString = query,
	QueryExecutionContext = {
	'Database' : database},
	ResultConfiguration = {
	'OutputLocation' : s3_output,
	})
	print ('Execution ID: ' + response ['QueryExecutionId'])
	return response


def run_query(self) :
	queries = [self.query]
	for q in queries :
		res = self.load_conf(q)
	try :
		query_status = None
		while query_status == 'QUEUED' or query_status == 'RUNNING' or query_status is None :
			query_status = self.client.get_query_execution(QueryExecutionId = res ["QueryExecutionId"]) ['QueryExecution'] ['Status'] ['State']
			print (query_status)
			if query_status == 'FAILED' or query_status == 'CANCELLED' :
				raise Exception('Athena query with the string "{}" failed or was cancelled'.format(self.query))
			time.sleep(10)
		print ("Query %s finished.")
		df = self.obtain_data()
		return df
	except Exception as e :
		print (e)

