from selenium.webdriver.common.by import By

from POweb.page_object.add_member_page import AddMemberPage
from POweb.page_object.base_page import BasePage
from POweb.page_object.contact_page import ContactPage
from POweb.page_object.tools_manage_page import ToolsManagePage
from selenium import webdriver

class IndexPage(BasePage):
    '''
    首页页面
    '''
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact(self):
        '''
        跳转通讯录
        :return: 返回contact页面实例对象
        '''
        return ContactPage()

    def goto_add_member(self):
        '''
        跳转添加成员页面
        :return: 返回AddMemberPage添加成员页面对象
        '''

        # 获取定位,点击添加成员按钮，跳转到添加成员页面
        # self.driver.find_element(By.CSS_SELECTOR,'#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1) > div').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        # 传递driver
        return AddMemberPage(self.driver)

    def go_to_tools_manage_page(self):
        '''
        跳转管理工具
        :return: 返回ToolsManagePage管理工具页面对象
        '''

        return ToolsManagePage()


