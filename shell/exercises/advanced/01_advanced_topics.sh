#!/bin/bash

###############################################################################
# Shell 高级练习题 - Shell Advanced Exercises
#
# 这些练习涵盖了高级文本处理、脚本优化、调试等高级主题
# These exercises cover advanced text processing, script optimization, debugging, and other advanced topics
#
# 作者 (Author): Your Name
# 日期 (Date): 2025
###############################################################################

# 练习1: 复杂的文本处理管道
# Exercise 1: Complex Text Processing Pipelines
exercise_01_pipelines() {
    echo "=== 练习1: 复杂的文本处理管道 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 组合多个命令处理数据
    # 2. 使用tee分流输出
    # 3. 使用xargs批量处理
    # 4. 复杂的管道链
    
    # 提示 (Hints):
    # cat file.txt | grep "pattern" | sort | uniq -c | sort -rn | head -10
    #
    # find . -name "*.log" | xargs grep "ERROR" | sort | uniq
    #
    # ps aux | tee /tmp/processes.txt | grep python | wc -l
    #
    # cat data.txt | awk '{print $1}' | sort -u | while read line; do
    #     echo "处理: $line"
    # done
    
    :
}

# 练习2: 高级正则表达式
# Exercise 2: Advanced Regular Expressions
exercise_02_advanced_regex() {
    echo -e "\n=== 练习2: 高级正则表达式 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用捕获组
    # 2. 非捕获组和前后查找
    # 3. 复杂的模式匹配
    # 4. 使用perl兼容的正则表达式
    
    # 提示 (Hints):
    # echo "2025-01-15" | sed -E 's/([0-9]{4})-([0-9]{2})-([0-9]{2})/\3\/\2\/\1/'
    #
    # echo "email@example.com" | grep -oP '[\w.]+(?=@)'  # 提取@前面的部分
    #
    # echo "价格: $100.50" | grep -oP '\$\d+\.\d+'
    
    :
}

# 练习3: 脚本调试和错误处理
# Exercise 3: Script Debugging and Error Handling
exercise_03_debugging() {
    echo -e "\n=== 练习3: 脚本调试和错误处理 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用set -x启用调试模式
    # 2. 使用set -e遇错即停
    # 3. 使用set -u检测未定义变量
    # 4. 自定义错误处理函数
    
    # 提示 (Hints):
    # set -x  # 启用调试
    # echo "调试信息会显示"
    # set +x  # 关闭调试
    #
    # set -e  # 遇到错误立即退出
    # set -u  # 使用未定义变量时报错
    # set -o pipefail  # 管道中任何命令失败都返回错误
    #
    # error_handler() {
    #     echo "错误发生在第 $1 行" >&2
    #     exit 1
    # }
    # trap 'error_handler $LINENO' ERR
    
    :
}

# 练习4: 性能优化
# Exercise 4: Performance Optimization
exercise_04_performance() {
    echo -e "\n=== 练习4: 性能优化 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 避免不必要的子shell
    # 2. 使用内置命令而非外部命令
    # 3. 批量处理而非逐个处理
    # 4. 使用time命令测量性能
    
    # 提示 (Hints):
    # 慢: cat file.txt | while read line; do echo $line; done
    # 快: while read line; do echo $line; done < file.txt
    #
    # 慢: result=$(cat file.txt)
    # 快: result=$(<file.txt)
    #
    # time {
    #     # 要测量的代码
    # }
    
    :
}

# 练习5: 并行处理
# Exercise 5: Parallel Processing
exercise_05_parallel() {
    echo -e "\n=== 练习5: 并行处理 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用&并行执行多个任务
    # 2. 使用wait等待所有后台任务
    # 3. 限制并发数量
    # 4. 使用GNU parallel（如果可用）
    
    # 提示 (Hints):
    # for i in {1..5}; do
    #     (
    #         echo "任务 $i 开始"
    #         sleep $((RANDOM % 3 + 1))
    #         echo "任务 $i 完成"
    #     ) &
    # done
    # wait
    # echo "所有任务完成"
    #
    # 限制并发数:
    # max_jobs=3
    # job_count=0
    # for i in {1..10}; do
    #     ((job_count >= max_jobs)) && wait -n
    #     (sleep 1; echo "任务 $i") &
    #     ((job_count++))
    # done
    # wait
    
    :
}

