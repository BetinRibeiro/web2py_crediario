# -*- coding: utf-8 -*-
# tente algo comohttps://rogoberto.pythonanywhere.com/Sist01/projeto/listar_projetos
@cache.action(time_expire=300, cache_model=cache.ram, quick='P')
@auth.requires_login()
def listar_projetos():
	a = auth.user
	rows = db(db.projeto.created_by == auth.user).select()
	return locals()


def criar_projeto():
	conteudo = db.projeto(request.args(0, auth.user))
	form = SQLFORM(db.projeto).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_projetos'))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()


def alterar_projeto():
	projeto = db.projeto(request.args(0, cast=int))
	form = SQLFORM(db.projeto, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'Filme atualizado'
		redirect(URL('listar_projetos'))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()

@cache.action(time_expire=300, cache_model=cache.ram, quick='P')
def acesso_geral():
	proj = db.projeto(request.args(0, cast=int))
	return locals()

def info_antes_venda():
    proj = db.projeto(request.args(0, cast=int))
    rowsvendedor = db(db.vendedor.projeto == request.args(0, cast=int)).select()
    rowsfuncionario = db(db.funcionario_venda.projeto == request.args(0, cast=int)).select()
    rowsmercadoria = db(db.mercadoria_enviada.projeto == request.args(0, cast=int)).select()
    return locals()

@cache.action(time_expire=300, cache_model=cache.ram, quick='P')
def prestacao_venda():
	proj = db.projeto(request.args(0, cast=int))
        return response.render('projeto/prestacao_venda.html', locals())


def info_venda():
	projeto = db.projeto(request.args(0, cast=int))
	form = SQLFORM(db.projeto, request.args(0, cast=int))
    
	db.projeto.devolucao_dinh.readable = True
	db.projeto.devolucao_dinh.writable = True

    
	if form.process().accepted:
		session.flash = 'atualizado'
		redirect(URL('prestacao_venda', args=projeto.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()

def relatorio_investimento():
	proj = db.projeto(request.args(0, cast=int))
	return locals()
