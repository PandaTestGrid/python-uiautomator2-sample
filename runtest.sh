#!/bin/bash
# 测试运行脚本

# 设置颜色
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Python UI Automator2 测试框架${NC}"
echo -e "${GREEN}========================================${NC}"

# 运行测试
echo -e "${GREEN}开始运行测试...${NC}"
pytest "$@"

echo -e "${GREEN}测试完成！${NC}"
echo -e "${YELLOW}HTML 报告: reports/report.html${NC}"
echo -e "${YELLOW}JSON 报告: reports/report.json${NC}"

