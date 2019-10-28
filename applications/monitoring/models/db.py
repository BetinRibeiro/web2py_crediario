# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    #db = DAL('sqlite://storage.sqlite', check_reserved=['postgres', 'mssql'])
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = False

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
# -*- coding: utf-8 -*-
db.define_table('projeto',
				#info_antes_venda
                Field('nome', 'string', notnull=True, label="Nome Projeto"),
				Field('nome_chefe', 'string', label="Nome Chefe"),
                Field('primeira_cidade', 'string', label="Primeira Cidade"),
				Field('vale_saida_chefe', 'double', label="Vale Chefe"),
				Field('adiantamento_dinh_venda', 'double', label="Adiant Dinh Venda"),
                Field('comissao_chefe_venda', 'double',  label="% Comissao Ven Chefe"),
                Field('data_saida_venda', 'date', label="Data Saida Venda"),
                Field('data_cobranca', 'date', label="Data Cobrança"),
				Field('comissao_chefe_cobranca', 'double', label="% Comissão Cob Chefe"),
                #info_chegada_Venda
				Field('devolucao_dinh_venda', 'double', label="Devol Dinh Venda"),
                Field('data_chegada_venda', 'date', label="Data Chegada Venda"),
                Field('ultima_cidade', 'string',label="Ultima Cidade"),
                Field('ultima_data_cobranca', 'date', label="Ultima Data Cobr"),
                #info_antes_cobranca
                Field('nome_cobrador', 'string', label="Nome Cobrador"),
				Field('comissao_cobrador', 'double', label="% Comissao Cobrador"),
				Field('vale_cobrador', 'double', label="Vale Cobrador"),
				Field('adiantamento_dinh_cobranca', 'double', label="Adiant Dinh Cobr",notnull=True, default=0),
                Field('data_saida_cobrador', 'date', label="Data saida Cobrador"),
                #info_chegada_venda
				Field('devolucao_dinh_cobranca', 'double', label="Devol Dinh Cobrança",notnull=True, default=0),
                Field('data_chegada_cobrador', 'date', label="Data Chegada Cobrador"),

				#informações das despesas (informação vem da tabela de despesas)
				Field('total_valor_depesa_local', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_valor_depesa_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_valor_depesa_cobranca', 'double', writable=False, readable=False, notnull=True, default=0),

				#Informações dos depositos (informação vem da tabela de Depositos)
				Field('total_valor_deposito', 'double', writable=False, readable=False, notnull=True, default=0),

				#informações Mercadoria (informação vem da tabela de Mercadoria)
				Field('total_quant_pcs_envio', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_preco_envio', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_custo_envio', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_quant_pcs_retorno', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_preco_retorno', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_custo_retorno', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_custo_aprov_retorno', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_quant_pcs_devolucao', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_preco_devolucao', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_custo_devolucao', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_custo_aprov_devolucao', 'double', writable=False, readable=False, notnull=True, default=0),

				#informações Funcionario (informação vem da tabela de Funcionario)
				Field('total_salario', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_vale_saida_funcionario', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_vale_caderno_funcionario', 'double', writable=False, readable=False, notnull=True, default=0),
                Field('total_recebido_chegada_funcionario', 'double', writable=False, readable=False, notnull=True, default=0),

                #informações vendedor (informação que vem da tabela de vendedor)
				Field('total_vale_saida_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_vale_caderno_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_entradas_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_quant_fichas', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_comis_venda_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_recebido_chegada_venda_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_recebido_cobranca', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_devolvido_cobranca', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_prego_cobranca', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_recebido_chegada_cobranca_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
                auth.signature)

db.define_table('deposito',
				Field('projeto','reference projeto', label='Equipe',  writable=True, readable=True),
				Field('descricao', 'string', notnull=True, default="Descrição"),
				Field('valor_deposito', 'double', notnull=True, default=0),
				Field('data_deposito','date'),
				auth.signature)

db.define_table('despesa',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('descricao', 'string', notnull=True, default="Valor Gasto"),
				Field('valor', 'double', notnull=True, default=0),
				Field('tipo_desp','string', writable=False, readable=False,notnull=True, default=""),
				auth.signature)

db.define_table('mercadoria',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('quant_pcs_enviada', 'integer', notnull=True, default=0),
				Field('descricao', 'string', notnull=True),
				Field('preco_unitario', 'double', notnull=True, default=0),
				Field('custo_unitario', 'double', notnull=True, default=0),
				Field('quant_pcs_retorno', 'integer', default=0, notnull=True),
				Field('quant_pcs_aprov_retorno', 'integer', default=0, notnull=True),
				Field('quant_pcs_devolucao', 'integer', default=0, notnull=True),
				Field('quant_pcs_aprov_devolucao', 'integer', default=0, notnull=True),
				auth.signature)

db.define_table('funcionario',
				Field('projeto','reference projeto', label='Equipe'),
				Field('nome_funcionario', 'string'),
				Field('funcao', 'string'),
				Field('salario_funcionario', 'double',  notnull=True, default=1000),
				Field('vale_saida_funcionario', 'double', notnull=True, default=0),
				Field('vale_caderno_funcionario', 'double',  notnull=True, default=0),
				Field('valor_recebido_chegada', 'double',  notnull=True, default=0),
				auth.signature)

db.define_table('vendedor',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('nome_vendedor', 'string'),
				Field('vale_saida', 'double'),
				Field('vale_caderno', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('entradas_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('quant_fichas', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('comissao_venda', 'double', writable=False, readable=False, notnull=True, default=7),
				Field('valor_receb_chegada_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('recebido_cobranca', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('devolvido_cobranca', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('prego_cobranca', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('comissao_cobranca', 'double', writable=False, readable=False, notnull=True, default=10),
				Field('valor_receb_chegada_cobra','double', writable=False, readable=False, notnull=True, default=0),
				auth.signature)
