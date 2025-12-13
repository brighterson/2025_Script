#!/usr/bin/env python3
"""
测试脚本：验证 fizzbuzz.py 的实现
"""

import subprocess
import sys

# 颜色输出
GREEN = '\033[0;32m'
RED = '\033[0;31m'
NC = '\033[0m'

PASS = 0
FAIL = 0

def test_fizzbuzz(n, expected_lines, description):
    """测试FizzBuzz输出"""
    global PASS, FAIL
    
    try:
        result = subprocess.run(
            ['python3', 'fizzbuzz.py', str(n)],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        actual_lines = result.stdout.strip().split('\n')
        
        if actual_lines == expected_lines:
            print(f"{GREEN}✓ PASS{NC}: {description}")
            PASS += 1
        else:
            print(f"{RED}✗ FAIL{NC}: {description}")
            print(f"  Expected: {expected_lines[:5]}...")
            print(f"  Actual:   {actual_lines[:5]}...")
            FAIL += 1
    except Exception as e:
        print(f"{RED}✗ FAIL{NC}: {description} - {str(e)}")
        FAIL += 1

def main():
    global PASS, FAIL
    
    # 检查文件是否存在
    try:
        with open('fizzbuzz.py', 'r'):
            pass
    except FileNotFoundError:
        print(f"{RED}错误: fizzbuzz.py 文件不存在{NC}")
        sys.exit(1)
    
    print("开始测试 fizzbuzz.py...")
    print()
    
    # 测试用例1: N=15
    expected_15 = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 
                   'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    test_fizzbuzz(15, expected_15, "N=15的FizzBuzz序列")
    
    # 测试用例2: N=5
    expected_5 = ['1', '2', 'Fizz', '4', 'Buzz']
    test_fizzbuzz(5, expected_5, "N=5的FizzBuzz序列")
    
    # 测试用例3: N=3
    expected_3 = ['1', '2', 'Fizz']
    test_fizzbuzz(3, expected_3, "N=3的FizzBuzz序列")
    
    print()
    print("测试完成！")
    print(f"{GREEN}通过: {PASS}{NC}")
    print(f"{RED}失败: {FAIL}{NC}")
    
    if FAIL == 0:
        print(f"{GREEN}恭喜！所有测试通过！{NC}")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
