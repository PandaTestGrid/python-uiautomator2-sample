"""
基础测试类
所有测试类应该继承此类
"""
import pytest
import uiautomator2 as u2
import logging
from typing import Optional
from datetime import datetime

from utils.helpers import wait_for, retry
from utils.logger import setup_logger

logger = setup_logger()


class BaseTest:
    """测试基类"""
    
    def __init__(self, device: u2.Device):
        """
        初始化测试类
        
        Args:
            device: uiautomator2 设备对象
        """
        self.device = device
        self.logger = logger
    
    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.logger.info(f"开始执行测试: {self.__class__.__name__}")
    
    def teardown_method(self):
        """每个测试方法执行后的清理"""
        self.logger.info(f"测试完成: {self.__class__.__name__}")
    
    def take_screenshot(self, name: Optional[str] = None) -> str:
        """
        截图
        
        Args:
            name: 截图文件名（不含扩展名）
        
        Returns:
            截图文件路径
        """
        import os
        
        if name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"screenshot_{timestamp}"
        
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        self.device.screenshot(screenshot_path)
        self.logger.info(f"截图已保存: {screenshot_path}")
        return screenshot_path
    
    def wait_for_element(
        self,
        selector: dict,
        timeout: float = 10.0,
        raise_exception: bool = True
    ) -> bool:
        """
        等待元素出现
        
        Args:
            selector: 元素选择器字典
            timeout: 超时时间
            raise_exception: 超时时是否抛出异常
        
        Returns:
            True 如果元素出现，否则 False
        """
        def check_element():
            return self.device(**selector).exists
        
        result = wait_for(
            check_element,
            timeout=timeout,
            error_message=f"等待元素超时: {selector}"
        )
        
        if not result and raise_exception:
            raise TimeoutError(f"元素未出现: {selector}")
        
        return result
    
    def click_element(self, selector: dict, timeout: float = 10.0):
        """
        点击元素
        
        Args:
            selector: 元素选择器字典
            timeout: 等待元素出现的超时时间
        """
        self.wait_for_element(selector, timeout)
        self.device(**selector).click()
        self.logger.info(f"点击元素: {selector}")
    
    def input_text(self, selector: dict, text: str, timeout: float = 10.0, clear: bool = True):
        """
        输入文本
        
        Args:
            selector: 元素选择器字典
            text: 要输入的文本
            timeout: 等待元素出现的超时时间
            clear: 是否先清空输入框
        """
        self.wait_for_element(selector, timeout)
        element = self.device(**selector)
        
        if clear:
            element.clear_text()
        
        element.set_text(text)
        self.logger.info(f"输入文本到元素 {selector}: {text}")
    
    def get_text(self, selector: dict, timeout: float = 10.0) -> str:
        """
        获取元素文本
        
        Args:
            selector: 元素选择器字典
            timeout: 等待元素出现的超时时间
        
        Returns:
            元素文本内容
        """
        self.wait_for_element(selector, timeout)
        text = self.device(**selector).get_text()
        self.logger.info(f"获取元素文本 {selector}: {text}")
        return text
    
    def swipe(self, direction: str, distance: float = 0.5):
        """
        滑动屏幕
        
        Args:
            direction: 滑动方向 ('up', 'down', 'left', 'right')
            distance: 滑动距离比例 (0.0-1.0)
        """
        width, height = self.device.window_size()
        
        if direction == "up":
            self.device.swipe(width // 2, int(height * (1 - distance / 2)),
                            width // 2, int(height * distance / 2), duration=0.5)
        elif direction == "down":
            self.device.swipe(width // 2, int(height * distance / 2),
                            width // 2, int(height * (1 - distance / 2)), duration=0.5)
        elif direction == "left":
            self.device.swipe(int(width * (1 - distance / 2)), height // 2,
                            int(width * distance / 2), height // 2, duration=0.5)
        elif direction == "right":
            self.device.swipe(int(width * distance / 2), height // 2,
                            int(width * (1 - distance / 2)), height // 2, duration=0.5)
        
        self.logger.info(f"滑动方向: {direction}")
    
    def press_back(self):
        """按返回键"""
        self.device.press("back")
        self.logger.info("按下返回键")
    
    def press_home(self):
        """按 Home 键"""
        self.device.press("home")
        self.logger.info("按下 Home 键")
    
    def press_recent(self):
        """按最近任务键"""
        self.device.press("recent")
        self.logger.info("按下最近任务键")

