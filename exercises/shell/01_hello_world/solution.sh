#!/bin/bash

# 练习题 1: Hello World 参考答案

# 检查是否提供了参数
if [ -z "$1" ]; then
    echo "Hello, World!"
else
    echo "Hello, $1!"
fi
