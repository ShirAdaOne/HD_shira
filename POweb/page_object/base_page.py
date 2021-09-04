from selenium import webdriver
import yaml
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    '''
    父类，封装页面共用的方法，比如driver的实例化
    与具体界面没有关系
    '''
    _base_url = ""
    def __init__(self, base_driver:WebDriver =None):
        # 若未给base_driver形参赋值，那么默认值为None
        if base_driver == None:
            # driver的初始化
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            # 进入index页面
            self.driver.get(self._base_url)
            with open('../conf/cookie.yaml') as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get(self._base_url)
        else:
            # 若base_driver形参，实例化过程中有参数传递，使self.driver=传入的driver对象
            # base_driver 形参，传递Driver对象，即浏览器驱动
            self.driver = base_driver


    def find(self, by, locator=None):
        '''
        \封装查找操作，比如每次查找后添加打印，或者添加日志信息
        参数传入：传入元组(定位方式, 定位元素)，传入两个参数by，locator
        :param by: 定位方式
        :param locator: 定位元素
        :return: find_element()的返回值
        '''
        if locator == None:
            # 若locator为None，那么判断为传入数据为元组
            # 元组解包(1,2),*(1,2)--分别以1，2 形式参数传入
            web_data = self.driver.find_element(*by)
        else:

            web_data = self.driver.find_element(by=by, value=locator)
        print(f"查找到的元素为{web_data}")
        return web_data
