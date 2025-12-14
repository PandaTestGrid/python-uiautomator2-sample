"""
元素操作测试用例
测试元素的查找、点击、输入等操作
"""
import pytest
import uiautomator2 as u2
import time
from base.base_test import BaseTest


class TestElementOperations(BaseTest):
    """元素操作测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        """测试设置"""
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_find_element_by_text(self, device: u2.Device):
        """
        测试通过文本查找元素
        使用系统设置应用作为示例
        """
        # 启动设置应用
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 尝试查找常见设置项（根据实际设备调整）
        try:
            # 查找"显示"或"Display"设置项
            element = device(text="显示") or device(text="Display")
            if element.exists:
                self.logger.info("找到元素: 显示/Display")
                element.click()
                time.sleep(1)
                self.take_screenshot("display_settings")
        except Exception as e:
            self.logger.warning(f"未找到指定元素: {e}")
    
    @pytest.mark.android
    def test_find_element_by_resource_id(self, device: u2.Device):
        """
        测试通过 resourceId 查找元素
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 尝试通过 resourceId 查找（需要根据实际应用调整）
        try:
            # 查找搜索框（如果存在）
            search_box = device(resourceId="com.android.settings:id/search_action_bar")
            if search_box.exists:
                self.logger.info("找到搜索框")
                search_box.click()
                time.sleep(1)
        except Exception as e:
            self.logger.warning(f"未找到指定元素: {e}")
    
    @pytest.mark.android
    def test_find_element_by_description(self, device: u2.Device):
        """
        测试通过描述（content-desc）查找元素
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 尝试通过描述查找
        try:
            # 查找返回按钮
            back_button = device(description="向上导航") or device(description="Navigate up")
            if back_button.exists:
                self.logger.info("找到返回按钮")
        except Exception as e:
            self.logger.warning(f"未找到指定元素: {e}")
    
    @pytest.mark.android
    def test_element_exists(self, device: u2.Device):
        """
        测试检查元素是否存在
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 检查元素是否存在
        exists = device(text="设置").exists or device(text="Settings").exists
        self.logger.info(f"元素存在: {exists}")
        
        # 使用基类方法等待元素
        try:
            self.wait_for_element({"text": "设置"}, timeout=5.0, raise_exception=False)
            self.logger.info("元素存在")
        except Exception:
            self.logger.info("元素不存在")
    
    @pytest.mark.android
    def test_element_count(self, device: u2.Device):
        """
        测试获取匹配元素的数量
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 获取所有可点击元素的数量
        clickable_elements = device(clickable=True)
        count = clickable_elements.count
        
        self.logger.info(f"可点击元素数量: {count}")
        assert count > 0, "未找到可点击元素"
    
    @pytest.mark.android
    def test_element_get_info(self, device: u2.Device):
        """
        测试获取元素信息
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 查找一个元素并获取信息
        try:
            element = device(text="设置") or device(text="Settings")
            if element.exists:
                info = element.info
                self.logger.info(f"元素信息: {info}")
                assert "text" in info or "contentDescription" in info, "元素信息不完整"
        except Exception as e:
            self.logger.warning(f"获取元素信息失败: {e}")
    
    @pytest.mark.android
    def test_input_text(self, device: u2.Device):
        """
        测试输入文本
        """
        # 启动浏览器或搜索应用（如果有）
        # 这里使用系统搜索作为示例
        device.press("home")
        time.sleep(1)
        
        # 尝试打开搜索
        try:
            # 长按 Home 键打开 Google Assistant 或搜索
            device.press("home")
            time.sleep(0.5)
            
            # 如果有搜索框，输入文本
            search_input = device(focused=True)
            if search_input.exists:
                self.input_text({"focused": True}, "测试文本", clear=True)
                self.logger.info("文本输入成功")
        except Exception as e:
            self.logger.warning(f"输入文本测试跳过: {e}")
    
    @pytest.mark.android
    def test_clear_text(self, device: u2.Device):
        """
        测试清空文本
        """
        # 这个测试需要在一个有输入框的应用中进行
        # 这里仅作为示例框架
        try:
            element = device(focused=True)
            if element.exists and element.info.get("className") == "android.widget.EditText":
                element.clear_text()
                self.logger.info("文本清空成功")
        except Exception as e:
            self.logger.warning(f"清空文本测试跳过: {e}")
    
    @pytest.mark.android
    def test_long_click(self, device: u2.Device):
        """
        测试长按操作
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 长按某个列表项（如果存在）
        try:
            # 查找第一个列表项
            list_item = device(className="android.widget.TextView")
            if list_item.exists:
                list_item.long_click()
                self.logger.info("长按操作成功")
                time.sleep(1)
        except Exception as e:
            self.logger.warning(f"长按操作测试跳过: {e}")

