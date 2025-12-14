# Python UI Automator2 自动化测试框架

基于 Python、uiautomator2 和 pytest 的 Android 自动化测试框架模板。

## 📋 目录结构

```
python-uiautomator2-sample/
├── base/                  # 基础测试类
│   ├── __init__.py
│   └── base_test.py      # 测试基类
├── config/               # 配置文件
│   ├── __init__.py
│   └── config.py        # 配置管理
├── page_objects/         # 页面对象模式
│   ├── __init__.py
│   ├── base_page.py     # 页面基类
│   └── home_page.py     # 首页示例
├── tests/               # 测试用例
│   ├── __init__.py
│   └── test_example.py  # 示例测试
├── utils/               # 工具类
│   ├── __init__.py
│   ├── device_manager.py  # 设备管理
│   ├── helpers.py        # 辅助函数
│   └── logger.py        # 日志工具
├── screenshots/         # 截图目录（自动创建）
├── reports/             # 测试报告（自动创建）
├── logs/                # 日志文件（自动创建）
├── conftest.py          # pytest 配置和 fixtures
├── pytest.ini           # pytest 配置文件
├── requirements.txt     # 依赖包
└── README.md            # 项目说明
```

## 🚀 快速开始

### 1. 环境准备

#### 安装 Python
确保已安装 Python 3.7 或更高版本。

#### 安装 ADB
确保已安装 Android SDK Platform Tools，并将 `adb` 添加到系统 PATH。

#### 连接设备
```bash
# 连接 Android 设备（USB 或 WiFi）
adb devices

# 或通过 WiFi 连接
adb connect <设备IP>:5555
```

### 2. 安装依赖

```bash
# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 初始化 uiautomator2（首次使用）
python -m uiautomator2 init
```

### 3. 运行测试

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest tests/test_example.py

# 运行指定测试类
pytest tests/test_example.py::TestExample

# 运行指定测试方法
pytest tests/test_example.py::TestExample::test_device_connection

# 运行标记为 smoke 的测试
pytest -m smoke

# 运行标记为 regression 的测试
pytest -m regression

# 并行运行测试（需要 pytest-xdist）
pytest -n auto

# 生成 HTML 报告
pytest --html=reports/report.html --self-contained-html

# 指定设备序列号
DEVICE_SERIAL=设备序列号 pytest
```

## 📝 编写测试用例

### 方式一：继承 BaseTest 类

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
    def test_my_feature(self, device: u2.Device):
        # 使用基类提供的方法
        self.click_element({"text": "按钮"})
        self.input_text({"resourceId": "com.app:id/input"}, "测试文本")
        self.take_screenshot("test_screenshot")
```

### 方式二：函数式测试

```python
import pytest

@pytest.mark.android
def test_simple(device):
    device(text="按钮").click()
    device.screenshot("screenshot.png")
```

## 🎯 页面对象模式

使用页面对象模式可以提高代码的可维护性和复用性：

```python
from page_objects.base_page import BasePage
import uiautomator2 as u2

class LoginPage(BasePage):
    USERNAME_INPUT = {"resourceId": "com.app:id/username"}
    PASSWORD_INPUT = {"resourceId": "com.app:id/password"}
    LOGIN_BUTTON = {"resourceId": "com.app:id/login"}
    
    def login(self, username: str, password: str):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        return self
```

## 🔧 配置说明

### 环境变量

- `DEVICE_SERIAL`: 设备序列号（可选，默认使用 adb devices 中的第一个设备）
- `DEVICE_TIMEOUT`: 设备操作超时时间（默认 10.0 秒）
- `APP_PACKAGE`: 应用包名
- `APP_ACTIVITY`: 应用主 Activity

### pytest.ini 配置

主要配置项：
- `testpaths`: 测试文件目录
- `markers`: 测试标记定义
- `addopts`: 默认命令行选项

## 📊 测试标记

框架预定义了以下测试标记：

- `@pytest.mark.smoke`: 冒烟测试
- `@pytest.mark.regression`: 回归测试
- `@pytest.mark.android`: Android 平台测试
- `@pytest.mark.slow`: 执行较慢的测试

使用示例：
```python
@pytest.mark.smoke
@pytest.mark.android
def test_feature(device):
    pass
```

## 📸 截图功能

测试失败时会自动截图，也可以手动截图：

```python
# 使用基类方法
self.take_screenshot("screenshot_name")

# 直接使用 device
device.screenshot("screenshot.png")
```

## 📋 常用操作

### 元素定位

```python
# 通过 resourceId
device(resourceId="com.app:id/button").click()

# 通过文本
device(text="登录").click()

# 通过描述
device(description="搜索").click()

# 组合定位
device(resourceId="com.app:id/input", text="用户名").click()
```

### 等待操作

```python
# 等待元素出现（基类方法）
self.wait_for_element({"text": "按钮"}, timeout=10.0)

# 使用 uiautomator2 的等待
device(text="按钮").wait(timeout=10.0)
```

### 滑动操作

```python
# 使用基类方法
self.swipe("up", distance=0.5)    # 向上滑动
self.swipe("down", distance=0.5)  # 向下滑动
self.swipe("left", distance=0.5)  # 向左滑动
self.swipe("right", distance=0.5) # 向右滑动

# 直接使用 device
device.swipe(x1, y1, x2, y2, duration=0.5)
```

### 按键操作

```python
# 使用基类方法
self.press_back()    # 返回键
self.press_home()    # Home 键
self.press_recent()  # 最近任务键

# 直接使用 device
device.press("back")
device.press("home")
device.press("recent")
```

## 🐛 调试技巧

1. **查看日志**: 日志文件保存在 `logs/` 目录
2. **查看截图**: 失败截图保存在 `screenshots/` 目录
3. **使用 pytest 调试选项**:
   ```bash
   pytest -v -s  # 显示详细输出
   pytest --pdb  # 失败时进入调试器
   ```

## 📚 更多资源

- [uiautomator2 文档](https://github.com/openatx/uiautomator2)
- [pytest 文档](https://docs.pytest.org/)
- [Android UI Automator 文档](https://developer.android.com/training/testing/ui-automator)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

