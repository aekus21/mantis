from suds.client import Client
from suds import WebFault
from model.project import Project



class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.baseUrl + 'api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list_soap(self, username, password):
        client = Client(self.app.baseUrl + 'api/soap/mantisconnect.php?wsdl')
        try:
            v = client.service.mc_projects_get_user_accessible(username, password)
            projects = []
            for project in v:
                name = project['name']
                id = project['id']
                projects.append(Project(project_name=name, id=id))
            return projects
        except WebFault:
            return False