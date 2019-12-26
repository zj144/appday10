from Base.Base import Base

# 设置页面操作
from page.pageElements import PageElements


class SettingPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    # 退出登录
    def logout(self,tag=1):
        # 点击退出
        self.click_element(PageElements.setting_logout_btn_id)
        # 判断是否确认退出
        if tag ==1:
            # 点击退出
            self.click_element(PageElements.setting_logout_acc_btn_id)
        if tag == 2:
            # 点击取消退出
            self.click_element(PageElements.setting_logout_dis_btn_id)