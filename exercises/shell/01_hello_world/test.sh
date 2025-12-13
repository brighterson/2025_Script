#!/bin/bash

# 测试脚本：验证 hello.sh 的实现

# 颜色输出
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 计数器
PASS=0
FAIL=0

# 测试函数
test_output() {
    local input="$1"
    local expected="$2"
    local description="$3"
    
    if [ -z "$input" ]; then
        actual=$(./hello.sh)
    else
        actual=$(./hello.sh "$input")
    fi
    
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

# 检查脚本是否存在
if [ ! -f "hello.sh" ]; then
    echo -e "${RED}错误: hello.sh 文件不存在${NC}"
    exit 1
fi

# 检查脚本是否有执行权限
if [ ! -x "hello.sh" ]; then
    echo -e "${RED}错误: hello.sh 没有执行权限，请运行: chmod +x hello.sh${NC}"
    exit 1
fi

echo "开始测试 hello.sh..."
echo ""

# 运行测试
test_output "" "Hello, World!" "无参数时输出 Hello, World!"
test_output "Alice" "Hello, Alice!" "参数为 Alice"
test_output "Bob" "Hello, Bob!" "参数为 Bob"
test_output "世界" "Hello, 世界!" "参数为中文"

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
