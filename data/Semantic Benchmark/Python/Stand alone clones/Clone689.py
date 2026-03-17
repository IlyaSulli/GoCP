def upgrade() :
	url = context.config.get_main_option("sqlalchemy.url")
	engine = sa.create_engine(url)
	DBSession.configure(bind = engine)
	op.create_table(
	'client_credential',
	sa.Column('id', sa.Integer(), nullable = False),
	sa.Column('created_at', sa.DateTime(), nullable = False),
	sa.Column('updated_at', sa.DateTime(), nullable = False),
	sa.Column('client_id', sa.Integer(), nullable = False),
	sa.Column('key', sa.String(length = 22), nullable = False),
	sa.Column('secret', sa.String(length = 44), nullable = False),
	sa.Column('is_active', sa.Boolean(), nullable = False),
	sa.ForeignKeyConstraint(['client_id'], ['client.id'],),
	sa.PrimaryKeyConstraint('id'),
	sa.UniqueConstraint('key'))
	clients = [
	{'secret' : client.secret,
	'key' : client.key,
	'is_active' : True,
	'client_id' : client.id,
	'created_at' : sa.func.now(),
	'updated_at' : sa.func.now()} for client in Client.query.all()]
	op.bulk_insert(ClientCredential, clients)
	op.drop_column(u'client', u'secret')
	op.drop_column(u'client', u'key')


def upgrade() :
	op.create_table('client_credential',
	sa.Column('id', sa.Integer(), nullable = False),
	sa.Column('created_at', sa.DateTime(), nullable = False),
	sa.Column('updated_at', sa.DateTime(), nullable = False),
	sa.Column('client_id', sa.Integer(), nullable = False),
	sa.Column('key', sa.String(length = 22), nullable = False),
	sa.Column('secret', sa.String(length = 44), nullable = False),
	sa.Column('is_active', sa.Boolean(), nullable = False),
	sa.ForeignKeyConstraint(['client_id'], ['client.id'],),
	sa.PrimaryKeyConstraint('id'),
	sa.UniqueConstraint('key'))
	client_credential = sa.sql.table('client_credential',
	sa.Column('client_id', sa.Integer, nullable = False),
	sa.Column('is_active', sa.Boolean, nullable = False, default = True),
	sa.Column('key', sa.String(22), nullable = False, default = True),
	sa.Column('secret', sa.String(22), nullable = False, default = True),
	sa.Column('created_at', sa.DateTime, nullable = False, default = sa.func.now()),
	sa.Column('updated_at', sa.DateTime, nullable = False, default = sa.func.now()),
	)
	conn = op.get_bind()
	res = conn.execute("select secret, key, id from client")
	results = res.fetchall()
	clients = [{'secret' : r [0], 'key' : r [1], 'is_active' : True, 'client_id' : r [2], 'created_at' : datetime.datetime.now(), 'updated_at' : datetime.datetime.now()} for r in results]
	op.bulk_insert(client_credential, clients)
	op.drop_column(u'client', u'secret')
	op.drop_column(u'client', u'key')

