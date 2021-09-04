from POweb.page_object.index_page import IndexPage
from POweb.page_object.material_library_page import MaterialLibraryPage


class TestAddMaterialLibrary:
    def test_add_word(self):
        '''
        1，进入素材库页面
        2，进入添加文字页面--操作--确认（返回素材库页面）
        3，对比文字是否添加成功
        :return:
        '''
        material_library = MaterialLibraryPage()
        addword = material_library.goto_add_material().add_material_word("456").get_material_word()
        assert "456" in addword
