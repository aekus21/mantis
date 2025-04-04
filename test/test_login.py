


def test_login(app):
    app.session.login_form('administrator', 'root')
    assert app.session.is_logged_in_as('administrator')