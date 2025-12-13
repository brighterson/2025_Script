# 练习题 3: 文件备份工具

**难度**: ⭐⭐

## 题目描述

编写一个Shell脚本，实现文件备份功能：

1. 接受一个文件路径作为参数
2. 创建该文件的备份，备份文件名格式为：原文件名.backup.YYYYMMDD_HHMMSS
3. 如果文件不存在，输出错误信息
4. 备份成功后，输出备份文件的路径

## 示例

```bash
$ ./backup.sh test.txt
备份成功: test.txt.backup.20250113_143025

$ ./backup.sh nonexistent.txt
错误: 文件 'nonexistent.txt' 不存在
```

## 要求

- 脚本名称：`backup.sh`
- 使用 `date` 命令生成时间戳
- 使用 `cp` 命令复制文件
- 检查文件是否存在

## 提示

- 使用 `date +%Y%m%d_%H%M%S` 生成时间戳
- 使用 `[ -f filename ]` 检查文件是否存在
- 使用 `$()` 捕获命令输出
