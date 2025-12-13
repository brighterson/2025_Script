#!/bin/bash

# 练习题 3: 文件备份工具 参考答案

# 检查参数
if [ $# -ne 1 ]; then
    echo "用法: $0 <文件路径>"
    exit 1
fi

filename=$1

# 检查文件是否存在
if [ ! -f "$filename" ]; then
    echo "错误: 文件 '$filename' 不存在"
    exit 1
fi

# 生成时间戳
timestamp=$(date +%Y%m%d_%H%M%S)

# 创建备份文件名
backup_name="${filename}.backup.${timestamp}"

# 执行备份
cp "$filename" "$backup_name"

# 检查备份是否成功
if [ $? -eq 0 ]; then
    echo "备份成功: $backup_name"
else
    echo "错误: 备份失败"
    exit 1
fi
