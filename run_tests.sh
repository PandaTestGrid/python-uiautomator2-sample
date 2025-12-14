#!/bin/bash
# 测试运行脚本

# 设置颜色
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Python UI Automator2 测试框架${NC}"
echo -e "${GREEN}========================================${NC}"

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}创建虚拟环境...${NC}"
    python3 -m venv venv
fi

# 激活虚拟环境
echo -e "${YELLOW}激活虚拟环境...${NC}"
source venv/bin/activate

# 安装依赖
if [ ! -f "venv/.installed" ]; then
    echo -e "${YELLOW}安装依赖包...${NC}"
    pip install -r requirements.txt
    touch venv/.installed
fi

# 检查设备连接
echo -e "${YELLOW}检查设备连接...${NC}"
adb devices

# 运行测试
echo -e "${GREEN}开始运行测试...${NC}"
pytest "$@"

echo -e "${GREEN}测试完成！${NC}"

