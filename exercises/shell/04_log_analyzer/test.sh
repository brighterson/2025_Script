#!/bin/bash

# 测试脚本：验证 log_analyzer.sh 的实现

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

PASS=0
FAIL=0

# 清理测试文件
cleanup() {
    rm -f test_access.log
}

trap cleanup EXIT

# 创建测试日志文件
create_test_log() {
    cat > test_access.log << 'EOF'
192.168.1.1 2025-01-13T10:00:01 GET /index.html 200
192.168.1.2 2025-01-13T10:00:05 POST /api/login 200
192.168.1.1 2025-01-13T10:00:10 GET /about.html 200
192.168.1.3 2025-01-13T10:00:15 GET /index.html 404
192.168.1.1 2025-01-13T10:00:20 GET /index.html 200
192.168.1.2 2025-01-13T10:00:25 GET /contact.html 200
192.168.1.4 2025-01-13T10:00:30 GET /index.html 500
192.168.1.1 2025-01-13T10:00:35 POST /api/login 200
192.168.1.3 2025-01-13T10:00:40 GET /about.html 404
192.168.1.1 2025-01-13T10:00:45 GET /index.html 200
EOF
}

if [ ! -f "log_analyzer.sh" ]; then
    echo -e "${RED}错误: log_analyzer.sh 文件不存在${NC}"
    exit 1
fi

if [ ! -x "log_analyzer.sh" ]; then
    echo -e "${RED}错误: log_analyzer.sh 没有执行权限${NC}"
    exit 1
fi

echo "开始测试 log_analyzer.sh..."
echo ""

# 创建测试日志
create_test_log

# 运行脚本
output=$(./log_analyzer.sh test_access.log)

# 测试1：检查总访问次数
if echo "$output" | grep -q "总访问次数.*10"; then
    echo -e "${GREEN}✓ PASS${NC}: 正确统计总访问次数"
    ((PASS++))
else
    echo -e "${RED}✗ FAIL${NC}: 总访问次数统计错误"
    ((FAIL++))
fi

# 测试2：检查是否包含IP统计
if echo "$output" | grep -q "192.168.1.1"; then
    echo -e "${GREEN}✓ PASS${NC}: 包含IP地址统计"
    ((PASS++))
else
    echo -e "${RED}✗ FAIL${NC}: 未找到IP地址统计"
    ((FAIL++))
fi

# 测试3：检查是否包含状态码统计
if echo "$output" | grep -q "200" && echo "$output" | grep -q "404"; then
    echo -e "${GREEN}✓ PASS${NC}: 包含HTTP状态码统计"
    ((PASS++))
else
    echo -e "${RED}✗ FAIL${NC}: 未找到HTTP状态码统计"
    ((FAIL++))
fi

# 测试4：检查是否包含URL统计
if echo "$output" | grep -q "/index.html"; then
    echo -e "${GREEN}✓ PASS${NC}: 包含URL统计"
    ((PASS++))
else
    echo -e "${RED}✗ FAIL${NC}: 未找到URL统计"
    ((FAIL++))
fi

echo ""
echo "测试完成！"
echo -e "${GREEN}通过: $PASS${NC}"
echo -e "${RED}失败: $FAIL${NC}"

if [ $FAIL -eq 0 ]; then
    echo -e "${GREEN}恭喜！所有测试通过！${NC}"
    exit 0
else
    exit 1
fi
