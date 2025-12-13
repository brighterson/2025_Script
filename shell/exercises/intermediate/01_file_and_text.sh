#!/bin/bash

###############################################################################
# Shell 中级练习题 - Shell Intermediate Exercises
#
# 这些练习涵盖了文件处理、文本处理、进程管理等中级主题
# These exercises cover file handling, text processing, process management, and other intermediate topics
#
# 作者 (Author): Your Name
# 日期 (Date): 2025
###############################################################################

# 练习1: 文件读取和处理
# Exercise 1: File Reading and Processing
exercise_01_file_reading() {
    echo "=== 练习1: 文件读取和处理 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 读取文件的每一行
    # 2. 统计文件行数、单词数、字符数
    # 3. 处理CSV文件
    # 4. 使用IFS分割字段
    
    # 提示 (Hints):
    # while IFS= read -r line; do
    #     echo "行: $line"
    # done < "file.txt"
    #
    # line_count=$(wc -l < "file.txt")
    # word_count=$(wc -w < "file.txt")
    # char_count=$(wc -c < "file.txt")
    #
    # while IFS=',' read -r col1 col2 col3; do
    #     echo "列1: $col1, 列2: $col2, 列3: $col3"
    # done < "data.csv"
    
    :
}

# 练习2: 文件写入和追加
# Exercise 2: File Writing and Appending
exercise_02_file_writing() {
    echo -e "\n=== 练习2: 文件写入和追加 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 创建新文件并写入内容
    # 2. 追加内容到文件
    # 3. 使用heredoc写入多行
    # 4. 创建临时文件
    
    # 提示 (Hints):
    # echo "第一行" > /tmp/output.txt
    # echo "第二行" >> /tmp/output.txt
    #
    # cat > /tmp/multi_line.txt << 'EOF'
    # 第一行
    # 第二行
    # 第三行
    # EOF
    #
    # temp_file=$(mktemp)
    # echo "临时内容" > "$temp_file"
    # rm "$temp_file"
    
    :
}

# 练习3: grep和正则表达式
# Exercise 3: grep and Regular Expressions
exercise_03_grep_regex() {
    echo -e "\n=== 练习3: grep和正则表达式 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用grep搜索文本
    # 2. 使用正则表达式匹配模式
    # 3. 使用grep选项：-i, -v, -c, -n, -r
    # 4. 使用扩展正则表达式 (grep -E)
    
    # 提示 (Hints):
    # echo "Hello World" | grep "Hello"
    # echo "hello world" | grep -i "HELLO"  # 忽略大小写
    # grep -c "pattern" file.txt  # 计数匹配行
    # grep -n "pattern" file.txt  # 显示行号
    # grep -v "pattern" file.txt  # 反向匹配
    #
    # echo "email@example.com" | grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    :
}

# 练习4: sed文本替换
# Exercise 4: sed Text Substitution
exercise_04_sed() {
    echo -e "\n=== 练习4: sed文本替换 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 基本替换
    # 2. 全局替换
    # 3. 删除行
    # 4. 插入和追加行
    
    # 提示 (Hints):
    # echo "Hello World" | sed 's/World/Shell/'
    # echo "one two one" | sed 's/one/three/g'  # 全局替换
    # sed '2d' file.txt  # 删除第2行
    # sed '/pattern/d' file.txt  # 删除匹配的行
    # sed '2i\新行' file.txt  # 在第2行前插入
    # sed '2a\新行' file.txt  # 在第2行后追加
    
    :
}

# 练习5: awk文本处理
# Exercise 5: awk Text Processing
exercise_05_awk() {
    echo -e "\n=== 练习5: awk文本处理 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 打印特定列
    # 2. 使用条件过滤
    # 3. 计算和统计
    # 4. 使用内置变量 (NR, NF, FS)
    
    # 提示 (Hints):
    # echo "列1 列2 列3" | awk '{print $1, $3}'
    # awk '$3 > 50 {print $0}' data.txt  # 打印第3列大于50的行
    # awk '{sum += $1} END {print sum}' numbers.txt  # 计算第1列的和
    # awk 'NR == 2 {print}' file.txt  # 打印第2行
    # awk '{print NF}' file.txt  # 打印每行的字段数
    # awk -F',' '{print $1}' data.csv  # 使用逗号作为分隔符
    
    :
}

