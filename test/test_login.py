


def test_login(app):
    if app.session.is_logged_in() is True:
        app.session.logout()
    app.session.login_form('administrator', 'root')
    assert app.session.is_logged_in_as('administrator')