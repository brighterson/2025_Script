#!/usr/bin/env python3
"""
测试脚本：验证 weather_cli.py 的实现
"""

import os
import sys
import subprocess
import json

GREEN = '\033[0;32m'
RED = '\033[0;31m'
NC = '\033[0m'

PASS = 0
FAIL = 0

def cleanup():
    """清理测试文件"""
    if os.path.exists('.weather_history.json'):
        os.remove('.weather_history.json')

def test_query_command():
    """测试query命令"""
    global PASS, FAIL
    
    result = subprocess.run(
        ['python3', 'weather_cli.py', 'query', '北京'],
        capture_output=True,
        text=True,
        timeout=5
    )
    
    output = result.stdout
    
    if '北京' in output and '温度' in output and '天气' in output:
        print(f"{GREEN}✓ PASS{NC}: query命令正常工作")
        PASS += 1
    else:
        print(f"{RED}✗ FAIL{NC}: query命令输出不正确")
        print(f"  输出: {output}")
        FAIL += 1

def test_history_saving():
    """测试历史记录保存"""
    global PASS, FAIL
    
    # 执行几次查询
    subprocess.run(['python3', 'weather_cli.py', 'query', '上海'],
                  capture_output=True, timeout=5)
    
    # 检查历史文件是否创建
    if os.path.exists('.weather_history.json'):
        print(f"{GREEN}✓ PASS{NC}: 历史记录文件已创建")
        PASS += 1
        
        # 验证历史文件内容
        try:
            with open('.weather_history.json', 'r', encoding='utf-8') as f:
                history = json.load(f)
            
            if len(history) > 0 and 'city' in history[0]:
                print(f"{GREEN}✓ PASS{NC}: 历史记录格式正确")
                PASS += 1
            else:
                print(f"{RED}✗ FAIL{NC}: 历史记录格式不正确")
                FAIL += 1
        except:
            print(f"{RED}✗ FAIL{NC}: 历史记录文件格式错误")
            FAIL += 1
    else:
        print(f"{RED}✗ FAIL{NC}: 历史记录文件未创建")
        FAIL += 2

def test_history_command():
    """测试history命令"""
    global PASS, FAIL
    
    result = subprocess.run(
        ['python3', 'weather_cli.py', 'history'],
        capture_output=True,
        text=True,
        timeout=5
    )
    
    output = result.stdout
    
    if '查询历史' in output or '历史' in output:
        print(f"{GREEN}✓ PASS{NC}: history命令正常工作")
        PASS += 1
    else:
        print(f"{RED}✗ FAIL{NC}: history命令输出不正确")
        FAIL += 1

def test_clear_command():
    """测试clear命令"""
    global PASS, FAIL
    
    result = subprocess.run(
        ['python3', 'weather_cli.py', 'clear'],
        capture_output=True,
        text=True,
        timeout=5
    )
    
    if not os.path.exists('.weather_history.json'):
        print(f"{GREEN}✓ PASS{NC}: clear命令成功清除历史")
        PASS += 1
    else:
        print(f"{RED}✗ FAIL{NC}: clear命令未清除历史文件")
        FAIL += 1

def main():
    global PASS, FAIL
    
    if not os.path.exists('weather_cli.py'):
        print(f"{RED}错误: weather_cli.py 文件不存在{NC}")
        sys.exit(1)
    
    print("开始测试 weather_cli.py...")
    print()
    
    try:
        cleanup()  # 清理旧的测试数据
        
        test_query_command()
        test_history_saving()
        test_history_command()
        test_clear_command()
        
    finally:
        cleanup()  # 清理测试数据
    
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
