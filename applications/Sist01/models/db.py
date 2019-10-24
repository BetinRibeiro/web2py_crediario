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
auth.settings.reset_password_requires_verification = True

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


db.define_table('projeto',
				#criação do projeto
                Field('nome', 'string', default="Projeto01"),
				Field('nome_chefe', 'string', writable=True),
				Field('primeira_cidade', 'string', writable=True),
                
				Field('vale_saida_chefe', 'double', default=1, writable=True, readable=True),
				Field('adiantamento_saida_venda', 'double', default=1, writable=True, readable=True),
				Field('devolucao_dinh', 'double', default=1, writable=True, readable=True),
				Field('comissao_chefe_venda', 'double', default=1, writable=True, readable=True),
                
				Field('data_saida_venda', 'date', writable=True, readable=True),
				Field('data_cobranca', 'date', writable=True, readable=True),

				#informações das despesas
				Field('total_valor_depesa_local', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_valor_depesa_venda', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_valor_depesa_cobranca', 'double', default=1, writable=False, readable=False, notnull=True),

				#Informações dos depositos
				Field('total_valor_deposito', 'double', default=1, writable=False, readable=False, notnull=True),

				#informações Mercadoria Envio
				Field('total_quantidade_envio', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_preco_envio', 'double',default=1, writable=False, readable=False, notnull=True),
				Field('total_custo_envio', 'double', default=1.0, writable=False, readable=False, notnull=True),

				#informações Mercadoria Retorno
				Field('total_quantidade_retorno', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_preco_retorno', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_custo_retorno', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_custo_aproveitamento', 'double', default=1, writable=False, readable=False, notnull=True),

				#informações Mercadoria
				Field('total_quantidade_devolucao', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_preco_devolucao', 'double',default=1,writable=False, readable=False, notnull=True),
				Field('total_custo_devolucao', 'double',default=1,  writable=False, readable=False, notnull=True),
				Field('total_custo_aproveitamento_devolucao', 'double',default=1, writable=False, readable=False, notnull=True),

				Field('total_salario', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_vale_saida_funcionario', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_vale_caderno_funcionario', 'double', default=1, writable=False, readable=False, notnull=True),

				Field('total_vale_saida_vendedor', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_vale_caderno_vendedor', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_venda', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_entradas_venda', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_quantidade_fichas', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_comissao_vendedor', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_recebido_cobranca', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_devolvido_cobranca', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_prego_cobranca', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('total_saldo', 'double', default=1, writable=False, readable=False, notnull=True),



				Field('data_chegada_venda', 'date', writable=False, readable=False),
                
				Field('ultima_cidade', 'string', writable=False, readable=False, notnull=True),
                
				Field('comissao_chefe', 'double', default=1, writable=False, readable=False, notnull=True),

				Field('nome_cobrador', 'string', writable=False, readable=False, notnull=True),
				Field('comissao_cobrador', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('vale_cobrador', 'double', default=1, writable=False, readable=False, notnull=True),
				Field('adiantamento_saida_cobranca', 'double', default=1, writable=False, readable=False, notnull=True),
                
				Field('data_chegada_cobranca', 'date', writable=False, readable=False),
				Field('retorno_dinheiro', 'double', default=1, writable=False, readable=False, notnull=True),
				auth.signature)




db.define_table('deposito_cobranca',
				Field('projeto','reference projeto', label='Equipe',  writable=True, readable=True),
				Field('descricao', 'string', label='Descrição', default='Cidade', writable=True, readable=True),
				Field('valor_deposito', 'double', label='Valor', default=0, writable=True, readable=True),
				Field('data_deposito','date', label='Data', writable=True, readable=True),
				auth.signature)

db.define_table('despesa_local',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('descricao', 'string', label='Descrição', default='Tipo de Despesa', writable=True, readable=True),
				Field('valor', 'double', default=0, writable=True, readable=True),
				Field('data_desp_local','date', writable=True, readable=True),
				auth.signature)

db.define_table('despesa_venda',
				Field('projeto','reference projeto', label='Equipe', writable=True),
				Field('descricao', 'string', label='Descrição', default='Tipo de Despesa', writable=True, readable=True),
				Field('valor', 'double', default=0, writable=True, readable=True),
				Field('data_despesa','date', writable=True, readable=True),
				auth.signature)


db.define_table('despesa_cobranca',
				Field('projeto','reference projeto', label='Equipe', writable=True),
				Field('descricao', 'string', label='Descrição', default='Tipo de Despesa', writable=True, readable=True),
				Field('valor', 'double', default=0, writable=True),
				Field('data_cobranca', 'date', writable=True),
				auth.signature)

db.define_table('entrada_dinheiro_venda',
				Field('projeto','reference projeto', label='Equipe', writable=True),
				Field('descricao', 'string', label='Descrição', default='Tipo de Despesa', writable=True, readable=True),
				Field('valor', 'double', default=0, writable=True),
				Field('data_ent_venda', 'date', writable=True),
				auth.signature)

Saida = db.define_table('saida_dinheiro_venda',
				Field('projeto','reference projeto', label='Equipe', writable=True),
				Field('descricao', 'string', label='Descrição', default='Tipo de Despesa', writable=True, readable=True),
				Field('valor', 'double', default=0, writable=True),
				Field('data_saida_cobranca', 'date', writable=True),
				auth.signature)

db.define_table('vendedor',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('nome_vendedor', 'string',label='Nome',default='Nome', writable=True, readable=True),
				Field('vale_saida', 'double', label='Vale',default=0, writable=True, readable=True),
				Field('vale_caderno', 'double',label='Caderno', default=0, writable=False, readable=False),
				Field('venda', 'double', label='Venda',default=0, writable=False, readable=False),
				Field('entradas_venda', 'double',label='Entradas',default=0, writable=False, readable=False),
				Field('quantidade_fichas', 'double',label='Q.Fichas', default=0, writable=False, readable=False),
				Field('comissao_venda', 'double', default=0,label='Comissão vend%', writable=True, readable=True),
				Field('saldo_venda_vendedor', 'double',label='Saldo', default=0, writable=False, readable=False),
				Field('recebido_cobranca', 'double',label='Recebido', default=0, writable=False, readable=False),
				Field('devolvido_cobranca', 'double',label='Devolvido', default=0, writable=False, readable=False),
				Field('prego_cobranca', 'double',label='Prego', default=0, writable=False, readable=False),
				Field('comissao_cobranca', 'double',label='Comissão cob%', default=0, writable=True, readable=True),
					Field('complemento_recebido','double',label='Complemento Recebido', default=0, writable=False, readable=False),
				auth.signature)


db.define_table('mercadoria_enviada',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('quantidade', 'double',label='Quant', default=0, writable=True, readable=True),
				Field('descricao', 'string',label='Descrição', writable=True, readable=True),
				Field('preco_unitario', 'double',label='Preço UND', default=0, writable=True, readable=True),
				Field('custo_unitario', 'double',label='Custo UND', default=0, writable=True, readable=True),
				auth.signature)


db.define_table('mercadoria_retorno',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('quantidade', 'double',label='Quant', default=0, writable=True, readable=True),
				Field('descricao', 'string',label='Descrição', writable=True, readable=True),
				Field('preco_unitario', 'double',label='Preço UND', default=0, writable=True, readable=True),
				Field('custo_unitario', 'double',label='Custo UND', default=0, writable=True, readable=True),
				Field('quantidade_reaproveitado','double',label='Pças Aproveitadas', default=0, writable=True, readable=True),
				auth.signature)

db.define_table('mercadoria_devolvida',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('quantidade', 'double',label='Quant', default=0, writable=True, readable=True),
				Field('descricao', 'string',label='Descrição', writable=True, readable=True),
				Field('preco_unitario', 'double',label='Preço UND', default=0, writable=True, readable=True),
				Field('custo_unitario', 'double',label='Custo UND', default=0, writable=True, readable=True),
				Field('quantidade_reaproveitado','double',label='Pças Aproveitadas', default=0, writable=True, readable=True),
				auth.signature)


db.define_table('funcionario_venda',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('nome', 'string',label='Nome', writable=True, readable=True),
				Field('funcao', 'string', label='Função',writable=True, readable=True),
				Field('salario', 'double',label='Salario', default=0, writable=True, readable=True),
				Field('vale_saida', 'double',label='Vale', default=0, writable=True, readable=True),
				Field('vale_caderno', 'double',label='Caderno', default=0, writable=True, readable=True),
                
				Field('complemento_recebido', 'double',label='Complemento', default=0, writable=True, readable=True),
				auth.signature)
