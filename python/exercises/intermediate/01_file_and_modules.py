#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 中级练习题 - Python Intermediate Exercises

这些练习涵盖了文件处理、模块、正则表达式和更高级的数据结构
These exercises cover file handling, modules, regex, and advanced data structures

作者 (Author): Your Name
日期 (Date): 2025
"""

import os
import json
import re
from datetime import datetime
from collections import defaultdict, Counter


def exercise_01_file_reading():
    """
    练习1: 文件读取
    Exercise 1: File Reading
    
    任务 (Tasks):
    1. 读取文本文件的全部内容
    2. 逐行读取文件
    3. 使用with语句确保文件正确关闭
    4. 处理文件不存在的情况
    """
    print("=== 练习1: 文件读取 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # try:
    #     with open('example.txt', 'r', encoding='utf-8') as f:
    #         content = f.read()
    #         print(content)
    # except FileNotFoundError:
    #     print("文件不存在")
    
    pass


def exercise_02_file_writing():
    """
    练习2: 文件写入
    Exercise 2: File Writing
    
    任务 (Tasks):
    1. 创建并写入新文件
    2. 追加内容到现有文件
    3. 写入多行内容
    4. 创建临时文件用于测试
    """
    print("\n=== 练习2: 文件写入 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # with open('output.txt', 'w', encoding='utf-8') as f:
    #     f.write("第一行\n")
    #     f.write("第二行\n")
    #
    # with open('output.txt', 'a', encoding='utf-8') as f:
    #     f.write("追加的行\n")
    
    pass


def exercise_03_json_handling():
    """
    练习3: JSON处理
    Exercise 3: JSON Handling
    
    任务 (Tasks):
    1. 将Python字典转换为JSON字符串
    2. 将JSON字符串解析为Python对象
    3. 读取和写入JSON文件
    4. 格式化JSON输出
    """
    print("\n=== 练习3: JSON处理 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # data = {"name": "张三", "age": 25, "city": "北京"}
    # json_str = json.dumps(data, ensure_ascii=False, indent=2)
    # parsed_data = json.loads(json_str)
    #
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=2)
    
    pass


def exercise_04_regular_expressions():
    """
    练习4: 正则表达式
    Exercise 4: Regular Expressions
    
    任务 (Tasks):
    1. 验证邮箱格式
    2. 提取文本中的所有数字
    3. 替换文本中的特定模式
    4. 使用分组提取信息
    """
    print("\n=== 练习4: 正则表达式 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # email = "test@example.com"
    # if re.match(email_pattern, email):
    #     print("有效的邮箱")
    #
    # text = "我有100个苹果和50个橙子"
    # numbers = re.findall(r'\d+', text)
    
    pass


def exercise_05_exception_handling():
    """
    练习5: 异常处理
    Exercise 5: Exception Handling
    
    任务 (Tasks):
    1. 创建自定义异常类
    2. 使用多个except块
    3. 使用else和finally
    4. 重新抛出异常
    """
    print("\n=== 练习5: 异常处理 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # class CustomError(Exception):
    #     pass
    #
    # try:
    #     value = int("abc")
    # except ValueError as e:
    #     print(f"值错误: {e}")
    # except Exception as e:
    #     print(f"其他错误: {e}")
    # else:
    #     print("没有异常")
    # finally:
    #     print("总是执行")
    
    pass


def exercise_06_lambda_functions():
    """
    练习6: Lambda函数和内置函数
    Exercise 6: Lambda Functions and Built-in Functions
    
    任务 (Tasks):
    1. 使用lambda创建简单函数
    2. 使用map()、filter()、reduce()
    3. 使用sorted()和自定义排序键
    4. 使用all()和any()
    """
    print("\n=== 练习6: Lambda函数和内置函数 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # square = lambda x: x ** 2
    # numbers = [1, 2, 3, 4, 5]
    # squared = list(map(square, numbers))
    # evens = list(filter(lambda x: x % 2 == 0, numbers))
    #
    # from functools import reduce
    # sum_all = reduce(lambda x, y: x + y, numbers)
    
    pass


def exercise_07_collections():
    """
    练习7: 集合数据结构
    Exercise 7: Collection Data Structures
    
    任务 (Tasks):
    1. 使用set进行集合操作（并集、交集、差集）
    2. 使用defaultdict
    3. 使用Counter统计元素
    4. 使用namedtuple
    """
    print("\n=== 练习7: 集合数据结构 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # set1 = {1, 2, 3, 4, 5}
    # set2 = {4, 5, 6, 7, 8}
    # union = set1 | set2
    # intersection = set1 & set2
    # difference = set1 - set2
    #
    # dd = defaultdict(list)
    # dd['key'].append('value')
    #
    # words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    # counter = Counter(words)
    
    pass


def exercise_08_datetime_handling():
    """
    练习8: 日期时间处理
    Exercise 8: DateTime Handling
    
    任务 (Tasks):
    1. 获取当前日期和时间
    2. 格式化日期时间
    3. 解析日期字符串
    4. 日期时间计算（加减）
    """
    print("\n=== 练习8: 日期时间处理 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # now = datetime.now()
    # formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    # parsed = datetime.strptime("2025-01-01", "%Y-%m-%d")
    #
    # from datetime import timedelta
    # tomorrow = now + timedelta(days=1)
    
    pass


def exercise_09_generators():
    """
    练习9: 生成器
    Exercise 9: Generators
    
    任务 (Tasks):
    1. 创建生成器函数
    2. 使用生成器表达式
    3. 实现斐波那契数列生成器
    4. 理解yield的使用
    """
    print("\n=== 练习9: 生成器 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # def number_generator(n):
    #     for i in range(n):
    #         yield i
    #
    # gen = (x**2 for x in range(10))
    #
    # def fibonacci(n):
    #     a, b = 0, 1
    #     for _ in range(n):
    #         yield a
    #         a, b = b, a + b
    
    pass


def exercise_10_path_operations():
    """
    练习10: 路径操作
    Exercise 10: Path Operations
    
    任务 (Tasks):
    1. 使用os.path进行路径操作
    2. 检查文件/目录是否存在
    3. 获取文件信息（大小、修改时间）
    4. 列出目录内容
    """
    print("\n=== 练习10: 路径操作 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # current_dir = os.getcwd()
    # file_path = os.path.join(current_dir, 'example.txt')
    # exists = os.path.exists(file_path)
    # is_file = os.path.isfile(file_path)
    # is_dir = os.path.isdir(current_dir)
    #
    # if exists:
    #     size = os.path.getsize(file_path)
    #     mtime = os.path.getmtime(file_path)
    
    pass


def main():
    """运行所有练习 (Run all exercises)"""
    print("Python 中级练习题\n" + "=" * 50 + "\n")
    
    exercises = [
        exercise_01_file_reading,
        exercise_02_file_writing,
        exercise_03_json_handling,
        exercise_04_regular_expressions,
        exercise_05_exception_handling,
        exercise_06_lambda_functions,
        exercise_07_collections,
        exercise_08_datetime_handling,
        exercise_09_generators,
        exercise_10_path_operations
    ]
    
    for exercise in exercises:
        try:
            exercise()
        except Exception as e:
            print(f"练习 {exercise.__name__} 出错: {e}")
        print()


if __name__ == '__main__':
    main()
