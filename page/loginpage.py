from Base.Base import Base
from page.pageElements import PageElements
class LoginPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 输入手机号密码
    def login(self,phon,passwd):
        self.send_text(PageElements.login_phone_id,phon)
        self.send_text(PageElements.login_passwd_id,passwd)
    # 点击确认登录
    def click_btn(self):
        self.click_element(PageElements.login_btn_id)
    # 点击返回按钮
    def click_return(self):
        self.click_element(PageElements.login_return_btn_id)
    def click_suc_btn(self):
        self.click_element(PageElements.login_suc_acc_btn_id)
    # 查找返回错误信息
    def find_err(self):
        return self.find_ele(PageElements.message_xpath)
