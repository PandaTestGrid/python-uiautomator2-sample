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
    def setup_device(self, device: u2.Device):
        """自动注入设备对象"""
        self.device = device

    @pytest.mark.smoke
    @pytest.mark.android
    def test_device_basic_info(self):
        """
        测试获取设备基本信息
        """
        print(info)
        for i in range(180):
            import time
            time.sleep(1)
            print(i)

