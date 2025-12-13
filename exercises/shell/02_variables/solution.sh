#!/bin/bash

# 练习题 2: 变量和计算器 参考答案

# 检查参数数量
if [ $# -ne 3 ]; then
    echo "错误: 需要三个参数 (数字1 运算符 数字2)"
    exit 1
fi

# 获取参数
num1=$1
operator=$2
num2=$3

# 根据运算符执行计算
case $operator in
    +)
        result=$((num1 + num2))
        echo $result
        ;;
    -)
        result=$((num1 - num2))
        echo $result
        ;;
    \*|x)
        result=$((num1 * num2))
        echo $result
        ;;
    /)
        if [ $num2 -eq 0 ]; then
            echo "错误: 除数不能为0"
            exit 1
        fi
        result=$((num1 / num2))
        echo $result
        ;;
    *)
        echo "错误: 不支持的运算符 '$operator'"
        echo "支持的运算符: + - * /"
        exit 1
        ;;
esac
