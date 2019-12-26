from Base.Base import Base
from page.pageElements import PageElements

# 个人中心页面
class PersonPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 点击登录注册按钮
    def click_login1(self):
        self.click_element(PageElements.person_login_sigin_btn_xpath)
    def xiahua(self):
        self.swip_screen()
    def sahnghua(self):
        self.swip_screen(2)
    # 获取用户名断言
    def get_username(self):
        return self.find_ele(PageElements.person_user_name_id).text
    # 点击设置按钮
    def click_setting_btn(self):
        self.click_element(PageElements.person_setting_btn_id)