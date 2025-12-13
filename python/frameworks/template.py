#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本模板 - Python Script Template

这是一个Python脚本的标准模板，包含了最佳实践和常用结构
This is a standard Python script template with best practices and common structures

作者 (Author): Your Name
日期 (Date): 2025
"""

import sys
import os
import argparse
import logging


def setup_logging(log_level=logging.INFO):
    """
    配置日志系统
    Setup logging configuration
    
    Args:
        log_level: 日志级别 (Logging level)
    """
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def parse_arguments():
    """
    解析命令行参数
    Parse command line arguments
    
    Returns:
        argparse.Namespace: 解析后的参数对象 (Parsed arguments)
    """
    parser = argparse.ArgumentParser(
        description='Python脚本模板 (Python Script Template)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例用法 (Example Usage):
  %(prog)s --input input.txt --output output.txt
  %(prog)s -i input.txt -o output.txt --verbose
        '''
    )
    
    parser.add_argument(
        '-i', '--input',
        type=str,
        required=False,
        help='输入文件路径 (Input file path)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=False,
        help='输出文件路径 (Output file path)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='详细输出模式 (Verbose output mode)'
    )
    
    return parser.parse_args()


def main():
    """
    主函数
    Main function
    """
    # 解析参数 (Parse arguments)
    args = parse_arguments()
    
    # 设置日志 (Setup logging)
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    logger = logging.getLogger(__name__)
    
    logger.info("脚本开始执行 (Script started)")
    
    try:
        # 在此处添加你的核心逻辑
        # Add your core logic here
        
        if args.input:
            logger.info(f"处理输入文件: {args.input}")
            # 处理输入文件 (Process input file)
            
        if args.output:
            logger.info(f"输出文件: {args.output}")
            # 写入输出文件 (Write output file)
        
        logger.info("脚本执行成功 (Script completed successfully)")
        return 0
        
    except Exception as e:
        logger.error(f"执行出错: {str(e)}")
        if args.verbose:
            logger.exception("详细错误信息:")
        return 1


if __name__ == '__main__':
    sys.exit(main())
