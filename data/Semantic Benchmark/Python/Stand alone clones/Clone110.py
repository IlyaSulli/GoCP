def moto_boto() :
	mock_s3().start()
	res = boto3.resource('s3')
	res.create_bucket(Bucket = BUCKET)
	yield
	mock_s3.stop()


def moto_boto() :
	@ mock_s3
	def boto_resource() :
		res = boto3.resource('s3')
		res.create_bucket(Bucket = BUCKET)
		return res
	return boto_resource

