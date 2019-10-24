# -*- coding: utf-8 -*-
# tente algo como

#@cache.action(time_expire=300, cache_model=cache.ram, quick='P')
@auth.requires_login()
def show_contact():
    a = auth.user
    rows = db(db.contact.created_by == auth.user).select()
    return locals()
def create_contact():
    form = SQLFORM(db.contact).process()
    if form.accepted:
        response.flash = 'accepted form'
        redirect(URL('show_contact'))
    elif form.errors:
        response.flash = 'form not accepted'
    else:
        response.flash = 'fill the form'
        return locals()
def change_contact():
    form = SQLFORM(db.contact, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'updated'
        redirect(URL('show_contact'))
    elif form.errors:
        response.flash = 'form error'
    else:
        if not response.flash:
            response.flash = 'fill the form'
    return locals()
