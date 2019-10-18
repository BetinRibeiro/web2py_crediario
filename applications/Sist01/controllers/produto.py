# -*- coding: utf-8 -*-
# tente algo como

def listar_merc_envio():
	proj = db.projeto(request.args(0, cast=int))
	rows = db(db.mercadoria_enviada.projeto == request.args(0, cast=int)).select()
	return locals()

def inserir_merc_envio():
	proj = db.projeto(request.args(0, cast=int))
	db.mercadoria_enviada.projeto.default = proj.id
	db.mercadoria_enviada.projeto.readable = False
	db.mercadoria_enviada.projeto.writable = False
	merc = db(db.mercadoria_enviada.projeto==proj.id).select()
	form = SQLFORM(db.mercadoria_enviada).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_merc_envio', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()

def alterar_merc_envio():
	merc = db.mercadoria_enviada(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.mercadoria_enviada.projeto.readable = False
	db.mercadoria_enviada.projeto.writable = False
	form = SQLFORM(db.mercadoria_enviada, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'atualizada'
		redirect(URL('listar_merc_envio', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()


def subir_dados_mercadoria_envio():
	iid = request.args(0, cast=int)
	quant = request.args(1)
	custo = request.args(3)
	preco = request.args(2)
	proj = db(db.projeto.id == iid).select().first()
	proj.update_record(total_custo_envio=custo)
	proj.update_record(total_quantidade_envio=quant)
	proj.update_record(total_preco_envio=preco)
	db.projeto.total_quantidade_envio.readable = True
	db.projeto.total_quantidade_envio.writable = False
	db.projeto.total_preco_envio.readable = True
	db.projeto.total_preco_envio.writable = False
	db.projeto.total_custo_envio.readable = True
	db.projeto.total_custo_envio.writable = False
	
	
	db.projeto.nome.readable = False
	db.projeto.nome.writable = False
	
	db.projeto.nome_chefe.readable = False
	db.projeto.nome_chefe.writable = False
	
	db.projeto.vale_saida_chefe.readable = False
	db.projeto.vale_saida_chefe.writable = False
	
	db.projeto.comissao_chefe.readable = False
	db.projeto.comissao_chefe.writable = False
	
	db.projeto.data_saida_venda.readable = False
	db.projeto.data_saida_venda.writable = False
	
	db.projeto.adiantamento_saida_venda.readable = False
	db.projeto.adiantamento_saida_venda.writable = False
	
	db.projeto.data_cobranca.readable = False
	db.projeto.data_cobranca.writable = False
	
	db.projeto.primeira_cidade.readable = False
	db.projeto.primeira_cidade.writable = False
	
	form = SQLFORM(db.projeto, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = ' atualizado'
		redirect(URL('listar_merc_envio', args=iid))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()

def listar_merc_retorno():
	proj = db.projeto(request.args(0, cast=int))
	rows = db(db.mercadoria_retorno.projeto == request.args(0, cast=int)).select()
	return locals()

def inserir_merc_retorno():
	proj = db.projeto(request.args(0, cast=int))
	db.mercadoria_retorno.projeto.default = proj.id
	db.mercadoria_retorno.projeto.readable = False
	db.mercadoria_retorno.projeto.writable = False
	merc = db(db.mercadoria_retorno.projeto==proj.id).select()
	form = SQLFORM(db.mercadoria_retorno).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_merc_retorno', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()

def alterar_merc_retorno():
	merc = db.mercadoria_retorno(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.mercadoria_retorno.projeto.readable = False
	db.mercadoria_retorno.projeto.writable = False
	form = SQLFORM(db.mercadoria_retorno, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'atualizada'
		redirect(URL('listar_merc_retorno', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()


def subir_dados_mercadoria_retorno():
	iid = request.args(0, cast=int)
	quant = request.args(1)
	custo = request.args(3)
	preco = request.args(2)
	proj = db(db.projeto.id == iid).select().first()
	proj.update_record(total_custo_retorno=custo)
	proj.update_record(total_quantidade_retorno=quant)
	proj.update_record(total_preco_retorno=preco)
	db.projeto.total_quantidade_retorno.readable = True
	db.projeto.total_quantidade_retorno.writable = False
	db.projeto.total_preco_retorno.readable = True
	db.projeto.total_preco_retorno.writable = False
	db.projeto.total_custo_retorno.readable = True
	db.projeto.total_custo_retorno.writable = False
	
	db.projeto.nome.readable = False
	db.projeto.nome.writable = False
	
	db.projeto.nome_chefe.readable = False
	db.projeto.nome_chefe.writable = False
	
	db.projeto.vale_saida_chefe.readable = False
	db.projeto.vale_saida_chefe.writable = False
	
	db.projeto.comissao_chefe.readable = False
	db.projeto.comissao_chefe.writable = False
	
	db.projeto.data_saida_venda.readable = False
	db.projeto.data_saida_venda.writable = False
	
	db.projeto.adiantamento_saida_venda.readable = False
	db.projeto.adiantamento_saida_venda.writable = False
	
	db.projeto.data_cobranca.readable = False
	db.projeto.data_cobranca.writable = False
	
	db.projeto.primeira_cidade.readable = False
	db.projeto.primeira_cidade.writable = False
	
	form = SQLFORM(db.projeto, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = ' atualizado'
		redirect(URL('listar_merc_retorno', args=iid))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()
