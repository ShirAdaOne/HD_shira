from selenium.webdriver.common.by import By

from POweb.page_object.base_page import BasePage



class MaterialLibraryPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#material/text"
    def goto_add_material(self):
        '''
        跳转素材库-添加文字
        :return: 返回AddMaterialWordPage 添加素材库-添加文字页面对象
        '''
        from POweb.page_object.add_material_word_page import AddMaterialWordPage
        self.find(By.CSS_SELECTOR, ".ww_btn_WithIcon").click()
        return AddMaterialWordPage(self.driver)

    def get_material_word(self):
        '''
        获取素材库内容进行比对
        :return: 返回素材库内容-list
        '''
        # ！！！注意 find_elements 注意s！！
        materials = self.driver.find_elements(By.CSS_SELECTOR, "td.material_text_table_text:nth-child(1)")
        mat_list = []
        for mater in materials:
            mat_list.append(mater.text)
        return mat_list