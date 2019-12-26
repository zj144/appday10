from selenium.common.exceptions import TimeoutException
from Base.Base import Base
from page.pageElements import PageElements
class HomePage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 点击稍后更新
    def click_after_btn(self):
        try:
            self.click_element(PageElements.home_after_btn_id)
        # except TimeoutException:
        except :
            print('xxxx')
        # try:
        #
        #
        # except TxxximeoutException:
        #     print('myyc')
        # 点击个人中心
    def click_my_btn(self):
        self.click_element(PageElements.home_my_btn_id)
