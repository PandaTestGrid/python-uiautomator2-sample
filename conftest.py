"""
pytest 配置文件
提供全局 fixtures 和测试配置
"""
import pytest
import uiautomator2 as u2
from typing import Generator
import logging
import os
from datetime import datetime

from utils.device_manager import DeviceManager
from utils.logger import setup_logger

# 配置日志
logger = setup_logger()


@pytest.fixture(scope="session")
def device_config():
    """
    设备配置 fixture
    可以通过环境变量或配置文件指定设备序列号
    """
    device_serial = os.getenv("DEVICE_SERIAL", None)
    return {
        "serial": device_serial,
        "timeout": 10.0,
    }


@pytest.fixture(scope="session")
def device(device_config) -> Generator[u2.Device, None, None]:
    """
    设备连接 fixture
    在整个测试会话期间保持连接
    """
    device_manager = DeviceManager(device_config)
    device = device_manager.connect()
    
    if device is None:
        pytest.skip("无法连接到设备，跳过测试")
    
    logger.info(f"设备连接成功: {device_manager.get_device_info()}")
    
    yield device
    
    # 清理工作
    try:
        device.app_stop_all()
        logger.info("测试会话结束，已清理所有应用")
    except Exception as e:
        logger.warning(f"清理设备时出错: {e}")


@pytest.fixture(scope="function")
def clean_device(device):
    """
    每个测试用例执行前清理设备状态
    """
    try:
        # 清理后台应用（可选）
        # device.app_stop_all()
        pass
    except Exception as e:
        logger.warning(f"清理设备状态时出错: {e}")
    
    yield device


@pytest.fixture(scope="function")
def screenshot_on_failure(device, request):
    """
    测试失败时自动截图
    """
    yield
    
    if request.node.rep_call.failed:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = request.node.name
            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
            
            # 确保目录存在
            os.makedirs("screenshots", exist_ok=True)
            
            device.screenshot(screenshot_path)
            logger.info(f"测试失败截图已保存: {screenshot_path}")
        except Exception as e:
            logger.error(f"截图失败: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    用于在测试失败时触发截图
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """
    测试环境初始化
    """
    # 创建必要的目录
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    logger.info("=" * 50)
    logger.info("测试环境初始化完成")
    logger.info("=" * 50)
    
    yield
    
    logger.info("=" * 50)
    logger.info("测试环境清理完成")
    logger.info("=" * 50)

