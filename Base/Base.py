'''
封装公共操作
将定位每一个元素都封装为显式等待
'''
import os
import time

import allure
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.get_driver import get_driver


class Base:
    def __init__(self,driver):
        self.driver = driver
    def find_ele(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def find_eles(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    # 调用上面方法，执行元素相关操作
    def click_element(self,el,timeout=10,poll=0.5):
        self.find_ele(el,timeout,poll).click()
    def send_text(self,el,text,timeout=10,poll=0.5):
        input = self.find_ele(el,timeout,poll)
        input.clear()
        input.send_keys(text)
    def swip_screen(self, tag=1):
        '''
        :param tag: 1向上滑动，2向下滑动，3.向左滑动，4.向右滑动
        :return:
        '''
        size = self.driver.get_window_size()
        time.sleep(3)
        if tag == 1:
            self.driver.swipe(start_x=size.get('width') * 0.5,
                              start_y=size.get('height') * 0.8,
                              end_x=size.get('width') * 0.5,
                              end_y=size.get('height') * 0.2, duration=2000)
        if tag == 2:
            self.driver.swipe(start_x=size.get('width') * 0.5,
                              start_y=size.get('height') * 0.2,
                              end_x=size.get('width') * 0.5,
                              end_y=size.get('height') * 0.8, duration=2000)
        if tag == 3:
            self.driver.swipe(start_x=size.get('width') * 0.8,
                              start_y=size.get('height') * 0.5,
                              end_x=size.get('width') * 0.2,
                              end_y=size.get('height') * 0.5, duration=2000)
        if tag == 4:
            self.driver.swipe(start_x=size.get('width') * 0.2,
                              start_y=size.get('height') * 0.5,
                              end_x=size.get('width') * 0.8,
                              end_y=size.get('height') * 0.5, duration=2000)
    def get_toast(self,text):
        message_xpath = (By.XPATH, "//*[contains(@text,{})]".format(text))
        return self.find_ele(message_xpath,timeout=3,poll=0.3).text

    def get_screen(self,name="截图"):
        class TestAdding:
            def test_001(self):
                # 将txt文件添加到allure文件

                with open("./image" + os.sep + "abc.png", "rb") as f:
                    allure.attach(name, f.read(), allure.attach_type.PNG)






























