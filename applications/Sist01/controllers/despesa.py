# -*- coding: utf-8 -*-
# tente algo como

def listar_despesa_venda():
	proj = db.projeto(request.args(0, cast=int))
	rows = db(db.despesa_venda.projeto == request.args(0, cast=int)).select()
	return locals()

def inserir_despesa_venda():
	proj = db.projeto(request.args(0, cast=int))
	db.despesa_venda.projeto.default = proj.id
	db.despesa_venda.projeto.readable = False
	db.despesa_venda.projeto.writable = False
	merc = db(db.despesa_venda.projeto==proj.id).select()
	form = SQLFORM(db.despesa_venda).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_despesa_venda', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()

def alterar_despesa_venda():
	merc = db.despesa_venda(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.despesa_venda.projeto.readable = False
	db.despesa_venda.projeto.writable = False
	form = SQLFORM(db.despesa_venda, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'Despesa atualizada'
		redirect(URL('listar_despesa_venda', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()


def subir_dados_despesa_venda():
	iid = request.args(0, cast=int)
	total = request.args(1)
	
	proj = db(db.projeto.id == iid).select().first()
	proj.update_record(total_valor_depesa_venda=total)
	
	db.projeto.total_valor_depesa_venda.readable = True
	db.projeto.total_valor_depesa_venda.writable = False
	
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
		redirect(URL('listar_despesa_venda', args=iid))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()
