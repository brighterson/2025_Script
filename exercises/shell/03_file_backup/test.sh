#!/bin/bash

# 测试脚本：验证 backup.sh 的实现

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

PASS=0
FAIL=0

# 清理测试文件
cleanup() {
    rm -f test_file.txt test_file.txt.backup.*
}

# 在脚本退出时清理
trap cleanup EXIT

if [ ! -f "backup.sh" ]; then
    echo -e "${RED}错误: backup.sh 文件不存在${NC}"
    exit 1
fi

if [ ! -x "backup.sh" ]; then
    echo -e "${RED}错误: backup.sh 没有执行权限${NC}"
    exit 1
fi

echo "开始测试 backup.sh..."
echo ""

# 测试1：备份存在的文件
echo "Test content" > test_file.txt
output=$(./backup.sh test_file.txt)

if [[ "$output" == *"备份成功"* ]]; then
    # 检查备份文件是否存在
    backup_count=$(ls test_file.txt.backup.* 2>/dev/null | wc -l)
    if [ $backup_count -eq 1 ]; then
        # 检查备份内容是否正确
        backup_file=$(ls test_file.txt.backup.*)
        if diff -q test_file.txt "$backup_file" >/dev/null; then
            echo -e "${GREEN}✓ PASS${NC}: 文件备份成功"
            ((PASS++))
        else
            echo -e "${RED}✗ FAIL${NC}: 备份文件内容不匹配"
            ((FAIL++))
        fi
    else
        echo -e "${RED}✗ FAIL${NC}: 备份文件未创建或创建了多个"
        ((FAIL++))
    fi
else
    echo -e "${RED}✗ FAIL${NC}: 备份失败或输出信息错误"
    echo "  输出: $output"
    ((FAIL++))
fi

# 测试2：尝试备份不存在的文件
output=$(./backup.sh nonexistent_file.txt 2>&1)
if [[ "$output" == *"不存在"* ]] || [[ "$output" == *"错误"* ]]; then
    echo -e "${GREEN}✓ PASS${NC}: 正确处理文件不存在的情况"
    ((PASS++))
else
    echo -e "${RED}✗ FAIL${NC}: 未正确处理文件不存在的情况"
    echo "  输出: $output"
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
