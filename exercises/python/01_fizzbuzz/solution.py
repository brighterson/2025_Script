#!/usr/bin/env python3
"""
练习题 1: FizzBuzz 参考答案
"""

import sys

def fizzbuzz(n):
    """生成1到n的FizzBuzz序列"""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    # 检查参数数量
    if len(sys.argv) != 2:
        print("用法: python fizzbuzz.py <正整数>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n <= 0:
            print("错误: 请输入正整数")
            sys.exit(1)
        
        fizzbuzz(n)
    except ValueError:
        print("错误: 参数必须是整数")
        sys.exit(1)

if __name__ == "__main__":
    main()
