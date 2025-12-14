# 测试用例说明

本目录包含各种类型的自动化测试用例，涵盖了 Android 自动化测试的常见场景。

## 测试文件列表

### 1. test_example.py
**示例测试用例**
- `test_device_connection` - 测试设备连接
- `test_screenshot` - 测试截图功能
- `test_swipe_gesture` - 测试滑动手势
- `test_home_page_example` - 页面对象模式示例
- `test_app_launch` - 测试应用启动
- `test_simple_example` - 简单函数式测试示例

### 2. test_app_operations.py
**应用操作测试用例**
- `test_app_start_and_stop` - 测试应用启动和关闭
- `test_app_clear_data` - 测试清除应用数据
- `test_app_info` - 测试获取应用信息
- `test_app_list` - 测试获取已安装应用列表
- `test_app_running_list` - 测试获取正在运行的应用列表
- `test_app_wait_activity` - 测试等待特定 Activity 出现

### 3. test_element_operations.py
**元素操作测试用例**
- `test_find_element_by_text` - 测试通过文本查找元素
- `test_find_element_by_resource_id` - 测试通过 resourceId 查找元素
- `test_find_element_by_description` - 测试通过描述查找元素
- `test_element_exists` - 测试检查元素是否存在
- `test_element_count` - 测试获取匹配元素的数量
- `test_element_get_info` - 测试获取元素信息
- `test_input_text` - 测试输入文本
- `test_clear_text` - 测试清空文本
- `test_long_click` - 测试长按操作

### 4. test_gesture_operations.py
**手势操作测试用例**
- `test_swipe_up` - 测试向上滑动
- `test_swipe_down` - 测试向下滑动
- `test_swipe_left` - 测试向左滑动
- `test_swipe_right` - 测试向右滑动
- `test_swipe_custom` - 测试自定义滑动
- `test_drag` - 测试拖拽操作
- `test_pinch_in` - 测试捏合手势（缩小）
- `test_pinch_out` - 测试放大手势
- `test_scroll` - 测试滚动操作
- `test_fling` - 测试快速滑动（fling）

### 5. test_device_info.py
**设备信息测试用例**
- `test_device_basic_info` - 测试获取设备基本信息
- `test_device_serial` - 测试获取设备序列号
- `test_window_size` - 测试获取屏幕尺寸
- `test_display_info` - 测试获取显示信息
- `test_device_orientation` - 测试获取设备方向
- `test_device_wake_up` - 测试唤醒设备
- `test_device_screen_on` - 测试检查屏幕是否点亮
- `test_device_battery_info` - 测试获取电池信息
- `test_device_memory_info` - 测试获取内存信息
- `test_device_cpu_info` - 测试获取 CPU 信息

### 6. test_key_operations.py
**按键操作测试用例**
- `test_press_home` - 测试按 Home 键
- `test_press_back` - 测试按返回键
- `test_press_recent` - 测试按最近任务键
- `test_press_menu` - 测试按菜单键
- `test_press_power` - 测试按电源键（锁屏/解锁）
- `test_press_volume_up` - 测试按音量加键
- `test_press_volume_down` - 测试按音量减键
- `test_press_enter` - 测试按回车键
- `test_press_keycode` - 测试通过键码按键
- `test_key_combination` - 测试组合键

### 7. test_wait_operations.py
**等待操作测试用例**
- `test_wait_for_element` - 测试等待元素出现
- `test_wait_for_element_timeout` - 测试等待元素超时
- `test_wait_for_app` - 测试等待应用启动
- `test_wait_for_condition` - 测试等待自定义条件
- `test_wait_with_retry` - 测试带重试的等待
- `test_implicit_wait` - 测试隐式等待
- `test_sleep_wait` - 测试固定时间等待
- `test_wait_until_gone` - 测试等待元素消失

## 运行测试

### 运行所有测试
```bash
pytest
```

### 运行指定测试文件
```bash
pytest tests/test_app_operations.py
```

### 运行指定测试类
```bash
pytest tests/test_element_operations.py::TestElementOperations
```

### 运行指定测试方法
```bash
pytest tests/test_app_operations.py::TestAppOperations::test_app_start_and_stop
```

### 运行标记为 smoke 的测试
```bash
pytest -m smoke
```

### 运行标记为 regression 的测试
```bash
pytest -m regression
```

### 并行运行测试
```bash
pytest -n auto
```

## 测试标记说明

- `@pytest.mark.smoke` - 冒烟测试，快速验证基本功能
- `@pytest.mark.regression` - 回归测试，全面验证功能
- `@pytest.mark.android` - Android 平台测试
- `@pytest.mark.slow` - 执行较慢的测试用例

## 注意事项

1. **设备连接**: 运行测试前确保设备已通过 ADB 连接
2. **应用包名**: 部分测试用例使用系统设置应用（`com.android.settings`）作为示例，实际使用时需要根据目标应用调整
3. **元素定位**: 测试用例中的元素定位器需要根据实际应用的 UI 结构进行调整
4. **等待时间**: 某些测试包含固定的等待时间，可能需要根据设备性能调整
5. **截图保存**: 测试失败时会自动截图，截图保存在 `screenshots/` 目录

## 自定义测试用例

参考现有测试用例的结构，可以轻松创建新的测试用例：

1. 继承 `BaseTest` 类
2. 使用 `@pytest.fixture(autouse=True)` 设置测试环境
3. 使用基类提供的方法（如 `click_element`, `input_text`, `swipe` 等）
4. 添加适当的测试标记
5. 使用 `self.logger` 记录测试日志
6. 使用 `self.take_screenshot()` 在关键步骤截图

## 示例

```python
import pytest
import uiautomator2 as u2
from base.base_test import BaseTest

class TestMyFeature(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, device: u2.Device):
        super().__init__(device)
        self.setup_method()
        yield
        self.teardown_method()
    
    @pytest.mark.smoke
    @pytest.mark.android
    def test_my_feature(self, device: u2.Device):
        # 启动应用
        device.app_start("com.example.app")
        
        # 点击元素
        self.click_element({"text": "按钮"})
        
        # 输入文本
        self.input_text({"resourceId": "com.example.app:id/input"}, "测试")
        
        # 截图
        self.take_screenshot("test_step")
        
        # 验证结果
        text = self.get_text({"resourceId": "com.example.app:id/result"})
        assert "预期结果" in text
```

