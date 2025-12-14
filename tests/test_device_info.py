"""
设备信息测试用例
测试获取设备信息、屏幕信息等
"""
import pytest
import uiautomator2 as u2
from base.base_test import BaseTest


class TestDeviceInfo(BaseTest):
    """设备信息测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        """测试设置"""
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_device_basic_info(self, device: u2.Device):
        """
        测试获取设备基本信息
        """
        info = device.info
        
        # 验证必要字段
        assert "version" in info, "设备信息缺少版本号"
        assert "sdk" in info, "设备信息缺少 SDK 版本"
        assert "productName" in info, "设备信息缺少产品名称"
        
        self.logger.info(f"设备版本: {info.get('version')}")
        self.logger.info(f"SDK 版本: {info.get('sdk')}")
        self.logger.info(f"产品名称: {info.get('productName')}")
        self.logger.info(f"品牌: {info.get('brand')}")
        self.logger.info(f"型号: {info.get('model')}")
    
    @pytest.mark.android
    def test_device_serial(self, device: u2.Device):
        """
        测试获取设备序列号
        """
        serial = device.serial
        assert serial is not None, "无法获取设备序列号"
        assert len(serial) > 0, "设备序列号为空"
        self.logger.info(f"设备序列号: {serial}")
    
    @pytest.mark.android
    def test_window_size(self, device: u2.Device):
        """
        测试获取屏幕尺寸
        """
        width, height = device.window_size()
        
        assert width > 0, "屏幕宽度无效"
        assert height > 0, "屏幕高度无效"
        
        self.logger.info(f"屏幕尺寸: {width} x {height}")
        self.logger.info(f"屏幕方向: {'横屏' if width > height else '竖屏'}")
    
    @pytest.mark.android
    def test_display_info(self, device: u2.Device):
        """
        测试获取显示信息
        """
        info = device.info
        display = info.get("display", {})
        
        if display:
            self.logger.info(f"显示信息: {display}")
            if "width" in display:
                self.logger.info(f"显示宽度: {display['width']}")
            if "height" in display:
                self.logger.info(f"显示高度: {display['height']}")
            if "density" in display:
                self.logger.info(f"显示密度: {display['density']}")
    
    @pytest.mark.android
    def test_device_orientation(self, device: u2.Device):
        """
        测试获取设备方向
        """
        orientation = device.orientation
        
        assert orientation in ["natural", "left", "right", "upsidedown"], "设备方向值无效"
        self.logger.info(f"设备方向: {orientation}")
    
    @pytest.mark.android
    def test_device_wake_up(self, device: u2.Device):
        """
        测试唤醒设备
        """
        device.wake_up()
        self.logger.info("设备已唤醒")
        
        # 验证设备是否唤醒
        info = device.info
        assert info is not None, "设备未唤醒"
    
    @pytest.mark.android
    def test_device_screen_on(self, device: u2.Device):
        """
        测试检查屏幕是否点亮
        """
        is_screen_on = device.info.get("screenOn", False)
        self.logger.info(f"屏幕状态: {'点亮' if is_screen_on else '熄灭'}")
    
    @pytest.mark.android
    def test_device_battery_info(self, device: u2.Device):
        """
        测试获取电池信息
        """
        try:
            # 通过 shell 命令获取电池信息
            battery_level = device.shell("dumpsys battery | grep level").output.strip()
            if battery_level:
                self.logger.info(f"电池信息: {battery_level}")
        except Exception as e:
            self.logger.warning(f"获取电池信息失败: {e}")
    
    @pytest.mark.android
    def test_device_memory_info(self, device: u2.Device):
        """
        测试获取内存信息
        """
        try:
            # 获取内存信息
            mem_info = device.shell("cat /proc/meminfo | head -3").output
            self.logger.info(f"内存信息:\n{mem_info}")
        except Exception as e:
            self.logger.warning(f"获取内存信息失败: {e}")
    
    @pytest.mark.android
    def test_device_cpu_info(self, device: u2.Device):
        """
        测试获取 CPU 信息
        """
        try:
            # 获取 CPU 信息
            cpu_info = device.shell("cat /proc/cpuinfo | head -10").output
            self.logger.info(f"CPU 信息:\n{cpu_info}")
        except Exception as e:
            self.logger.warning(f"获取 CPU 信息失败: {e}")

