"""
示例测试用例
演示如何使用框架进行测试
"""
import pytest
import uiautomator2 as u2
from base.base_test import BaseTest
from page_objects.home_page import HomePage


class TestExample(BaseTest):
    """示例测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        """测试设置"""
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_device_connection(self, device: u2.Device):
        """
        测试设备连接
        验证设备是否可以正常连接并获取信息
        """
        # 获取设备信息
        info = device.info
        assert info is not None, "无法获取设备信息"
        
        # 验证设备信息包含必要字段
        assert "version" in info, "设备信息缺少 version 字段"
        assert "sdk" in info, "设备信息缺少 sdk 字段"
        
        self.logger.info(f"设备信息: {info}")
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_screenshot(self, device: u2.Device):
        """
        测试截图功能
        """
        screenshot_path = self.take_screenshot("test_screenshot")
        assert screenshot_path is not None
        self.logger.info(f"截图路径: {screenshot_path}")
    
    @pytest.mark.regression
    @pytest.mark.android
    def test_swipe_gesture(self, device: u2.Device):
        """
        测试滑动手势
        """
        # 向上滑动
        self.swipe("up", distance=0.3)
        
        # 等待一下
        import time
        time.sleep(1)
        
        # 向下滑动
        self.swipe("down", distance=0.3)
        
        self.logger.info("滑动测试完成")
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_home_page_example(self, device: u2.Device):
        """
        测试首页示例（需要根据实际应用调整）
        演示如何使用页面对象模式
        """
        # 创建页面对象
        home_page = HomePage(device)
        
        # 等待页面加载
        home_page.wait_for_page_load()
        
        # 执行页面操作
        # home_page.click_search_box()
        # home_page.input_search_text("测试")
        
        self.logger.info("首页测试完成")
    
    @pytest.mark.android
    def test_app_launch(self, device: u2.Device, app_package: str = "com.android.settings"):
        """
        测试应用启动
        
        Args:
            device: 设备对象
            app_package: 应用包名（默认使用系统设置）
        """
        # 启动应用
        device.app_start(app_package)
        
        # 等待应用启动
        device.app_wait(app_package, timeout=10.0)
        
        # 验证应用是否在运行
        assert device.app_current()["package"] == app_package, "应用启动失败"
        
        self.logger.info(f"应用 {app_package} 启动成功")
        
        # 关闭应用
        device.app_stop(app_package)


@pytest.mark.android
def test_simple_example(device: u2.Device):
    """
    简单的函数式测试示例
    """
    # 获取屏幕尺寸
    width, height = device.window_size()
    assert width > 0 and height > 0, "无法获取屏幕尺寸"
    
    # 截图
    device.screenshot("simple_test.png")
    
    # 按 Home 键
    device.press("home")

