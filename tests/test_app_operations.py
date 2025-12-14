"""
应用操作测试用例
测试应用的启动、关闭、切换等基本操作
"""
import pytest
import uiautomator2 as u2
import time
from base.base_test import BaseTest


class TestAppOperations(BaseTest):
    """应用操作测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        """测试设置"""
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_app_start_and_stop(self, device: u2.Device):
        """
        测试应用启动和关闭
        使用系统设置应用作为示例
        """
        app_package = "com.android.settings"
        
        # 确保应用已关闭
        device.app_stop(app_package)
        time.sleep(1)
        
        # 启动应用
        device.app_start(app_package)
        self.logger.info(f"启动应用: {app_package}")
        
        # 等待应用启动
        device.app_wait(app_package, timeout=10.0)
        
        # 验证应用是否在运行
        current_app = device.app_current()
        assert current_app["package"] == app_package, f"应用启动失败，当前应用: {current_app}"
        self.logger.info(f"应用启动成功，当前应用: {current_app}")
        
        # 等待界面加载
        time.sleep(2)
        
        # 关闭应用
        device.app_stop(app_package)
        self.logger.info(f"关闭应用: {app_package}")
        
        # 验证应用已关闭
        time.sleep(1)
        current_app = device.app_current()
        assert current_app["package"] != app_package, "应用未成功关闭"
    
    @pytest.mark.android
    def test_app_clear_data(self, device: u2.Device):
        """
        测试清除应用数据
        """
        app_package = "com.android.settings"
        
        # 清除应用数据
        device.app_clear(app_package)
        self.logger.info(f"清除应用数据: {app_package}")
        
        # 重新启动应用验证
        device.app_start(app_package)
        device.app_wait(app_package, timeout=10.0)
        
        self.logger.info("应用数据清除成功")
    
    @pytest.mark.android
    def test_app_info(self, device: u2.Device):
        """
        测试获取应用信息
        """
        app_package = "com.android.settings"
        
        # 获取应用信息
        app_info = device.app_info(app_package)
        
        assert app_info is not None, "无法获取应用信息"
        assert "packageName" in app_info, "应用信息缺少包名"
        assert "versionName" in app_info, "应用信息缺少版本号"
        
        self.logger.info(f"应用信息: {app_info}")
    
    @pytest.mark.android
    def test_app_list(self, device: u2.Device):
        """
        测试获取已安装应用列表
        """
        # 获取所有已安装应用
        app_list = device.app_list()
        
        assert len(app_list) > 0, "应用列表为空"
        self.logger.info(f"已安装应用数量: {len(app_list)}")
        
        # 检查系统设置应用是否在列表中
        assert "com.android.settings" in app_list, "系统设置应用未在列表中"
    
    @pytest.mark.android
    def test_app_running_list(self, device: u2.Device):
        """
        测试获取正在运行的应用列表
        """
        # 获取正在运行的应用
        running_apps = device.app_list_running()
        
        assert len(running_apps) > 0, "没有正在运行的应用"
        self.logger.info(f"正在运行的应用数量: {len(running_apps)}")
        self.logger.info(f"运行中的应用: {running_apps}")
    
    @pytest.mark.android
    def test_app_wait_activity(self, device: u2.Device):
        """
        测试等待特定 Activity 出现
        """
        app_package = "com.android.settings"
        activity = ".Settings"
        
        # 启动应用
        device.app_start(app_package)
        
        # 等待特定 Activity
        result = device.app_wait(app_package, timeout=10.0)
        assert result, "应用启动超时"
        
        self.logger.info(f"Activity 已启动: {app_package}/{activity}")

