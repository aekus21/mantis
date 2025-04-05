import random
from model.project import Project

def test_del_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    app.project.open_project_page()
    if len(app.soap.get_project_list_soap(username, password)) == 0:
        app.project.create_project(Project(project_name='test_project', project_description='test_descr'))
    old_project_list = app.soap.get_project_list_soap(username, password)
    project = random.choice(old_project_list)
    app.project.select_project_by_id(project.id)
    new_project_list = app.soap.get_project_list_soap(username, password)
    assert len(old_project_list) - 1 == len(new_project_list)
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)