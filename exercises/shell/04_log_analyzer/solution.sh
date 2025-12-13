#!/bin/bash

# 练习题 4: 日志分析器 参考答案

# 检查参数
if [ $# -ne 1 ]; then
    echo "用法: $0 <日志文件>"
    exit 1
fi

logfile=$1

# 检查文件是否存在
if [ ! -f "$logfile" ]; then
    echo "错误: 文件 '$logfile' 不存在"
    exit 1
fi

echo "日志分析报告"
echo "============================================"
echo ""

# 统计总访问次数
total=$(wc -l < "$logfile")
echo "总访问次数: $total"
echo ""

# 统计不同IP地址的访问次数（前5名）
echo "访问次数最多的IP (前5名):"
awk '{print $1}' "$logfile" | sort | uniq -c | sort -rn | head -n 5 | while read count ip; do
    printf "  %3d %s\n" "$count" "$ip"
done
echo ""

# 统计HTTP状态码分布
echo "HTTP状态码分布:"
awk '{print $5}' "$logfile" | sort | uniq -c | sort -rn | while read count code; do
    printf " %4d %s\n" "$count" "$code"
done
echo ""

# 找出访问次数最多的URL（前3名）
echo "访问最多的URL (前3名):"
awk '{print $4}' "$logfile" | sort | uniq -c | sort -rn | head -n 3 | while read count url; do
    printf "  %3d %s\n" "$count" "$url"
done
