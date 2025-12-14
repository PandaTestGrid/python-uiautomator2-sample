"""
手势操作测试用例
测试滑动、拖拽、缩放等手势操作
"""
import pytest
import uiautomator2 as u2
import time
from base.base_test import BaseTest


class TestGestureOperations(BaseTest):
    """手势操作测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        """测试设置"""
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_swipe_up(self, device: u2.Device):
        """
        测试向上滑动
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 向上滑动
        self.swipe("up", distance=0.5)
        time.sleep(1)
        self.take_screenshot("swipe_up")
        self.logger.info("向上滑动完成")
    
    @pytest.mark.android
    def test_swipe_down(self, device: u2.Device):
        """
        测试向下滑动
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 先向上滑动
        self.swipe("up", distance=0.5)
        time.sleep(1)
        
        # 再向下滑动
        self.swipe("down", distance=0.5)
        time.sleep(1)
        self.take_screenshot("swipe_down")
        self.logger.info("向下滑动完成")
    
    @pytest.mark.android
    def test_swipe_left(self, device: u2.Device):
        """
        测试向左滑动
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 向左滑动
        self.swipe("left", distance=0.5)
        time.sleep(1)
        self.take_screenshot("swipe_left")
        self.logger.info("向左滑动完成")
    
    @pytest.mark.android
    def test_swipe_right(self, device: u2.Device):
        """
        测试向右滑动
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 先向左滑动
        self.swipe("left", distance=0.5)
        time.sleep(1)
        
        # 再向右滑动
        self.swipe("right", distance=0.5)
        time.sleep(1)
        self.take_screenshot("swipe_right")
        self.logger.info("向右滑动完成")
    
    @pytest.mark.android
    def test_swipe_custom(self, device: u2.Device):
        """
        测试自定义滑动
        """
        width, height = device.window_size()
        
        # 从屏幕中间滑动到顶部
        device.swipe(
            width // 2, height // 2,
            width // 2, height // 4,
            duration=0.5
        )
        time.sleep(1)
        self.logger.info("自定义滑动完成")
    
    @pytest.mark.android
    def test_drag(self, device: u2.Device):
        """
        测试拖拽操作
        """
        width, height = device.window_size()
        
        # 拖拽操作（从一点拖到另一点）
        device.drag(
            width // 2, height // 2,
            width // 2, height // 4,
            duration=0.5
        )
        time.sleep(1)
        self.logger.info("拖拽操作完成")
    
    @pytest.mark.android
    def test_pinch_in(self, device: u2.Device):
        """
        测试捏合手势（缩小）
        """
        width, height = device.window_size()
        center_x, center_y = width // 2, height // 2
        
        # 捏合手势（两个点向内移动）
        device.pinch_in(percent=50, steps=10)
        time.sleep(1)
        self.logger.info("捏合手势完成")
    
    @pytest.mark.android
    def test_pinch_out(self, device: u2.Device):
        """
        测试放大手势
        """
        # 放大手势（两个点向外移动）
        device.pinch_out(percent=50, steps=10)
        time.sleep(1)
        self.logger.info("放大手势完成")
    
    @pytest.mark.android
    def test_scroll(self, device: u2.Device):
        """
        测试滚动操作
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 向下滚动
        device(scrollable=True).scroll.vert.forward(steps=10)
        time.sleep(1)
        self.take_screenshot("scroll_down")
        
        # 向上滚动
        device(scrollable=True).scroll.vert.backward(steps=10)
        time.sleep(1)
        self.take_screenshot("scroll_up")
        
        self.logger.info("滚动操作完成")
    
    @pytest.mark.android
    def test_fling(self, device: u2.Device):
        """
        测试快速滑动（fling）
        """
        device.app_start("com.android.settings")
        device.app_wait("com.android.settings", timeout=10.0)
        time.sleep(2)
        
        # 快速向下滑动
        try:
            device(scrollable=True).fling.vert.forward()
            time.sleep(2)
            self.take_screenshot("fling_down")
            
            # 快速向上滑动
            device(scrollable=True).fling.vert.backward()
            time.sleep(2)
            self.take_screenshot("fling_up")
            
            self.logger.info("快速滑动完成")
        except Exception as e:
            self.logger.warning(f"快速滑动测试跳过: {e}")

