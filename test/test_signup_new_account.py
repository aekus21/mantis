



def test_signup_new_account(app):
    username = 'user'
    password = 'test'
    app.james.ensure_user_exist(username, password)