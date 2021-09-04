from selenium.webdriver.common.by import By

from POweb.page_object.base_page import BasePage
from POweb.page_object.material_library_page import MaterialLibraryPage


class AddMaterialWordPage(BasePage):
    def add_material_word(self, text):
        '''
        素材库--添加文字
        :param text: 添加的文字
        :return: 返回MaterialLibraryPage 素材库页面对象
        '''
        self.find(By.CSS_SELECTOR, ".ww_textarea_Big").send_keys(text)
        self.find(By.CSS_SELECTOR, ".js_save_action").click()
        return MaterialLibraryPage(self.driver)