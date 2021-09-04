from time import sleep

from POweb.page_object.add_member_page import AddMemberPage
from POweb.page_object.contact_page import ContactPage
from POweb.page_object.index_page import IndexPage


class TestAddMember:
    '''
    测试添加成员用例类
    '''
    def test_add_member(self):
        '''
        1，在首页点击添加成员
        2，在添加成员填充成员信息：姓名，手机，账号
        3，在添加成员页面点击保存
        4，在通讯录页面查看成员是否保存成功
        :return:
        '''
        # 获得index,addmember,contact实例对象
        index = IndexPage()
        # addmember = AddMemberPage()
        # contact = ContactPage()

        # 实例对象的操作,测试用例的步骤
        # 测试用例数据问题，避免在PO内维护，在用例中维护测试数据
        phone_list = index.goto_add_member().add_member("yee","0010","13650007018").get_members()
        # addmember.add_member()
        # name_list = contact.get_members()
        # 实际结果是否在预期结果内
        assert "13650007008" in phone_list


