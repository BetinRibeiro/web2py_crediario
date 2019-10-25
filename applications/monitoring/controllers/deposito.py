# -*- coding: utf-8 -*-

def listar_depositos():
	proj = db.projeto(request.args(0, cast=int))
	rows = db((db.deposito.projeto == request.args(0, cast=int))).select()
	return locals()


def inserir_deposito():
	proj = db.projeto(request.args(0, cast=int))
	db.deposito.projeto.default = proj.id
	db.deposito.projeto.readable = False
	db.deposito.projeto.writable = False
	merc = db(db.deposito.projeto==proj.id).select()
	form = SQLFORM(db.deposito).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_depositos', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()


def alterar_deposito():
	merc = db.deposito(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
	db.deposito.projeto.readable = False
	db.deposito.projeto.writable = False
	form = SQLFORM(db.deposito, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'Despesa atualizada'
		redirect(URL('listar_depositos', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()
