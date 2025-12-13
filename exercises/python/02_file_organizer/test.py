#!/usr/bin/env python3
"""
测试脚本：验证 file_organizer.py 的实现
"""

import os
import sys
import shutil
import subprocess
import tempfile

GREEN = '\033[0;32m'
RED = '\033[0;31m'
NC = '\033[0m'

PASS = 0
FAIL = 0

def test_file_organizer():
    """测试文件整理功能"""
    global PASS, FAIL
    
    # 创建临时测试目录
    with tempfile.TemporaryDirectory() as tmpdir:
        # 创建测试文件
        test_files = [
            'photo.jpg',
            'document.pdf',
            'music.mp3',
            'video.mp4',
            'readme.txt',
            'archive.zip',
            'unknown.xyz'
        ]
        
        for filename in test_files:
            filepath = os.path.join(tmpdir, filename)
            with open(filepath, 'w') as f:
                f.write('test content')
        
        # 运行整理脚本
        try:
            result = subprocess.run(
                ['python3', 'file_organizer.py', tmpdir],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            # 检查是否创建了分类目录
            expected_dirs = ['images', 'documents', 'audio', 'videos', 'archives', 'others']
            created_dirs = []
            
            for dirname in expected_dirs:
                dir_path = os.path.join(tmpdir, dirname)
                if os.path.exists(dir_path):
                    created_dirs.append(dirname)
            
            if len(created_dirs) >= 4:  # 至少创建了一些分类目录
                print(f"{GREEN}✓ PASS{NC}: 成功创建分类目录")
                PASS += 1
            else:
                print(f"{RED}✗ FAIL{NC}: 未创建足够的分类目录")
                print(f"  创建的目录: {created_dirs}")
                FAIL += 1
            
            # 检查文件是否被移动
            # 根目录不应该还有测试文件
            remaining_files = [f for f in os.listdir(tmpdir) 
                              if os.path.isfile(os.path.join(tmpdir, f))]
            
            if len(remaining_files) == 0:
                print(f"{GREEN}✓ PASS{NC}: 所有文件都被移动")
                PASS += 1
            else:
                print(f"{RED}✗ FAIL{NC}: 还有文件未被移动")
                print(f"  剩余文件: {remaining_files}")
                FAIL += 1
            
            # 检查特定文件是否在正确的目录
            if os.path.exists(os.path.join(tmpdir, 'images', 'photo.jpg')):
                print(f"{GREEN}✓ PASS{NC}: 图片文件正确分类")
                PASS += 1
            else:
                print(f"{RED}✗ FAIL{NC}: 图片文件未正确分类")
                FAIL += 1
                
        except Exception as e:
            print(f"{RED}✗ FAIL{NC}: 运行出错 - {str(e)}")
            FAIL += 1

def main():
    global PASS, FAIL
    
    # 检查文件是否存在
    if not os.path.exists('file_organizer.py'):
        print(f"{RED}错误: file_organizer.py 文件不存在{NC}")
        sys.exit(1)
    
    print("开始测试 file_organizer.py...")
    print()
    
    test_file_organizer()
    
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
