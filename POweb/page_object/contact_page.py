from selenium.webdriver.common.by import By

from POweb.page_object.base_page import BasePage


class ContactPage(BasePage):
    '''
    通讯页面
    '''
    def goto_add_member(self):
        '''
        跳转到添加成员页面
        若A导入B，B导入A，有循环导入的场景，那么需要在方法内做导包操作即可避免
        :return: 返回AddMemberPage页面对象
        '''

        from POweb.page_object.add_member_page import AddMemberPage
        return AddMemberPage()

    def get_members(self):
        '''
        获取成员信息
        :return: 返回 phone_list进行断言
        '''
        members = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        phone_list = []
        print(members)
        for member in members:
            phone_list.append(member.text)
        return phone_list
