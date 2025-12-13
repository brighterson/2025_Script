#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 高级练习题 - Python Advanced Exercises

这些练习涵盖了装饰器、元类、多线程、协程等高级主题
These exercises cover decorators, metaclasses, multithreading, coroutines, and other advanced topics

作者 (Author): Your Name
日期 (Date): 2025
"""

import time
import functools
from typing import Callable, Any
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio


def exercise_01_decorators():
    """
    练习1: 装饰器
    Exercise 1: Decorators
    
    任务 (Tasks):
    1. 创建一个计时装饰器
    2. 创建一个缓存装饰器
    3. 创建带参数的装饰器
    4. 使用functools.wraps保持元数据
    """
    print("=== 练习1: 装饰器 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # def timer(func):
    #     @functools.wraps(func)
    #     def wrapper(*args, **kwargs):
    #         start = time.time()
    #         result = func(*args, **kwargs)
    #         end = time.time()
    #         print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
    #         return result
    #     return wrapper
    #
    # @timer
    # def slow_function():
    #     time.sleep(1)
    
    pass


def exercise_02_context_managers():
    """
    练习2: 上下文管理器
    Exercise 2: Context Managers
    
    任务 (Tasks):
    1. 使用__enter__和__exit__创建上下文管理器
    2. 使用contextlib.contextmanager创建上下文管理器
    3. 处理异常的上下文管理器
    4. 嵌套上下文管理器
    """
    print("\n=== 练习2: 上下文管理器 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # from contextlib import contextmanager
    #
    # @contextmanager
    # def timer_context(name):
    #     start = time.time()
    #     yield
    #     end = time.time()
    #     print(f"{name} 执行时间: {end - start:.4f}秒")
    #
    # with timer_context("操作"):
    #     time.sleep(0.5)
    
    pass


def exercise_03_generators_advanced():
    """
    练习3: 高级生成器
    Exercise 3: Advanced Generators
    
    任务 (Tasks):
    1. 使用send()向生成器发送值
    2. 使用throw()向生成器抛出异常
    3. 使用close()关闭生成器
    4. 创建生成器管道
    """
    print("\n=== 练习3: 高级生成器 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # def coroutine():
    #     print("启动协程")
    #     while True:
    #         value = yield
    #         print(f"接收到: {value}")
    #
    # coro = coroutine()
    # next(coro)  # 启动
    # coro.send(10)
    # coro.send(20)
    
    pass


def exercise_04_property_descriptor():
    """
    练习4: 属性和描述符
    Exercise 4: Properties and Descriptors
    
    任务 (Tasks):
    1. 使用@property创建只读属性
    2. 创建getter、setter和deleter
    3. 实现描述符协议
    4. 使用__getattr__和__setattr__
    """
    print("\n=== 练习4: 属性和描述符 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # class Temperature:
    #     def __init__(self, celsius):
    #         self._celsius = celsius
    #
    #     @property
    #     def celsius(self):
    #         return self._celsius
    #
    #     @celsius.setter
    #     def celsius(self, value):
    #         if value < -273.15:
    #             raise ValueError("温度不能低于绝对零度")
    #         self._celsius = value
    #
    #     @property
    #     def fahrenheit(self):
    #         return self._celsius * 9/5 + 32
    
    pass


def exercise_05_metaclasses():
    """
    练习5: 元类
    Exercise 5: Metaclasses
    
    任务 (Tasks):
    1. 理解type()作为元类
    2. 创建自定义元类
    3. 使用元类修改类创建过程
    4. 使用__init_subclass__
    """
    print("\n=== 练习5: 元类 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # class Meta(type):
    #     def __new__(mcs, name, bases, dct):
    #         print(f"创建类: {name}")
    #         return super().__new__(mcs, name, bases, dct)
    #
    # class MyClass(metaclass=Meta):
    #     pass
    
    pass


def exercise_06_multithreading():
    """
    练习6: 多线程
    Exercise 6: Multithreading
    
    任务 (Tasks):
    1. 使用threading创建线程
    2. 使用ThreadPoolExecutor
    3. 线程同步（Lock、RLock、Semaphore）
    4. 线程间通信（Queue）
    """
    print("\n=== 练习6: 多线程 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # import threading
    #
    # def worker(n):
    #     print(f"线程 {n} 开始")
    #     time.sleep(1)
    #     print(f"线程 {n} 完成")
    #     return n * 2
    #
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     futures = [executor.submit(worker, i) for i in range(5)]
    #     results = [f.result() for f in futures]
    
    pass


def exercise_07_multiprocessing():
    """
    练习7: 多进程
    Exercise 7: Multiprocessing
    
    任务 (Tasks):
    1. 使用ProcessPoolExecutor
    2. 进程间通信
    3. 理解GIL的影响
    4. CPU密集型任务的并行化
    """
    print("\n=== 练习7: 多进程 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # def cpu_intensive(n):
    #     return sum(i*i for i in range(n))
    #
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     results = list(executor.map(cpu_intensive, [1000000] * 4))
    
    pass


def exercise_08_async_await():
    """
    练习8: 异步编程
    Exercise 8: Async Programming
    
    任务 (Tasks):
    1. 使用async/await创建协程
    2. 使用asyncio.gather并发执行
    3. 使用asyncio.create_task
    4. 异步上下文管理器
    """
    print("\n=== 练习8: 异步编程 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # async def fetch_data(n):
    #     print(f"开始获取数据 {n}")
    #     await asyncio.sleep(1)
    #     print(f"完成获取数据 {n}")
    #     return n * 2
    #
    # async def main():
    #     results = await asyncio.gather(
    #         fetch_data(1),
    #         fetch_data(2),
    #         fetch_data(3)
    #     )
    #     print(results)
    #
    # asyncio.run(main())
    
    pass


def exercise_09_itertools():
    """
    练习9: itertools高级用法
    Exercise 9: Advanced itertools
    
    任务 (Tasks):
    1. 使用chain、zip_longest
    2. 使用groupby
    3. 使用permutations、combinations
    4. 使用cycle、repeat、count
    """
    print("\n=== 练习9: itertools高级用法 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # from itertools import chain, groupby, combinations, cycle
    #
    # list1 = [1, 2, 3]
    # list2 = [4, 5, 6]
    # chained = list(chain(list1, list2))
    #
    # data = [1, 1, 2, 2, 2, 3, 3]
    # for key, group in groupby(data):
    #     print(key, list(group))
    #
    # combs = list(combinations([1, 2, 3, 4], 2))
    
    pass


def exercise_10_memory_optimization():
    """
    练习10: 内存优化
    Exercise 10: Memory Optimization
    
    任务 (Tasks):
    1. 使用__slots__减少内存使用
    2. 使用weakref
    3. 使用sys.getsizeof()检查对象大小
    4. 生成器vs列表的内存对比
    """
    print("\n=== 练习10: 内存优化 ===")
    
    # TODO: 在这里完成练习
    # 提示 (Hints):
    # import sys
    #
    # class WithoutSlots:
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #
    # class WithSlots:
    #     __slots__ = ['x', 'y']
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #
    # obj1 = WithoutSlots(1, 2)
    # obj2 = WithSlots(1, 2)
    # print(f"Without slots: {sys.getsizeof(obj1.__dict__)} bytes")
    # print(f"With slots: {sys.getsizeof(obj2)} bytes")
    
    pass


def main():
    """运行所有练习 (Run all exercises)"""
    print("Python 高级练习题\n" + "=" * 50 + "\n")
    
    exercises = [
        exercise_01_decorators,
        exercise_02_context_managers,
        exercise_03_generators_advanced,
        exercise_04_property_descriptor,
        exercise_05_metaclasses,
        exercise_06_multithreading,
        exercise_07_multiprocessing,
        exercise_08_async_await,
        exercise_09_itertools,
        exercise_10_memory_optimization
    ]
    
    for exercise in exercises:
        try:
            exercise()
        except Exception as e:
            print(f"练习 {exercise.__name__} 出错: {e}")
        print()


if __name__ == '__main__':
    main()
