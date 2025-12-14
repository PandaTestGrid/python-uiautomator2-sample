"""
配置文件
"""
import os
from typing import Dict, Any


class Config:
    """配置类"""
    
    # 设备配置
    DEVICE_SERIAL = os.getenv("DEVICE_SERIAL", None)  # 设备序列号，None 表示使用默认设备
    DEVICE_TIMEOUT = float(os.getenv("DEVICE_TIMEOUT", "10.0"))  # 设备操作超时时间
    
    # 应用配置
    APP_PACKAGE = os.getenv("APP_PACKAGE", "com.example.app")  # 应用包名
    APP_ACTIVITY = os.getenv("APP_ACTIVITY", ".MainActivity")  # 应用主 Activity
    
    # 测试配置
    TEST_TIMEOUT = float(os.getenv("TEST_TIMEOUT", "30.0"))  # 测试超时时间
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
    
    # 报告配置
    REPORT_DIR = os.getenv("REPORT_DIR", "reports")
    SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "screenshots")
    LOG_DIR = os.getenv("LOG_DIR", "logs")
    
    # 等待配置
    IMPLICIT_WAIT = float(os.getenv("IMPLICIT_WAIT", "10.0"))  # 隐式等待时间
    EXPLICIT_WAIT = float(os.getenv("EXPLICIT_WAIT", "10.0"))  # 显式等待时间
    
    @classmethod
    def get_device_config(cls) -> Dict[str, Any]:
        """
        获取设备配置
        
        Returns:
            设备配置字典
        """
        return {
            "serial": cls.DEVICE_SERIAL,
            "timeout": cls.DEVICE_TIMEOUT,
        }
    
    @classmethod
    def get_app_config(cls) -> Dict[str, Any]:
        """
        获取应用配置
        
        Returns:
            应用配置字典
        """
        return {
            "package": cls.APP_PACKAGE,
            "activity": cls.APP_ACTIVITY,
        }

