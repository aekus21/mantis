import random
from model.project import Project

def test_del_project(app):
    app.project.open_project_page()
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(project_name='test_project', project_description='test_descr'))
    old_project_list = app.project.get_project_list()
    project = random.choice(old_project_list)
    app.project.select_project_by_id(project.id)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)