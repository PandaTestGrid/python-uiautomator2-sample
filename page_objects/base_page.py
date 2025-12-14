"""
页面对象基类
所有页面对象应该继承此类
"""
import uiautomator2 as u2
import logging
from typing import Optional, Dict, Any
from base.base_test import BaseTest

logger = logging.getLogger(__name__)


class BasePage(BaseTest):
    """页面对象基类"""
    
    def __init__(self, device: u2.Device):
        """
        初始化页面对象
        
        Args:
            device: uiautomator2 设备对象
        """
        super().__init__(device)
        self.page_name = self.__class__.__name__
    
    def is_page_loaded(self, timeout: float = 10.0) -> bool:
        """
        检查页面是否已加载
        
        子类应该重写此方法，定义页面加载的标识元素
        
        Args:
            timeout: 超时时间
        
        Returns:
            True 如果页面已加载，否则 False
        """
        # 默认实现，子类应该重写
        return True
    
    def wait_for_page_load(self, timeout: float = 10.0):
        """
        等待页面加载完成
        
        Args:
            timeout: 超时时间
        """
        if not self.is_page_loaded(timeout):
            raise TimeoutError(f"页面 {self.page_name} 加载超时")
        self.logger.info(f"页面 {self.page_name} 加载完成")

