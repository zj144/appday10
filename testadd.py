import os

import allure


class TestAdding:
    def test_001(self):
        # 将txt文件添加到allure文件


        with open("./image"+os.sep+"abc.png","rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)
        assert True