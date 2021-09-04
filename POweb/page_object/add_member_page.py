from selenium.webdriver.common.by import By

from POweb.page_object.base_page import BasePage
from POweb.page_object.contact_page import ContactPage
# from selenium.webdriver.remote.webdriver import WebDriver  # !!!

class AddMemberPage(BasePage):
    '''
    添加成员页面
    '''
    # 构造函数，可以在不同对象中构造/实例化
    # driver: WebDriver表示类型注解
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    # 定位--页面元素及定位方式
    # 勿暴露私有的页面内部元素--PO六大原则
    # python私有语法 变量名+_ 即 _xxxx
    _username_locator = (By.ID,"username")

    def goto_contact(self):
        '''
        跳转通讯录页面
        :return: 返回 ContactPage 通讯录页面对象
        '''
        return ContactPage()

    def add_member(self, name, accid, phone):
        '''
        添加成员操作
        :param name: 成员名称
        :param accid: 成员唯一标识
        :param phone: 成员电话
        :return: 返回 ContactPage 通讯录页面对象
        '''
        self.find(self._username_locator).send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(accid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage(self.driver)


