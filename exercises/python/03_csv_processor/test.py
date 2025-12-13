#!/usr/bin/env python3
"""
测试脚本：验证 csv_processor.py 的实现
"""

import os
import sys
import csv
import subprocess
import tempfile

GREEN = '\033[0;32m'
RED = '\033[0;31m'
NC = '\033[0m'

PASS = 0
FAIL = 0

def create_test_csv(filepath):
    """创建测试CSV文件"""
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['日期', '产品', '数量', '单价'])
        writer.writerow(['2025-01-01', '苹果', '10', '5.0'])
        writer.writerow(['2025-01-01', '香蕉', '15', '3.0'])
        writer.writerow(['2025-01-02', '苹果', '8', '5.0'])
        writer.writerow(['2025-01-02', '橙子', '12', '4.0'])
        writer.writerow(['2025-01-03', '香蕉', '20', '3.0'])

def test_csv_processor():
    """测试CSV处理功能"""
    global PASS, FAIL
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # 创建测试CSV
        test_csv = os.path.join(tmpdir, 'test_sales.csv')
        create_test_csv(test_csv)
        
        # 切换到临时目录运行脚本
        original_dir = os.getcwd()
        os.chdir(tmpdir)
        
        try:
            # 运行处理脚本
            result = subprocess.run(
                ['python3', os.path.join(original_dir, 'csv_processor.py'), 
                 'test_sales.csv'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            output = result.stdout
            
            # 测试1: 检查输出包含销售统计
            if '销售统计报告' in output:
                print(f"{GREEN}✓ PASS{NC}: 输出包含销售统计报告")
                PASS += 1
            else:
                print(f"{RED}✗ FAIL{NC}: 输出不包含销售统计报告")
                FAIL += 1
            
            # 测试2: 检查是否包含产品信息
            if '苹果' in output and '香蕉' in output:
                print(f"{GREEN}✓ PASS{NC}: 输出包含产品信息")
                PASS += 1
            else:
                print(f"{RED}✗ FAIL{NC}: 输出缺少产品信息")
                FAIL += 1
            
            # 测试3: 检查是否生成报告文件
            if os.path.exists('sales_report.csv'):
                print(f"{GREEN}✓ PASS{NC}: 成功生成报告CSV文件")
                PASS += 1
                
                # 验证报告内容
                with open('sales_report.csv', 'r', encoding='utf-8') as f:
                    content = f.read()
                    if '苹果' in content or '香蕉' in content:
                        print(f"{GREEN}✓ PASS{NC}: 报告文件包含正确内容")
                        PASS += 1
                    else:
                        print(f"{RED}✗ FAIL{NC}: 报告文件内容不正确")
                        FAIL += 1
            else:
                print(f"{RED}✗ FAIL{NC}: 未生成报告CSV文件")
                FAIL += 2
                
        except Exception as e:
            print(f"{RED}✗ FAIL{NC}: 运行出错 - {str(e)}")
            FAIL += 1
        finally:
            os.chdir(original_dir)

def main():
    global PASS, FAIL
    
    if not os.path.exists('csv_processor.py'):
        print(f"{RED}错误: csv_processor.py 文件不存在{NC}")
        sys.exit(1)
    
    print("开始测试 csv_processor.py...")
    print()
    
    test_csv_processor()
    
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
