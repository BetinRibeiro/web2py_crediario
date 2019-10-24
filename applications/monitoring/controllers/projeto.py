# -*- coding: utf-8 -*-
# tente algo como
def prestacao_venda():
    return locals()
def prestacao_cobranca():
    return locals()

def acesso_geral_projeto():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()

def alterar_projeto():
    projeto = db.projeto(request.args(0, cast=int))


    db.projeto.adiantamento_dinh_cobranca.readable = False
    db.projeto.adiantamento_dinh_cobranca.writable = False

    db.projeto.comissao_cobrador.readable = False
    db.projeto.comissao_cobrador.writable = False

    db.projeto.data_chegada_cobrador.readable = False
    db.projeto.data_chegada_cobrador.writable = False

    db.projeto.data_chegada_venda.readable = False
    db.projeto.data_chegada_venda.writable = False

    db.projeto.data_saida_cobrador.readable = False
    db.projeto.data_saida_cobrador.writable = False

    db.projeto.devolucao_dinh_cobranca.readable = False
    db.projeto.devolucao_dinh_cobranca.writable = False

    db.projeto.devolucao_dinh_venda.readable = False
    db.projeto.devolucao_dinh_venda.writable = False

    db.projeto.nome_cobrador.readable = False
    db.projeto.nome_cobrador.writable = False

    db.projeto.ultima_cidade.readable = False
    db.projeto.ultima_cidade.writable = False

    db.projeto.ultima_data_cobranca.readable = False
    db.projeto.ultima_data_cobranca.writable = False

    db.projeto.vale_cobrador.readable = False
    db.projeto.vale_cobrador.writable = False


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

@auth.requires_login()
def listar_projetos():
    a = auth.user
    rows = db(db.projeto.created_by == auth.user).select()
    return locals()

def criar_projeto():
    conteudo = db.projeto(request.args(0, auth.user))

    db.projeto.adiantamento_dinh_cobranca.readable = False
    db.projeto.adiantamento_dinh_cobranca.writable = False

    db.projeto.comissao_cobrador.readable = False
    db.projeto.comissao_cobrador.writable = False

    db.projeto.data_chegada_cobrador.readable = False
    db.projeto.data_chegada_cobrador.writable = False

    db.projeto.data_chegada_venda.readable = False
    db.projeto.data_chegada_venda.writable = False

    db.projeto.data_saida_cobrador.readable = False
    db.projeto.data_saida_cobrador.writable = False

    db.projeto.devolucao_dinh_cobranca.readable = False
    db.projeto.devolucao_dinh_cobranca.writable = False

    db.projeto.devolucao_dinh_venda.readable = False
    db.projeto.devolucao_dinh_venda.writable = False

    db.projeto.nome_cobrador.readable = False
    db.projeto.nome_cobrador.writable = False

    db.projeto.ultima_cidade.readable = False
    db.projeto.ultima_cidade.writable = False

    db.projeto.ultima_data_cobranca.readable = False
    db.projeto.ultima_data_cobranca.writable = False

    db.projeto.vale_cobrador.readable = False
    db.projeto.vale_cobrador.writable = False
    form = SQLFORM(db.projeto).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('listar_projetos'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
