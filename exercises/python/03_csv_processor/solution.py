#!/usr/bin/env python3
"""
练习题 3: CSV数据处理器 参考答案
"""

import csv
import sys
from collections import defaultdict

def process_sales_data(input_file):
    """处理销售数据CSV文件"""
    # 检查文件是否存在
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # 统计每个产品的销售额
            product_sales = defaultdict(float)
            
            for row in reader:
                try:
                    product = row['产品']
                    quantity = float(row['数量'])
                    price = float(row['单价'])
                    sales = quantity * price
                    product_sales[product] += sales
                except (KeyError, ValueError) as e:
                    print(f"警告: 跳过无效数据行 - {e}")
                    continue
            
            return product_sales
    
    except FileNotFoundError:
        print(f"错误: 文件 '{input_file}' 不存在")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 读取文件时出错 - {e}")
        sys.exit(1)

def generate_report(product_sales, output_file='sales_report.csv'):
    """生成销售报告"""
    # 按销售额排序
    sorted_products = sorted(product_sales.items(), 
                            key=lambda x: x[1], 
                            reverse=True)
    
    # 计算总销售额
    total_sales = sum(product_sales.values())
    
    # 输出到控制台
    print("\n销售统计报告")
    print("=================================")
    print("产品销售排行:")
    for i, (product, sales) in enumerate(sorted_products, 1):
        print(f"  {i}. {product}: ¥{sales:.2f}")
    
    print(f"\n总销售额: ¥{total_sales:.2f}")
    
    # 保存到CSV文件
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['排名', '产品', '销售额'])
            
            for i, (product, sales) in enumerate(sorted_products, 1):
                writer.writerow([i, product, f'{sales:.2f}'])
            
            writer.writerow([])
            writer.writerow(['总销售额', '', f'{total_sales:.2f}'])
        
        print(f"\n统计结果已保存到: {output_file}")
    
    except Exception as e:
        print(f"错误: 保存报告时出错 - {e}")

def main():
    if len(sys.argv) != 2:
        print("用法: python csv_processor.py <CSV文件路径>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # 处理数据
    product_sales = process_sales_data(input_file)
    
    if not product_sales:
        print("警告: 没有找到有效的销售数据")
        return
    
    # 生成报告
    generate_report(product_sales)

if __name__ == "__main__":
    main()
