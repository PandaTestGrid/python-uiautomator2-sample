"""
设备管理工具类
负责设备的连接、信息获取等操作
"""
import uiautomator2 as u2
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


class DeviceManager:
    """设备管理器"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化设备管理器
        
        Args:
            config: 设备配置字典，包含 serial, timeout 等
        """
        self.config = config
        self.device: Optional[u2.Device] = None
        self.serial = config.get("serial")
        self.timeout = config.get("timeout", 10.0)
    
    def connect(self) -> Optional[u2.Device]:
        """
        连接到设备
        
        Returns:
            u2.Device 对象，连接失败返回 None
        """
        try:
            if self.serial:
                logger.info(f"正在连接到设备: {self.serial}")
                self.device = u2.connect(self.serial)
            else:
                logger.info("正在连接到默认设备（通过 adb devices 获取）")
                self.device = u2.connect()
            
            # 验证连接
            if self.device:
                info = self.device.info
                logger.info(f"设备连接成功: {info.get('productName', 'Unknown')}")
                return self.device
            else:
                logger.error("设备连接失败")
                return None
                
        except Exception as e:
            logger.error(f"连接设备时发生错误: {e}")
            return None
    
    def get_device_info(self) -> Dict[str, Any]:
        """
        获取设备信息
        
        Returns:
            设备信息字典
        """
        if not self.device:
            return {}
        
        try:
            info = self.device.info
            return {
                "serial": self.device.serial,
                "version": info.get("version", "Unknown"),
                "sdk": info.get("sdk", "Unknown"),
                "product_name": info.get("productName", "Unknown"),
                "brand": info.get("brand", "Unknown"),
                "model": info.get("model", "Unknown"),
                "display": info.get("display", {}),
            }
        except Exception as e:
            logger.error(f"获取设备信息失败: {e}")
            return {}
    
    def is_connected(self) -> bool:
        """
        检查设备是否已连接
        
        Returns:
            True 如果设备已连接，否则 False
        """
        if not self.device:
            return False
        
        try:
            self.device.info
            return True
        except Exception:
            return False
    
    def disconnect(self):
        """断开设备连接"""
        if self.device:
            try:
                self.device = None
                logger.info("设备已断开连接")
            except Exception as e:
                logger.error(f"断开连接时出错: {e}")

