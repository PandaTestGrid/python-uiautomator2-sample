"""
等待操作测试用例
测试各种等待场景
"""
import pytest
import uiautomator2 as u2
import time
from base.base_test import BaseTest
from utils.helpers import wait_for


class TestWaitOperations(BaseTest):
    """等待操作测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        """测试设置"""
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_wait_for_element(self, device: u2.Device):
        """
        测试等待元素出现
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 等待元素出现（不抛出异常）
        result = self.wait_for_element(
            {"text": "设置"},
            timeout=5.0,
            raise_exception=False
        )
        self.logger.info(f"元素等待结果: {result}")
    
    @pytest.mark.android
    def test_wait_for_element_timeout(self, device: u2.Device):
        """
        测试等待元素超时
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 等待一个不存在的元素（应该超时）
        result = self.wait_for_element(
            {"text": "不存在的元素12345"},
            timeout=3.0,
            raise_exception=False
        )
        assert result is False, "应该超时但未超时"
        self.logger.info("等待超时测试通过")
    
    @pytest.mark.android
    def test_wait_for_app(self, device: u2.Device):
        """
        测试等待应用启动
        """
        app_package = "com.android.settings"
        
        # 启动应用
        device.app_start(app_package)
        
        # 等待应用启动
        result = device.app_wait(app_package, timeout=10.0)
        assert result, "应用启动超时"
        self.logger.info("应用启动等待成功")
    
    @pytest.mark.android
    def test_wait_for_condition(self, device: u2.Device):
        """
        测试等待自定义条件
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        
        # 等待应用完全加载（通过检查当前应用包名）
        def app_loaded():
            current = device.app_current()
            return current.get("package") == "com.android.settings"
        
        result = wait_for(
            app_loaded,
            timeout=10.0,
            error_message="应用加载超时"
        )
        assert result, "应用未加载完成"
        self.logger.info("自定义条件等待成功")
    
    @pytest.mark.android
    def test_wait_with_retry(self, device: u2.Device):
        """
        测试带重试的等待
        """
        from utils.helpers import retry
        
        @retry(max_attempts=3, delay=1.0)
        def click_with_retry():
            device.app_start("com.android.settings")
            device.app_wait("com.android.settings", timeout=10.0)
            time.sleep(2)
            # 尝试点击一个元素
            element = device(text="设置") or device(text="Settings")
            if element.exists:
                element.click()
                return True
            raise Exception("元素不存在")
        
        try:
            result = click_with_retry()
            self.logger.info(f"重试等待成功: {result}")
        except Exception as e:
            self.logger.warning(f"重试等待失败: {e}")
    
    @pytest.mark.android
    def test_implicit_wait(self, device: u2.Device):
        """
        测试隐式等待
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        
        # 使用 uiautomator2 的隐式等待
        element = device(text="设置")
        element.wait(timeout=5.0)  # 等待元素出现，最多5秒
        
        if element.exists:
            self.logger.info("隐式等待成功")
        else:
            self.logger.warning("隐式等待超时")
    
    @pytest.mark.android
    def test_sleep_wait(self, device: u2.Device):
        """
        测试固定时间等待
        """
        start_time = time.time()
        time.sleep(2)  # 固定等待2秒
        elapsed = time.time() - start_time
        
        assert elapsed >= 2.0, "等待时间不足"
        self.logger.info(f"固定等待完成，耗时: {elapsed:.2f}秒")
    
    @pytest.mark.android
    def test_wait_until_gone(self, device: u2.Device):
        """
        测试等待元素消失
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 等待某个元素消失（例如加载提示）
        try:
            # 如果存在加载提示，等待它消失
            loading = device(text="加载中") or device(text="Loading")
            if loading.exists:
                loading.wait_gone(timeout=10.0)
                self.logger.info("元素已消失")
        except Exception as e:
            self.logger.warning(f"等待元素消失测试跳过: {e}")