# 练习6: 网络操作
# Exercise 6: Network Operations
exercise_06_network() {
    echo -e "\n=== 练习6: 网络操作 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用curl下载文件
    # 2. 解析HTTP响应
    # 3. 使用nc进行端口测试
    # 4. 解析JSON响应
    
    # 提示 (Hints):
    # curl -s https://api.github.com/users/github | jq '.name'
    # curl -I https://www.example.com  # 获取HTTP头
    # curl -o output.html https://www.example.com
    #
    # nc -zv localhost 80  # 测试端口是否开放
    
    :
}

# 练习7: 日志处理和分析
# Exercise 7: Log Processing and Analysis
exercise_07_log_analysis() {
    echo -e "\n=== 练习7: 日志处理和分析 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 解析日志文件
    # 2. 统计错误类型和数量
    # 3. 提取特定时间范围的日志
    # 4. 生成日志摘要报告
    
    # 提示 (Hints):
    # grep "ERROR" application.log | cut -d' ' -f3 | sort | uniq -c | sort -rn
    #
    # awk '/2025-01-15/,/2025-01-16/' application.log
    #
    # awk '/ERROR/ {errors++} /WARN/ {warnings++} END {
    #     print "错误:", errors
    #     print "警告:", warnings
    # }' application.log
    
    :
}

# 练习8: 数据库操作
# Exercise 8: Database Operations
exercise_08_database() {
    echo -e "\n=== 练习8: 数据库操作 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用sqlite3命令行工具
    # 2. 执行SQL查询并处理结果
    # 3. 导入和导出数据
    # 4. 批量处理查询结果
    
    # 提示 (Hints):
    # sqlite3 test.db "CREATE TABLE users (id INTEGER, name TEXT);"
    # sqlite3 test.db "INSERT INTO users VALUES (1, '张三');"
    # sqlite3 test.db "SELECT * FROM users;" | while IFS='|' read id name; do
    #     echo "ID: $id, 姓名: $name"
    # done
    #
    # sqlite3 -csv test.db "SELECT * FROM users;" > users.csv
    
    :
}

# 练习9: 复杂的文件操作
# Exercise 9: Complex File Operations
exercise_09_complex_file_ops() {
    echo -e "\n=== 练习9: 复杂的文件操作 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 批量重命名文件
    # 2. 递归处理目录树
    # 3. 文件去重
    # 4. 同步和备份文件
    
    # 提示 (Hints):
    # 批量重命名:
    # for file in *.txt; do
    #     mv "$file" "${file%.txt}.backup.txt"
    # done
    #
    # 递归处理:
    # find . -type f -name "*.log" -exec gzip {} \;
    #
    # 查找重复文件:
    # find . -type f -exec md5sum {} \; | sort | uniq -w32 -D
    #
    # rsync -av --delete source/ destination/
    
    :
}

# 练习10: 脚本模块化和重用
# Exercise 10: Script Modularity and Reusability
exercise_10_modularity() {
    echo -e "\n=== 练习10: 脚本模块化和重用 ==="
    
    # TODO: 在这里完成练习
    # 任务 (Tasks):
    # 1. 使用source加载外部脚本
    # 2. 创建函数库
    # 3. 使用配置文件
    # 4. 实现插件系统
    
    # 提示 (Hints):
    # 创建函数库 lib.sh:
    # log_info() { echo "[INFO] $*"; }
    # log_error() { echo "[ERROR] $*" >&2; }
    #
    # 在主脚本中:
    # source ./lib.sh
    # log_info "这是信息"
    #
    # 读取配置文件:
    # source config.conf
    # echo "数据库: $DB_HOST"
    #
    # 加载插件:
    # for plugin in plugins/*.sh; do
    #     [ -f "$plugin" ] && source "$plugin"
    # done
    
    :
}

###############################################################################
# 主函数 (Main Function)
###############################################################################

main() {
    echo "Shell 高级练习题"
    echo "================================================"
    echo
    
    # 运行所有练习
    exercise_01_pipelines
    exercise_02_advanced_regex
    exercise_03_debugging
    exercise_04_performance
    exercise_05_parallel
    exercise_06_network
    exercise_07_log_analysis
    exercise_08_database
    exercise_09_complex_file_ops
    exercise_10_modularity
    
    echo -e "\n所有练习完成！"
}

# 运行主函数
main "$@"
