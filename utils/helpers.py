"""
辅助工具函数
"""
import time
import logging
from typing import Optional, Callable, Any
from functools import wraps

logger = logging.getLogger(__name__)


def wait_for(
    condition: Callable[[], bool],
    timeout: float = 10.0,
    interval: float = 0.5,
    error_message: str = "等待条件超时"
) -> bool:
    """
    等待某个条件满足
    
    Args:
        condition: 返回布尔值的函数
        timeout: 超时时间（秒）
        interval: 检查间隔（秒）
        error_message: 超时时的错误消息
    
    Returns:
        True 如果条件满足，否则 False
    """
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            if condition():
                return True
        except Exception as e:
            logger.debug(f"等待条件检查时出错: {e}")
        
        time.sleep(interval)
    
    logger.warning(f"{error_message} (超时: {timeout}秒)")
    return False


def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)):
    """
    重试装饰器
    
    Args:
        max_attempts: 最大尝试次数
        delay: 重试延迟（秒）
        exceptions: 需要重试的异常类型
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts:
                        logger.warning(
                            f"{func.__name__} 第 {attempt} 次尝试失败: {e}, "
                            f"{delay} 秒后重试..."
                        )
                        time.sleep(delay)
                    else:
                        logger.error(f"{func.__name__} 所有尝试均失败")
            
            raise last_exception
        
        return wrapper
    return decorator


def safe_execute(func: Callable, default_value: Any = None, *args, **kwargs) -> Any:
    """
    安全执行函数，捕获异常并返回默认值
    
    Args:
        func: 要执行的函数
        default_value: 异常时的默认返回值
        *args, **kwargs: 传递给函数的参数
    
    Returns:
        函数返回值或默认值
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.warning(f"执行 {func.__name__} 时出错: {e}")
        return default_value


def format_time(seconds: float) -> str:
    """
    格式化时间（秒）为可读字符串
    
    Args:
        seconds: 秒数
    
    Returns:
        格式化后的时间字符串
    """
    if seconds < 60:
        return f"{seconds:.2f}秒"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}分{secs:.2f}秒"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours}小时{minutes}分{secs:.2f}秒"

