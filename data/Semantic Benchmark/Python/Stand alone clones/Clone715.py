def setUp(self) :
	logging.getLogger().setLevel(logging.DEBUG)
	tb = testbed.Testbed()
	tb.setup_env(current_version_id = 'testbed.version')
	tb.activate()
	tb.init_all_stubs()
	self.testbed = tb


def setUp(self) :
	APP_CONFIGS = ['/path/to/app.yaml']
	python_runtime._RUNTIME_ARGS = [
	sys.executable,
	os.path.join(os.path.dirname(dev_appserver.__file__),
	'_python_runtime.py')]
	options = devappserver2.PARSER.parse_args([
	'--admin_port', '0',
	'--port', '8123',
	'--datastore_path', ':memory:',
	'--logs_path', ':memory:',
	'--skip_sdk_update_check',
	'--',
	] + APP_CONFIGS)
	server = devappserver2.DevelopmentServer()
	server.start(options)
	self.server = server

