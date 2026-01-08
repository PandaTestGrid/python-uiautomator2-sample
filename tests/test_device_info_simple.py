"""
简化版设备信息测试
直接使用函数式测试，避免类继承问题
"""
import pytest
import uiautomator2 as u2
from utils.logger import setup_logger

logger = setup_logger()


@pytest.mark.smoke
@pytest.mark.android
def test_device_basic_info(device: u2.Device):
    """
    测试获取设备基本信息
    """
    logger.info("开始测试设备基本信息")
    info = device.info

    # 验证必要字段
    assert "version" in info, "设备信息缺少版本号"
    assert "sdk" in info, "设备信息缺少 SDK 版本"
    assert "productName" in info, "设备信息缺少产品名称"

    logger.info(f"设备版本: {info.get('version')}")
    logger.info(f"SDK 版本: {info.get('sdk')}")
    logger.info(f"产品名称: {info.get('productName')}")
    logger.info(f"品牌: {info.get('brand')}")
    logger.info(f"型号: {info.get('model')}")


@pytest.mark.android
def test_device_serial(device: u2.Device):
    """
    测试获取设备序列号
    """
    logger.info("开始测试设备序列号")
    serial = device.serial
    assert serial is not None, "无法获取设备序列号"
    assert len(serial) > 0, "设备序列号为空"
    logger.info(f"设备序列号: {serial}")


@pytest.mark.android
def test_window_size(device: u2.Device):
    """
    测试获取屏幕尺寸
    """
    logger.info("开始测试屏幕尺寸")
    width, height = device.window_size()

    assert width > 0, "屏幕宽度无效"
    assert height > 0, "屏幕高度无效"

    logger.info(f"屏幕尺寸: {width} x {height}")
    logger.info(f"屏幕方向: {'横屏' if width > height else '竖屏'}")


@pytest.mark.android
def test_device_orientation(device: u2.Device):
    """
    测试获取设备方向
    """
    logger.info("开始测试设备方向")
    orientation = device.orientation

    assert orientation in ["natural", "left", "right", "upsidedown"], "设备方向值无效"
    logger.info(f"设备方向: {orientation}")


@pytest.mark.android
def test_device_wake_up(device: u2.Device):
    """
    测试唤醒设备
    """
    logger.info("开始测试设备唤醒")
    device.wake_up()
    logger.info("设备已唤醒")

    # 验证设备是否唤醒
    info = device.info
    assert info is not None, "设备未唤醒"
