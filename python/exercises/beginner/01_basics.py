#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 初级练习题 - Python Beginner Exercises

这些练习涵盖了Python的基础知识，包括变量、数据类型、控制流和函数
These exercises cover Python basics including variables, data types, control flow, and functions

作者 (Author): Your Name
日期 (Date): 2025
"""


def exercise_01_variables():
    """
    练习1: 变量和数据类型
    Exercise 1: Variables and Data Types
    
    任务 (Tasks):
    1. 创建不同类型的变量：整数、浮点数、字符串、布尔值
    2. 打印变量类型
    3. 进行基本的数学运算
    """
    print("=== 练习1: 变量和数据类型 ===")
    
    # TODO: 在这里完成练习
    # 示例 (Example):
    # age = 25
    # name = "张三"
    # height = 1.75
    # is_student = True
    
    pass


def exercise_02_strings():
    """
    练习2: 字符串操作
    Exercise 2: String Operations
    
    任务 (Tasks):
    1. 创建一个字符串并获取其长度
    2. 字符串大小写转换
    3. 字符串分割和拼接
    4. 字符串格式化（使用f-string）
    """
    print("\n=== 练习2: 字符串操作 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints): 
    # text = "Hello World"
    # length = len(text)
    # upper_text = text.upper()
    # formatted = f"文本是: {text}"
    
    pass


def exercise_03_lists():
    """
    练习3: 列表操作
    Exercise 3: List Operations
    
    任务 (Tasks):
    1. 创建一个包含5个元素的列表
    2. 添加和删除元素
    3. 访问列表元素（正索引和负索引）
    4. 列表切片
    5. 使用列表方法：sort(), reverse(), append(), extend()
    """
    print("\n=== 练习3: 列表操作 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # numbers = [1, 2, 3, 4, 5]
    # numbers.append(6)
    # first = numbers[0]
    # last = numbers[-1]
    # slice_list = numbers[1:4]
    
    pass


def exercise_04_dictionaries():
    """
    练习4: 字典操作
    Exercise 4: Dictionary Operations
    
    任务 (Tasks):
    1. 创建一个字典存储学生信息（姓名、年龄、成绩）
    2. 访问字典值
    3. 添加和修改键值对
    4. 遍历字典的键、值和键值对
    5. 使用get()方法安全访问
    """
    print("\n=== 练习4: 字典操作 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # student = {
    #     "name": "张三",
    #     "age": 20,
    #     "grade": 95
    # }
    # name = student.get("name", "未知")
    
    pass


def exercise_05_conditionals():
    """
    练习5: 条件语句
    Exercise 5: Conditional Statements
    
    任务 (Tasks):
    1. 使用if-elif-else判断一个数字是正数、负数还是零
    2. 判断一个年份是否是闰年
    3. 根据分数判断等级（A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: <60）
    """
    print("\n=== 练习5: 条件语句 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # number = 10
    # if number > 0:
    #     print("正数")
    # elif number < 0:
    #     print("负数")
    # else:
    #     print("零")
    
    pass


def exercise_06_loops():
    """
    练习6: 循环
    Exercise 6: Loops
    
    任务 (Tasks):
    1. 使用for循环打印1到10
    2. 使用while循环计算1到100的和
    3. 遍历列表并打印每个元素
    4. 使用break和continue
    5. 使用enumerate()和zip()
    """
    print("\n=== 练习6: 循环 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # for i in range(1, 11):
    #     print(i)
    #
    # total = 0
    # i = 1
    # while i <= 100:
    #     total += i
    #     i += 1
    
    pass


def exercise_07_functions():
    """
    练习7: 函数
    Exercise 7: Functions
    
    任务 (Tasks):
    1. 创建一个计算两个数之和的函数
    2. 创建一个判断是否为质数的函数
    3. 创建一个带默认参数的函数
    4. 创建一个返回多个值的函数
    5. 使用*args和**kwargs
    """
    print("\n=== 练习7: 函数 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # def add(a, b):
    #     return a + b
    #
    # def is_prime(n):
    #     if n < 2:
    #         return False
    #     for i in range(2, int(n ** 0.5) + 1):
    #         if n % i == 0:
    #             return False
    #     return True
    
    pass


def exercise_08_list_comprehension():
    """
    练习8: 列表推导式
    Exercise 8: List Comprehension
    
    任务 (Tasks):
    1. 创建一个包含1到10平方数的列表
    2. 从列表中筛选出偶数
    3. 将字符串列表转换为大写
    4. 创建字典推导式
    """
    print("\n=== 练习8: 列表推导式 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # squares = [x**2 for x in range(1, 11)]
    # evens = [x for x in range(1, 21) if x % 2 == 0]
    # upper_words = [word.upper() for word in ["hello", "world"]]
    
    pass


def exercise_09_basic_io():
    """
    练习9: 基本输入输出
    Exercise 9: Basic Input/Output
    
    任务 (Tasks):
    1. 从用户获取输入
    2. 将输入转换为适当的类型
    3. 格式化输出
    """
    print("\n=== 练习9: 基本输入输出 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # name = input("请输入你的名字: ")
    # age = int(input("请输入你的年龄: "))
    # print(f"你好 {name}，你今年 {age} 岁")
    
    # 注意：在自动化测试中，input()可能不适用
    # 可以使用硬编码的值进行测试
    
    pass


def exercise_10_error_handling():
    """
    练习10: 基本错误处理
    Exercise 10: Basic Error Handling
    
    任务 (Tasks):
    1. 使用try-except捕获除零错误
    2. 捕获类型转换错误
    3. 使用finally块
    """
    print("\n=== 练习10: 基本错误处理 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # try:
    #     result = 10 / 0
    # except ZeroDivisionError:
    #     print("不能除以零")
    # finally:
    #     print("执行完成")
    
    pass


def main():
    """运行所有练习 (Run all exercises)"""
    print("Python 初级练习题\n" + "=" * 50 + "\n")
    
    exercises = [
        exercise_01_variables,
        exercise_02_strings,
        exercise_03_lists,
        exercise_04_dictionaries,
        exercise_05_conditionals,
        exercise_06_loops,
        exercise_07_functions,
        exercise_08_list_comprehension,
        exercise_09_basic_io,
        exercise_10_error_handling
    ]
    
    for exercise in exercises:
        try:
            exercise()
        except Exception as e:
            print(f"练习 {exercise.__name__} 出错: {e}")
        print()


if __name__ == '__main__':
    main()
