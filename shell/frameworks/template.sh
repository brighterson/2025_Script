#!/bin/bash
# -*- coding: utf-8 -*-

###############################################################################
# Shell 脚本模板 - Shell Script Template
#
# 这是一个Shell脚本的标准模板，包含了最佳实践和常用结构
# This is a standard Shell script template with best practices and common structures
#
# 作者 (Author): Your Name
# 日期 (Date): 2025
###############################################################################

# 严格模式 (Strict mode)
set -euo pipefail
IFS=$'\n\t'

###############################################################################
# 全局变量 (Global Variables)
###############################################################################

# 脚本信息 (Script information)
readonly SCRIPT_NAME=$(basename "$0")
readonly SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
readonly VERSION="1.0.0"

# 颜色定义 (Color definitions)
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[0;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m' # No Color

# 默认值 (Default values)
INPUT_FILE=""
OUTPUT_FILE=""
VERBOSE=0

###############################################################################
# 函数定义 (Function Definitions)
###############################################################################

# 打印使用说明
# Print usage information
usage() {
    cat << EOF
使用方法 (Usage): $SCRIPT_NAME [选项] (options)

选项 (Options):
    -h, --help              显示此帮助信息 (Show this help message)
    -v, --version           显示版本信息 (Show version information)
    -i, --input FILE        输入文件 (Input file)
    -o, --output FILE       输出文件 (Output file)
    --verbose               详细输出模式 (Verbose output mode)

示例 (Examples):
    $SCRIPT_NAME -i input.txt -o output.txt
    $SCRIPT_NAME --input input.txt --output output.txt --verbose

EOF
}

# 打印版本信息
# Print version information
version() {
    echo "$SCRIPT_NAME version $VERSION"
}

# 日志函数 (Logging functions)
log_info() {
    echo -e "${GREEN}[INFO]${NC} $*"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $*" >&2
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $*" >&2
}

log_debug() {
    if [ "$VERBOSE" -eq 1 ]; then
        echo -e "${BLUE}[DEBUG]${NC} $*"
    fi
}

# 错误处理函数
# Error handling function
error_exit() {
    log_error "$1"
    exit "${2:-1}"
}

# 检查依赖
# Check dependencies
check_dependencies() {
    local deps=("$@")
    for cmd in "${deps[@]}"; do
        if ! command -v "$cmd" &> /dev/null; then
            error_exit "需要的命令未找到: $cmd (Required command not found: $cmd)"
        fi
    done
}

# 检查文件是否存在
# Check if file exists
check_file_exists() {
    local file="$1"
    if [ ! -f "$file" ]; then
        error_exit "文件不存在: $file (File does not exist: $file)"
    fi
}

# 创建备份
# Create backup
backup_file() {
    local file="$1"
    if [ -f "$file" ]; then
        local backup="${file}.backup.$(date +%Y%m%d_%H%M%S)"
        cp "$file" "$backup"
        log_info "已创建备份: $backup (Backup created: $backup)"
    fi
}

# 清理函数 (在脚本退出时执行)
# Cleanup function (executed on script exit)
cleanup() {
    log_debug "执行清理操作... (Performing cleanup...)"
    # 在此处添加清理代码
    # Add cleanup code here
}

# 注册清理函数
trap cleanup EXIT

###############################################################################
# 参数解析 (Argument Parsing)
###############################################################################

parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                exit 0
                ;;
            -v|--version)
                version
                exit 0
                ;;
            -i|--input)
                if [[ -z "${2:-}" ]]; then
                    error_exit "选项 $1 需要参数 (Option $1 requires an argument)" 1
                fi
                INPUT_FILE="$2"
                shift 2
                ;;
            -o|--output)
                if [[ -z "${2:-}" ]]; then
                    error_exit "选项 $1 需要参数 (Option $1 requires an argument)" 1
                fi
                OUTPUT_FILE="$2"
                shift 2
                ;;
            --verbose)
                VERBOSE=1
                shift
                ;;
            *)
                error_exit "未知选项: $1 (Unknown option: $1)" 1
                ;;
        esac
    done
}

###############################################################################
# 核心功能函数 (Core Functionality Functions)
###############################################################################

# 主要处理函数
# Main processing function
process_data() {
    log_info "开始处理数据... (Starting data processing...)"
    
    # 在此处添加你的核心逻辑
    # Add your core logic here
    
    if [ -n "$INPUT_FILE" ]; then
        log_debug "处理输入文件: $INPUT_FILE (Processing input file: $INPUT_FILE)"
        check_file_exists "$INPUT_FILE"
        # 处理输入文件 (Process input file)
    fi
    
    if [ -n "$OUTPUT_FILE" ]; then
        log_debug "输出文件: $OUTPUT_FILE (Output file: $OUTPUT_FILE)"
        # 写入输出文件 (Write to output file)
    fi
    
    log_info "数据处理完成 (Data processing completed)"
}

###############################################################################
# 主函数 (Main Function)
###############################################################################

main() {
    log_info "脚本开始执行: $SCRIPT_NAME (Script started: $SCRIPT_NAME)"
    log_debug "脚本目录: $SCRIPT_DIR (Script directory: $SCRIPT_DIR)"
    
    # 解析命令行参数
    # Parse command line arguments
    parse_arguments "$@"
    
    # 检查必要的依赖
    # Check required dependencies
    # check_dependencies "awk" "sed" "grep"
    
    # 执行主要处理
    # Execute main processing
    process_data
    
    log_info "脚本执行成功 (Script completed successfully)"
    exit 0
}

###############################################################################
# 脚本入口 (Script Entry Point)
###############################################################################

# 运行主函数
# Run main function
main "$@"
