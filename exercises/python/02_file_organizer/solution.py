#!/usr/bin/env python3
"""
练习题 2: 文件整理工具 参考答案
"""

import os
import sys
import shutil
from collections import defaultdict

# 文件类型映射
FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.md', '.xlsx', '.pptx'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
}

def get_file_category(filename):
    """根据文件扩展名确定类别"""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    
    return 'others'

def organize_files(directory):
    """整理指定目录中的文件"""
    if not os.path.isdir(directory):
        print(f"错误: '{directory}' 不是有效的目录")
        return
    
    print("开始整理文件...\n")
    
    # 统计计数器
    stats = defaultdict(int)
    
    # 遍历目录中的所有文件
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # 跳过目录
        if not os.path.isfile(item_path):
            continue
        
        # 确定文件类别
        category = get_file_category(item)
        
        # 创建目标目录
        target_dir = os.path.join(directory, category)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"创建目录: {target_dir}")
        
        # 移动文件
        target_path = os.path.join(target_dir, item)
        try:
            shutil.move(item_path, target_path)
            print(f"  {item} → {category}/")
            stats[category] += 1
        except Exception as e:
            print(f"错误: 无法移动 {item}: {e}")
    
    # 输出统计
    print("\n整理完成！")
    for category in sorted(stats.keys()):
        print(f"  {category}: {stats[category]} 个")

def main():
    if len(sys.argv) != 2:
        print("用法: python file_organizer.py <目录路径>")
        sys.exit(1)
    
    directory = sys.argv[1]
    organize_files(directory)

if __name__ == "__main__":
    main()
