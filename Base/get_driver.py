def get_driver():
    from appium import webdriver
    desired = {
        "platformName": "android",
        "platformVersion": "5.1",
        "deviceName": "192.168.94.101:5555",
        # "deviceName": "emulator-5554",
        "appPackage": 'com.bjcsxq.chat.carfriend',
        "appActivity": '.module_main.activity.MainActivity',
        "unicodeKeyboard":True,
        "resetKeyboard": True
        # 支持toast消息获取

        # com.bjcsxq.chat.carfriend /.module_main.activity.MainActivity
    }
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=desired)
    return driver