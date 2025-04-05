from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def create_page(self):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def create_project(self, project_name):
        wd = self.app.wd
        self.create_page()
        wd.find_element_by_name('name').click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_name.project_name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("test_desc")
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_cache = []
        for element in wd.find_elements_by_xpath("//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            id = element.get_attribute('href').replace('http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=','')
            self.project_cache.append(Project(project_name=text, id=id))
        return list(self.project_cache)

    def select_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.get_project_id(id)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        self.project_cache = None

    def get_project_id(self, id):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=' + str(id))