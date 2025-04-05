from model.project import Project
import random
import string


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    app.project.open_project_page()
    old_project_list = app.soap.get_project_list_soap(username, password)
    projects = Project(project_name=random_project_name('proj_', 5))
    app.project.create_project(projects)
    new_project_list = app.soap.get_project_list_soap(username, password)
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(projects)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
