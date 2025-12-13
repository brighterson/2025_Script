#!/bin/bash

# 测试脚本：验证 calculator.sh 的实现

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

PASS=0
FAIL=0

test_calc() {
    local num1="$1"
    local op="$2"
    local num2="$3"
    local expected="$4"
    local description="$5"
    
    actual=$(./calculator.sh "$num1" "$op" "$num2" 2>&1)
    
    if [ "$actual" = "$expected" ]; then
        echo -e "${GREEN}✓ PASS${NC}: $description"
        ((PASS++))
    else
        echo -e "${RED}✗ FAIL${NC}: $description"
        echo "  Expected: $expected"
        echo "  Actual:   $actual"
        ((FAIL++))
    fi
}

if [ ! -f "calculator.sh" ]; then
    echo -e "${RED}错误: calculator.sh 文件不存在${NC}"
    exit 1
fi

if [ ! -x "calculator.sh" ]; then
    echo -e "${RED}错误: calculator.sh 没有执行权限${NC}"
    exit 1
fi

echo "开始测试 calculator.sh..."
echo ""

# 运行测试
test_calc 10 + 5 "15" "加法: 10 + 5 = 15"
test_calc 20 - 8 "12" "减法: 20 - 8 = 12"
test_calc 6 \* 7 "42" "乘法: 6 * 7 = 42"
test_calc 100 / 4 "25" "除法: 100 / 4 = 25"
test_calc 15 / 2 "7" "除法取整: 15 / 2 = 7"

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
