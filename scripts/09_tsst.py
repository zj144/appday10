import os
import sys
import pytest
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from getData import GetData
from Base.get_driver import get_driver
from Base.page import PageObj
class TestLogin():
    def setup_class(self):
        self.driver= get_driver()
        self.page = PageObj(self.driver)
    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture(scope='class',autouse=True)
    # 初始化操作
    def init_login(self):
        # 点击稍后更新
        self.page.get_home_page().click_after_btn()
        # 点击个人中心
        self.page.get_home_page().click_my_btn()
    # 正向用例
    @pytest.mark.parametrize('a,b,c,d',GetData().get_yml_data('login.yml'))
    def test_login(self,a,b,c,d):        # 点击登录
        if c is None:
            self.page.get_person_page().click_login1()  # 输入账号密码
            self.page.get_login_page().login(a,b)  # 点击登录
            self.page.get_login_page().click_btn() # 点击确认登录
            self.page.get_login_page().click_suc_btn() # 获取用户名文本断言
            data = self.page.get_person_page().get_username()
            try:
                assert d in data
            except AssertionError:
                self.page.get_seting_page().get_screen('失败截图')
                raise
            finally:
                self.page.get_person_page().xiahua() # 下滑
                self.page.get_person_page().click_setting_btn() # 点击设置
                self.page.get_seting_page().logout() # 点击退出当前账号
                self.page.get_person_page().sahnghua()# 上话到初始化界面
    # 逆向用例
    # @pytest.mark.parametrize('a,b','c', [("13383161571", "ykx199","错误")])
    # def test_login2(self,a,b,c):        # 点击登录
    #     self.page.get_person_page().click_login1()  # 输入账号密码
    #     self.page.get_login_page().login(a,b)  # 点击登录
    #     self.page.get_login_page().click_btn() # 点击确认登录
    #     try:
    #         self.page.get_login_page().get_toast(c)
    #         assert True
    #     except:
    #         assert False
        else:
            self.page.get_person_page().click_login1()  # 输入账号密码
            self.page.get_login_page().login(a,b)  # 点击登录
            self.page.get_login_page().click_btn() # 点击确认登录
            # message_xpath = (By.XPATH, "//*[contains(@text,{})]".format(c))
            # data = self.driver.find_element_by_xpath(message_xpath).text
            # s6 = self.page.get_login_page().get_toast(c)
            # print('获得的toast信息',data,d)
            try:
                s6 = self.driver.find_element_by_xpath("//*[contains(@text,{})]".format(d))
                print(s6.text,d)
            except Exception as s7:
                self.page.get_seting_page().get_screen()
                raise s7
            finally:
                self.page.get_login_page().click_return()
if __name__ == '__main__':
    pytest.main(['09_tsst.py'])




