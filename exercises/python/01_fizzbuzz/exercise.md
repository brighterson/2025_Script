# 练习题 1: FizzBuzz

**难度**: ⭐

## 题目描述

编写一个Python脚本，实现经典的FizzBuzz问题：

1. 接受一个命令行参数N（正整数）
2. 从1到N，对于每个数字：
   - 如果能被3和5整除，输出 "FizzBuzz"
   - 如果能被3整除，输出 "Fizz"
   - 如果能被5整除，输出 "Buzz"
   - 否则输出数字本身
3. 每个结果占一行

## 示例

```bash
$ python fizzbuzz.py 15
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## 要求

- 脚本名称：`fizzbuzz.py`
- 使用 `sys.argv` 获取命令行参数
- 适当处理错误输入（如非数字、负数等）

## 提示

- 使用 `%` 运算符检查整除
- 注意判断顺序：先判断能否同时被3和5整除
- 使用 `try-except` 处理异常
