from page.homepage import HomePage
from page.loginpage import LoginPage
from page.personpage import PersonPage
from page.settingpage import SettingPage


class PageObj():
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return HomePage(self.driver)

    def get_person_page(self):
        return PersonPage(self.driver)

    def get_seting_page(self):
        return SettingPage(self.driver)

    def get_login_page(self):
        return LoginPage(self.driver)



