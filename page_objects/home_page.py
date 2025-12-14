"""
首页页面对象示例
"""
import uiautomator2 as u2
from page_objects.base_page import BasePage


class HomePage(BasePage):
    """首页页面对象"""
    
    # 页面元素定位（示例）
    SEARCH_BOX = {"resourceId": "com.example.app:id/search_box"}
    MENU_BUTTON = {"resourceId": "com.example.app:id/menu_button"}
    SETTINGS_BUTTON = {"description": "设置"}
    
    def __init__(self, device: u2.Device):
        super().__init__(device)
    
    def is_page_loaded(self, timeout: float = 10.0) -> bool:
        """
        检查首页是否已加载
        
        通过检查关键元素是否存在来判断
        """
        try:
            # 检查搜索框或菜单按钮是否存在
            return (self.device(**self.SEARCH_BOX).exists(timeout=timeout) or
                   self.device(**self.MENU_BUTTON).exists(timeout=timeout))
        except Exception:
            return False
    
    def click_search_box(self):
        """点击搜索框"""
        self.click_element(self.SEARCH_BOX)
        return self
    
    def input_search_text(self, text: str):
        """在搜索框输入文本"""
        self.input_text(self.SEARCH_BOX, text)
        return self
    
    def click_menu_button(self):
        """点击菜单按钮"""
        self.click_element(self.MENU_BUTTON)
        return self
    
    def click_settings(self):
        """点击设置按钮"""
        self.click_element(self.SETTINGS_BUTTON)
        return self
    
    def navigate_to_settings(self):
        """导航到设置页面"""
        self.click_settings()
        # 返回设置页面对象（需要导入）
        # from page_objects.settings_page import SettingsPage
        # return SettingsPage(self.device)

