#!/bin/bash

###############################################################################
# Shell 初级练习题 - Shell Beginner Exercises
#
# 这些练习涵盖了Shell的基础知识，包括变量、条件语句、循环和函数
# These exercises cover Shell basics including variables, conditionals, loops, and functions
#
# 作者 (Author): Your Name
# 日期 (Date): 2025
###############################################################################

# 练习1: 变量和输出
# Exercise 1: Variables and Output
exercise_01_variables() {
    echo "=== 练习1: 变量和输出 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 创建字符串变量并打印
    # 2. 创建数字变量并进行算术运算
    # 3. 使用命令替换
    # 4. 使用echo的不同选项
    
    # 提示 (Hints):
    # name="张三"
    # age=25
    # echo "姓名: $name"
    # echo "年龄: $age"
    # current_date=$(date +%Y-%m-%d)
    # echo "当前日期: $current_date"
    
    :
}

# 练习2: 字符串操作
# Exercise 2: String Operations
exercise_02_strings() {
    echo -e "\n=== 练习2: 字符串操作 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 字符串连接
    # 2. 获取字符串长度
    # 3. 字符串切片
    # 4. 字符串替换
    
    # 提示 (Hints):
    # str1="Hello"
    # str2="World"
    # combined="$str1 $str2"
    # length=${#combined}
    # echo "长度: $length"
    # 
    # text="Hello World"
    # echo "${text:0:5}"  # 获取前5个字符
    # echo "${text/World/Shell}"  # 替换
    
    :
}

# 练习3: 条件语句
# Exercise 3: Conditional Statements
exercise_03_conditionals() {
    echo -e "\n=== 练习3: 条件语句 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用if-elif-else
    # 2. 数字比较
    # 3. 字符串比较
    # 4. 文件测试
    
    # 提示 (Hints):
    # number=10
    # if [ $number -gt 5 ]; then
    #     echo "大于5"
    # elif [ $number -eq 5 ]; then
    #     echo "等于5"
    # else
    #     echo "小于5"
    # fi
    #
    # str1="abc"
    # str2="abc"
    # if [ "$str1" = "$str2" ]; then
    #     echo "字符串相等"
    # fi
    #
    # if [ -f "file.txt" ]; then
    #     echo "文件存在"
    # fi
    
    :
}

# 练习4: 循环
# Exercise 4: Loops
exercise_04_loops() {
    echo -e "\n=== 练习4: 循环 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. for循环遍历数字范围
    # 2. for循环遍历数组
    # 3. while循环
    # 4. until循环
    # 5. break和continue
    
    # 提示 (Hints):
    # for i in {1..5}; do
    #     echo "数字: $i"
    # done
    #
    # fruits=("苹果" "香蕉" "橙子")
    # for fruit in "${fruits[@]}"; do
    #     echo "水果: $fruit"
    # done
    #
    # counter=1
    # while [ $counter -le 5 ]; do
    #     echo "计数: $counter"
    #     ((counter++))
    # done
    
    :
}

# 练习5: 数组
# Exercise 5: Arrays
exercise_05_arrays() {
    echo -e "\n=== 练习5: 数组 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 创建数组
    # 2. 访问数组元素
    # 3. 获取数组长度
    # 4. 添加元素到数组
    # 5. 遍历数组
    
    # 提示 (Hints):
    # numbers=(1 2 3 4 5)
    # echo "第一个元素: ${numbers[0]}"
    # echo "所有元素: ${numbers[@]}"
    # echo "数组长度: ${#numbers[@]}"
    # numbers+=(6)
    # 
    # for num in "${numbers[@]}"; do
    #     echo "元素: $num"
    # done
    
    :
}

# 练习6: 函数
# Exercise 6: Functions
exercise_06_functions() {
    echo -e "\n=== 练习6: 函数 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 创建简单函数
    # 2. 函数参数
    # 3. 函数返回值
    # 4. 局部变量和全局变量
    
    # 提示 (Hints):
    # greet() {
    #     echo "你好!"
    # }
    # greet
    #
    # greet_name() {
    #     local name=$1
    #     echo "你好, $name!"
    # }
    # greet_name "张三"
    #
    # add() {
    #     local a=$1
    #     local b=$2
    #     echo $((a + b))
    # }
    # result=$(add 5 3)
    # echo "结果: $result"
    
    :
}

# 练习7: 算术运算
# Exercise 7: Arithmetic Operations
exercise_07_arithmetic() {
    echo -e "\n=== 练习7: 算术运算 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 基本算术运算（+, -, *, /, %）
    # 2. 使用 $(( )) 进行计算
    # 3. 使用 let 命令
    # 4. 使用 expr 命令
    
    # 提示 (Hints):
    # a=10
    # b=3
    # echo "加法: $((a + b))"
    # echo "减法: $((a - b))"
    # echo "乘法: $((a * b))"
    # echo "除法: $((a / b))"
    # echo "取模: $((a % b))"
    #
    # let result=a+b
    # echo "let结果: $result"
    
    :
}

# 练习8: 命令行参数
# Exercise 8: Command Line Arguments
exercise_08_arguments() {
    echo -e "\n=== 练习8: 命令行参数 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 访问位置参数 $1, $2, etc.
    # 2. 使用 $# 获取参数个数
    # 3. 使用 $@ 和 $* 获取所有参数
    # 4. 使用 shift 命令
    
    # 提示 (Hints):
    # echo "参数个数: $#"
    # echo "所有参数: $@"
    # echo "第一个参数: $1"
    # echo "第二个参数: $2"
    
    # 注意: 在此练习函数中，参数是传递给函数的，不是脚本的
    
    :
}

# 练习9: 文件测试
# Exercise 9: File Tests
exercise_09_file_tests() {
    echo -e "\n=== 练习9: 文件测试 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 测试文件是否存在 (-e, -f)
    # 2. 测试目录是否存在 (-d)
    # 3. 测试文件权限 (-r, -w, -x)
    # 4. 测试文件大小 (-s)
    
    # 提示 (Hints):
    # file="test.txt"
    # if [ -f "$file" ]; then
    #     echo "文件存在"
    # fi
    #
    # if [ -d "/tmp" ]; then
    #     echo "目录存在"
    # fi
    #
    # if [ -r "$file" ]; then
    #     echo "文件可读"
    # fi
    
    :
}

# 练习10: 输入输出重定向
# Exercise 10: Input/Output Redirection
exercise_10_redirection() {
    echo -e "\n=== 练习10: 输入输出重定向 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 输出重定向 >
    # 2. 追加重定向 >>
    # 3. 输入重定向 <
    # 4. 管道 |
    # 5. 错误重定向 2>
    
    # 提示 (Hints):
    # echo "Hello" > /tmp/output.txt
    # echo "World" >> /tmp/output.txt
    # 
    # ls -l | grep ".txt"
    # 
    # ls non_existent_file 2> /tmp/error.txt
    # 
    # ls -l 2>&1 | tee /tmp/output_and_errors.txt
    
    :
}

###############################################################################
# 主函数 (Main Function)
###############################################################################

main() {
    echo "Shell 初级练习题"
    echo "================================================"
    echo
    
    # 运行所有练习
    exercise_01_variables
    exercise_02_strings
    exercise_03_conditionals
    exercise_04_loops
    exercise_05_arrays
    exercise_06_functions
    exercise_07_arithmetic
    exercise_08_arguments
    exercise_09_file_tests
    exercise_10_redirection
    
    echo -e "\n所有练习完成！"
}

# 运行主函数
main "$@"
