# -*- coding: utf-8 -*-
Projeto = db.define_table('projeto',
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
				Field('adiantamento_dinh_cobranca', 'double', label="Adiant Dinh Cobr"),
                Field('data_saida_cobrador', 'date', label="Data saida Cobrador"),
                #info_chegada_venda
				Field('devolucao_dinh_cobranca', 'double', label="Devol Dinh Cobrança"),
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
                Field('total_recebido_chegada', 'double', writable=False, readable=False, notnull=True, default=0),

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


Deposito = db.define_table('deposito',
				Field('projeto','reference projeto', label='Equipe',  writable=True, readable=True),
				Field('descricao', 'string'),
				Field('valor_deposito', 'double'),
				Field('data_deposito','date'),
				auth.signature)

Despesa = db.define_table('despesa',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('descricao', 'string'),
				Field('valor', 'double'),
				Field('tipo_desp','string'),
				auth.signature)

Mercadoria = db.define_table('mercadoria',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('quant_pcs_enviada', 'integer'),
				Field('descricao', 'string'),
				Field('preco_unitario', 'double'),
				Field('custo_unitario', 'double'),
				Field('quant_pcs_retorno', 'integer', default=0, notnull=True),
				Field('quant_pcs_aprov_retorno', 'integer', default=0, notnull=True),
				Field('quant_pcs_devolucao', 'integer', default=0, notnull=True),
				Field('quant_pcs_aprov_devolucao', 'integer', default=0, notnull=True),
				auth.signature)

Funcionario = db.define_table('funcionario',
				Field('projeto','reference projeto', label='Equipe'),
				Field('nome_funcionario', 'string'),
				Field('funcao', 'string'),
				Field('salario_funcionario', 'double'),
				Field('vale_saida_funcionario', 'double'),
				Field('vale_caderno_funcionario', 'double'),
				Field('valor_recebido_chegada', 'double'),
				auth.signature)

Vendedor = db.define_table('vendedor',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('nome_vendedor', 'string'),
				Field('vale_saida', 'double'),
				Field('vale_caderno', 'double'),
				Field('venda', 'double'),
				Field('entradas_venda', 'double'),
				Field('quant_fichas', 'integer'),
				Field('comissao_venda', 'double'),
				Field('valor_receb_chegada_venda', 'double'),
				Field('recebido_cobranca', 'double'),
				Field('devolvido_cobranca', 'double'),
				Field('prego_cobranca', 'double'),
				Field('comissao_cobranca', 'double'),
				Field('valor_receb_chegada_cobra','double'),
				auth.signature)