# 练习6: 进程管理
# Exercise 6: Process Management
exercise_06_processes() {
    echo -e "\n=== 练习6: 进程管理 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 列出进程 (ps)
    # 2. 后台运行命令 (&)
    # 3. 使用jobs查看后台任务
    # 4. 等待进程完成 (wait)
    
    # 提示 (Hints):
    # ps aux | grep bash
    # ps -ef | head -10
    #
    # sleep 5 &
    # pid=$!
    # echo "后台进程PID: $pid"
    # wait $pid
    # echo "进程完成"
    
    :
}

# 练习7: 查找文件
# Exercise 7: Finding Files
exercise_07_find() {
    echo -e "\n=== 练习7: 查找文件 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 按名称查找文件
    # 2. 按类型查找 (-type f/d)
    # 3. 按大小查找
    # 4. 按修改时间查找
    # 5. 对查找结果执行命令
    
    # 提示 (Hints):
    # find /tmp -name "*.txt"
    # find . -type f -name "*.sh"
    # find . -type d -name "test*"
    # find . -size +1M  # 大于1MB的文件
    # find . -mtime -7  # 最近7天修改的文件
    # find . -name "*.txt" -exec cat {} \;
    
    :
}

# 练习8: 关联数组
# Exercise 8: Associative Arrays
exercise_08_associative_arrays() {
    echo -e "\n=== 练习8: 关联数组 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 声明关联数组
    # 2. 添加键值对
    # 3. 访问值
    # 4. 遍历关联数组
    
    # 提示 (Hints):
    # declare -A scores
    # scores["张三"]=95
    # scores["李四"]=88
    # scores["王五"]=92
    #
    # echo "张三的分数: ${scores["张三"]}"
    #
    # for name in "${!scores[@]}"; do
    #     echo "$name: ${scores[$name]}"
    # done
    
    :
}

# 练习9: getopts参数解析
# Exercise 9: getopts Argument Parsing
exercise_09_getopts() {
    echo -e "\n=== 练习9: getopts参数解析 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用getopts解析单字符选项
    # 2. 处理带参数的选项
    # 3. 处理无效选项
    
    # 提示 (Hints):
    # parse_options() {
    #     while getopts ":i:o:vh" opt; do
    #         case $opt in
    #             i) input_file="$OPTARG" ;;
    #             o) output_file="$OPTARG" ;;
    #             v) verbose=1 ;;
    #             h) echo "Usage: $0 -i input -o output [-v]"; return ;;
    #             \?) echo "无效选项: -$OPTARG" >&2; return 1 ;;
    #             :) echo "选项 -$OPTARG 需要参数" >&2; return 1 ;;
    #         esac
    #     done
    # }
    
    :
}

# 练习10: 信号处理
# Exercise 10: Signal Handling
exercise_10_signals() {
    echo -e "\n=== 练习10: 信号处理 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用trap捕获信号
    # 2. 清理临时文件
    # 3. 捕获脚本退出
    # 4. 处理中断信号 (SIGINT)
    
    # 提示 (Hints):
    # cleanup() {
    #     echo "执行清理..."
    #     rm -f /tmp/temp_file
    # }
    # trap cleanup EXIT
    #
    # interrupt_handler() {
    #     echo "收到中断信号"
    #     exit 1
    # }
    # trap interrupt_handler INT
    #
    # echo "创建临时文件..."
    # touch /tmp/temp_file
    # sleep 10
    
    :
}

###############################################################################
# 主函数 (Main Function)
###############################################################################

main() {
    echo "Shell 中级练习题"
    echo "================================================"
    echo
    
    # 运行所有练习
    exercise_01_file_reading
    exercise_02_file_writing
    exercise_03_grep_regex
    exercise_04_sed
    exercise_05_awk
    exercise_06_processes
    exercise_07_find
    exercise_08_associative_arrays
    exercise_09_getopts
    exercise_10_signals
    
    echo -e "\n所有练习完成！"
}

# 运行主函数
main "$@"
