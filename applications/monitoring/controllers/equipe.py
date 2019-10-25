# -*- coding: utf-8 -*-
# tente algo como
def listar_vendedor():
    proj = db.projeto(request.args(0, cast=int))
    rows = db(db.vendedor.projeto == request.args(0, cast=int)).select()
    return locals()

def inserir_vendedor():
    proj = db.projeto(request.args(0, cast=int))
    db.vendedor.projeto.default = proj.id
    db.vendedor.projeto.readable = False
    db.vendedor.projeto.writable = False

    db.vendedor.comissao_venda.readable = True
    db.vendedor.comissao_venda.writable = True
    db.vendedor.comissao_cobranca.readable = True
    db.vendedor.comissao_cobranca.writable = True

    merc = db(db.vendedor.projeto==proj.id).select()
    form = SQLFORM(db.vendedor).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('listar_vendedor', args=proj.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()

def alterar_vendedor():
    merc = db.vendedor(request.args(0, cast=int))
    proj = db.projeto(merc.projeto)
    db.vendedor.projeto.default = proj.id
    db.vendedor.projeto.readable = False
    db.vendedor.projeto.writable = False
    db.vendedor.comissao_venda.readable = True
    db.vendedor.comissao_venda.writable = True
    db.vendedor.comissao_venda.readable = True
    db.vendedor.comissao_venda.writable = True
    db.vendedor.comissao_cobranca.readable = True
    db.vendedor.comissao_cobranca.writable = True
    form = SQLFORM(db.vendedor, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'atualizada'
        redirect(URL('listar_vendedor', args=proj.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()


def alterar_vendedor_venda():
    merc = db.vendedor(request.args(0, cast=int))
    proj = db.projeto(merc.projeto)
    db.vendedor.projeto.default = proj.id
    db.vendedor.projeto.readable = False
    db.vendedor.projeto.writable = False

    db.vendedor.vale_saida.readable = True
    db.vendedor.vale_saida.writable = True

    db.vendedor.vale_caderno.readable = True
    db.vendedor.vale_caderno.writable = True

    db.vendedor.venda.readable = True
    db.vendedor.venda.writable = True

    db.vendedor.entradas_venda.readable = True
    db.vendedor.entradas_venda.writable = True

    db.vendedor.quant_fichas.readable = True
    db.vendedor.quant_fichas.writable = True


    form = SQLFORM(db.vendedor, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'atualizada'
        redirect(URL('listar_venda', args=proj.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

def listar_venda():
    proj = db.projeto(request.args(0, cast=int))
    rows = db(db.vendedor.projeto == request.args(0, cast=int)).select()
    return locals()
def listar_cobranca():
    proj = db.projeto(request.args(0, cast=int))
    rows = db(db.vendedor.projeto == request.args(0, cast=int)).select()
    return locals()


def alterar_vendedor_cobranca():
    merc = db.vendedor(request.args(0, cast=int))
    proj = db.projeto(merc.projeto)
    db.vendedor.projeto.default = proj.id
    db.vendedor.projeto.readable = False
    db.vendedor.projeto.writable = False
    db.vendedor.vale_saida.readable = False
    db.vendedor.vale_saida.writable = False

    db.vendedor.nome_vendedor.readable = True
    db.vendedor.nome_vendedor.writable = False

    db.vendedor.venda.readable = True
    db.vendedor.venda.writable = False

    db.vendedor.quant_fichas.readable = True
    db.vendedor.quant_fichas.writable = False

    db.vendedor.recebido_cobranca.readable = True
    db.vendedor.recebido_cobranca.writable = True

    db.vendedor.devolvido_cobranca.readable = True
    db.vendedor.devolvido_cobranca.writable = True

    db.vendedor.prego_cobranca.readable = True
    db.vendedor.prego_cobranca.writable = True
    form = SQLFORM(db.vendedor, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'atualizada'
        redirect(URL('listar_vendedor', args=proj.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
