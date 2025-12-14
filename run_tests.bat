@echo off
REM Windows 测试运行脚本

echo ========================================
echo   Python UI Automator2 测试框架
echo ========================================

REM 检查虚拟环境
if not exist "venv" (
    echo 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call venv\Scripts\activate.bat

REM 安装依赖
if not exist "venv\.installed" (
    echo 安装依赖包...
    pip install -r requirements.txt
    type nul > venv\.installed
)

REM 检查设备连接
echo 检查设备连接...
adb devices

REM 运行测试
echo 开始运行测试...
pytest %*

echo 测试完成！

