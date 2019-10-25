# -*- coding: utf-8 -*-
# tente algo como

def listar_desp_local():
	proj = db.projeto(request.args(0, cast=int))
	rows = db((db.despesa.projeto == request.args(0, cast=int))& (db.despesa.tipo_desp == "Local") ).select()
	return locals()


def listar_desp_venda():
	proj = db.projeto(request.args(0, cast=int))
	rows = db((db.despesa.projeto == request.args(0, cast=int)) & (db.despesa.tipo_desp == "Venda") ).select()
	return locals()


def listar_desp_cobranca():
	proj = db.projeto(request.args(0, cast=int))
	rows = db((db.despesa.projeto == request.args(0, cast=int))& (db.despesa.tipo_desp == "Cobranca") ).select()
	return locals()

def inserir_desp_local():
	proj = db.projeto(request.args(0, cast=int))
	db.despesa.projeto.default = proj.id
	db.despesa.projeto.readable = False
	db.despesa.projeto.writable = False

	db.despesa.tipo_desp.default = "Local"
	db.despesa.tipo_desp.readable = True
	db.despesa.tipo_desp.writable = False
	merc = db(db.despesa.projeto==proj.id).select()
	form = SQLFORM(db.despesa).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_desp_local', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()


def alterar_desp_local():
	merc = db.despesa(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.despesa.projeto.readable = False
	db.despesa.projeto.writable = False
	form = SQLFORM(db.despesa, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'Despesa atualizada'
		redirect(URL('listar_desp_local', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()


def inserir_desp_venda():
	proj = db.projeto(request.args(0, cast=int))
	db.despesa.projeto.default = proj.id
	db.despesa.projeto.readable = False
	db.despesa.projeto.writable = False

	db.despesa.tipo_desp.default = "Venda"
	db.despesa.tipo_desp.readable = True
	db.despesa.tipo_desp.writable = False
	merc = db(db.despesa.projeto==proj.id).select()
	form = SQLFORM(db.despesa).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_desp_venda', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()


def alterar_desp_venda():
	merc = db.despesa(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.despesa.projeto.readable = False
	db.despesa.projeto.writable = False
	form = SQLFORM(db.despesa, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'Despesa atualizada'
		redirect(URL('listar_desp_venda', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()


def inserir_desp_cobranca():
	proj = db.projeto(request.args(0, cast=int))
	db.despesa.projeto.default = proj.id
	db.despesa.projeto.readable = False
	db.despesa.projeto.writable = False

	db.despesa.tipo_desp.default = "Cobranca"
	db.despesa.tipo_desp.readable = True
	db.despesa.tipo_desp.writable = False
	merc = db(db.despesa.projeto==proj.id).select()
	form = SQLFORM(db.despesa).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_desp_cobranca', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()


def alterar_desp_cobranca():
	merc = db.despesa(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.despesa.projeto.readable = False
	db.despesa.projeto.writable = False
	form = SQLFORM(db.despesa, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'Despesa atualizada'
		redirect(URL('listar_desp_cobranca', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()
