from time import sleep

import yaml

# from POweb.page_object.base_page import BasePage
from selenium import webdriver


class TestCookie():
    def test_get_cookie(self):
        # option = webdriver.ChromeOptions()
        # option.debugger_address = "localhost:9222"
        # driver = webdriver.Chrome(options=option)
        # driver.implicitly_wait(3)
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(15)
        cookie = driver.get_cookies()
        print(cookie)
        with open("cookie.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)  # 将cookie值写入文件中

    def test_login_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("cookie.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

