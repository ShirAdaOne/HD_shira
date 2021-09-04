from POweb.page_object.material_library_page import MaterialLibraryPage


class ToolsManagePage:
    def goto_MaterialLibrary(self):
        '''
        跳转至素材库
        :return:
        '''
        return MaterialLibraryPage()