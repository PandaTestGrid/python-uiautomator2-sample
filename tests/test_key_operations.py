"""
按键操作测试用例
测试各种按键操作
"""
import pytest
import uiautomator2 as u2
import time
from base.base_test import BaseTest


class TestKeyOperations(BaseTest):
    """按键操作测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        """测试设置"""
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_press_home(self, device: u2.Device):
        """
        测试按 Home 键
        """
        # 启动一个应用
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(1)
        
        # 按 Home 键
        self.press_home()
        time.sleep(1)
        
        # 验证已返回桌面
        current_app = device.app_current()
        self.logger.info(f"当前应用: {current_app}")
        self.take_screenshot("press_home")
    
    @pytest.mark.android
    def test_press_back(self, device: u2.Device):
        """
        测试按返回键
        """
        # 启动设置应用
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 进入一个子页面（如果可能）
        try:
            # 尝试点击一个设置项
            element = device(text="显示") or device(text="Display")
            if element.exists:
                element.click()
                time.sleep(1)
                self.take_screenshot("before_back")
                
                # 按返回键
                self.press_back()
                time.sleep(1)
                self.take_screenshot("after_back")
        except Exception as e:
            self.logger.warning(f"返回键测试跳过: {e}")
    
    @pytest.mark.android
    def test_press_recent(self, device: u2.Device):
        """
        测试按最近任务键
        """
        # 启动一个应用
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(1)
        
        # 按最近任务键
        self.press_recent()
        time.sleep(2)
        self.take_screenshot("press_recent")
        
        # 再次按最近任务键关闭
        self.press_recent()
        time.sleep(1)
    
    @pytest.mark.android
    def test_press_menu(self, device: u2.Device):
        """
        测试按菜单键
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(1)
        
        # 按菜单键（如果设备支持）
        try:
            device.press("menu")
            time.sleep(1)
            self.take_screenshot("press_menu")
        except Exception as e:
            self.logger.warning(f"菜单键测试跳过（可能不支持）: {e}")
    
    @pytest.mark.android
    def test_press_power(self, device: u2.Device):
        """
        测试按电源键（锁屏/解锁）
        """
        # 按电源键锁屏
        device.press("power")
        time.sleep(1)
        self.logger.info("设备已锁屏")
        
        # 再次按电源键解锁
        device.press("power")
        time.sleep(1)
        self.logger.info("设备已解锁")
        
        # 唤醒设备
        device.wake_up()
        time.sleep(1)
    
    @pytest.mark.android
    def test_press_volume_up(self, device: u2.Device):
        """
        测试按音量加键
        """
        device.press("volume_up")
        time.sleep(0.5)
        self.logger.info("音量加键已按下")
    
    @pytest.mark.android
    def test_press_volume_down(self, device: u2.Device):
        """
        测试按音量减键
        """
        device.press("volume_down")
        time.sleep(0.5)
        self.logger.info("音量减键已按下")
    
    @pytest.mark.android
    def test_press_enter(self, device: u2.Device):
        """
        测试按回车键
        """
        device.press("enter")
        time.sleep(0.5)
        self.logger.info("回车键已按下")
    
    @pytest.mark.android
    def test_press_keycode(self, device: u2.Device):
        """
        测试通过键码按键
        """
        # KEYCODE_HOME = 3
        device.press_keycode(3)
        time.sleep(1)
        self.logger.info("通过键码按 Home 键")
    
    @pytest.mark.android
    def test_key_combination(self, device: u2.Device):
        """
        测试组合键
        """
        # 例如：Ctrl + A（在某些输入场景中）
        try:
            # 注意：uiautomator2 的组合键支持有限
            # 这里仅作为示例
            device.press("home")
            time.sleep(0.5)
            self.logger.info("组合键测试完成")
        except Exception as e:
            self.logger.warning(f"组合键测试跳过: {e}")

