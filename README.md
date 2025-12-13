# 2025_Script

创建于2025年，用于学习脚本语言（Shell和Python）  
Created in 2025, to learn script languages like Shell and Python

## 📚 目录结构 (Directory Structure)

```
2025_Script/
├── python/                    # Python相关内容
│   ├── frameworks/           # Python框架和模板
│   │   ├── template.py      # 基础脚本模板
│   │   └── class_template.py # 面向对象编程模板
│   └── exercises/           # Python练习题
│       ├── beginner/        # 初级练习
│       ├── intermediate/    # 中级练习
│       └── advanced/        # 高级练习
├── shell/                    # Shell相关内容
│   ├── frameworks/          # Shell框架和模板
│   │   └── template.sh     # Shell脚本模板
│   └── exercises/          # Shell练习题
│       ├── beginner/       # 初级练习
│       ├── intermediate/   # 中级练习
│       └── advanced/       # 高级练习
└── README.md               # 本文件
```

## 🐍 Python 学习路径

### 框架模板 (Frameworks)

#### 1. 基础脚本模板 (`python/frameworks/template.py`)
- 命令行参数解析
- 日志系统配置
- 错误处理
- 标准项目结构

#### 2. 面向对象编程模板 (`python/frameworks/class_template.py`)
- 抽象基类和继承
- 属性和方法
- 上下文管理器
- 类型注解

### 练习题 (Exercises)

#### 初级 (Beginner) - `python/exercises/beginner/`
适合Python初学者，涵盖基础语法和概念：

1. **变量和数据类型** - 整数、浮点数、字符串、布尔值
2. **字符串操作** - 格式化、切片、方法
3. **列表操作** - 增删改查、切片、方法
4. **字典操作** - 键值对、遍历、方法
5. **条件语句** - if-elif-else、比较运算符
6. **循环** - for、while、break、continue
7. **函数** - 定义、参数、返回值
8. **列表推导式** - 简洁的列表创建
9. **基本输入输出** - input、print、格式化
10. **基本错误处理** - try-except-finally

#### 中级 (Intermediate) - `python/exercises/intermediate/`
适合有一定基础的学习者：

1. **文件读取** - 读取文本、处理异常
2. **文件写入** - 创建文件、追加内容
3. **JSON处理** - 序列化、反序列化
4. **正则表达式** - 模式匹配、提取、替换
5. **异常处理** - 自定义异常、多重捕获
6. **Lambda函数** - map、filter、reduce
7. **集合数据结构** - set、defaultdict、Counter
8. **日期时间处理** - 格式化、解析、计算
9. **生成器** - yield、生成器表达式
10. **路径操作** - os.path、文件信息

#### 高级 (Advanced) - `python/exercises/advanced/`
适合进阶学习者：

1. **装饰器** - 函数装饰器、类装饰器
2. **上下文管理器** - \_\_enter\_\_、\_\_exit\_\_
3. **高级生成器** - send、throw、close
4. **属性和描述符** - @property、描述符协议
5. **元类** - type、自定义元类
6. **多线程** - ThreadPoolExecutor、同步
7. **多进程** - ProcessPoolExecutor、并行
8. **异步编程** - async/await、asyncio
9. **itertools** - chain、groupby、combinations
10. **内存优化** - \_\_slots\_\_、weakref

## 🐚 Shell 学习路径

### 框架模板 (Frameworks)

#### Shell脚本模板 (`shell/frameworks/template.sh`)
- 参数解析
- 日志函数
- 错误处理
- 信号处理
- 最佳实践

### 练习题 (Exercises)

#### 初级 (Beginner) - `shell/exercises/beginner/`
适合Shell脚本初学者：

1. **变量和输出** - 变量定义、echo、命令替换
2. **字符串操作** - 连接、长度、切片、替换
3. **条件语句** - if-elif-else、测试运算符
4. **循环** - for、while、until
5. **数组** - 创建、访问、遍历
6. **函数** - 定义、参数、返回值
7. **算术运算** - 加减乘除、let、expr
8. **命令行参数** - $1、$2、$@、$#
9. **文件测试** - -f、-d、-r、-w、-x
10. **输入输出重定向** - >、>>、<、|、2>

#### 中级 (Intermediate) - `shell/exercises/intermediate/`
适合有一定基础的学习者：

1. **文件读取和处理** - while read、IFS
2. **文件写入和追加** - echo、cat、heredoc
3. **grep和正则表达式** - 模式匹配、选项
4. **sed文本替换** - 替换、删除、插入
5. **awk文本处理** - 列操作、统计、过滤
6. **进程管理** - ps、后台任务、wait
7. **查找文件** - find命令、各种选项
8. **关联数组** - declare -A、键值对
9. **getopts参数解析** - 选项处理
10. **信号处理** - trap、清理函数

#### 高级 (Advanced) - `shell/exercises/advanced/`
适合进阶学习者：

1. **复杂的文本处理管道** - 多命令组合
2. **高级正则表达式** - 捕获组、前后查找
3. **脚本调试和错误处理** - set -x、set -e、set -u
4. **性能优化** - 避免子shell、内置命令
5. **并行处理** - 后台任务、并发控制
6. **网络操作** - curl、nc、API调用
7. **日志处理和分析** - 解析、统计、报告
8. **数据库操作** - sqlite3、SQL查询
9. **复杂的文件操作** - 批量处理、去重、同步
10. **脚本模块化和重用** - source、函数库、配置

## 🚀 使用方法 (How to Use)

### Python

1. **使用框架模板创建新脚本：**
   ```bash
   cp python/frameworks/template.py my_script.py
   chmod +x my_script.py
   ./my_script.py --help
   ```

2. **运行练习题：**
   ```bash
   cd python/exercises/beginner
   python3 01_basics.py
   ```

3. **完成练习：**
   - 打开练习文件
   - 找到标记为 `# TODO` 的部分
   - 根据提示完成练习
   - 运行脚本验证结果

### Shell

1. **使用框架模板创建新脚本：**
   ```bash
   cp shell/frameworks/template.sh my_script.sh
   chmod +x my_script.sh
   ./my_script.sh --help
   ```

2. **运行练习题：**
   ```bash
   cd shell/exercises/beginner
   chmod +x 01_basics.sh
   ./01_basics.sh
   ```

3. **完成练习：**
   - 打开练习文件
   - 找到标记为 `# TODO` 的部分
   - 根据提示完成练习
   - 运行脚本验证结果

## 📖 学习建议 (Learning Recommendations)

### 对于初学者：
1. 从初级练习开始，逐个完成
2. 理解每个概念后再继续下一个
3. 多实践，修改代码观察变化
4. 查阅官方文档加深理解

### 对于有经验的学习者：
1. 可以直接从中级或高级开始
2. 尝试不看提示完成练习
3. 思考更优的实现方式
4. 将学到的知识应用到实际项目

### 学习路径建议：
```
初学者路径：
Python初级 → Shell初级 → Python中级 → Shell中级 → 实战项目

进阶路径：
Python中级 → Python高级 → Shell中级 → Shell高级 → 系统自动化

专项提升：
选择特定主题深入学习（如：文本处理、并发编程、网络操作等）
```

## 🔧 依赖要求 (Requirements)

### Python
- Python 3.6 或更高版本
- 标准库（无需额外安装）

### Shell
- Bash 4.0 或更高版本
- 标准Unix工具：grep、sed、awk、find等

## 📝 贡献 (Contributing)

欢迎提交问题报告、功能请求或代码贡献！

## 📄 许可证 (License)

本项目采用开源许可证，欢迎学习和分享。

## 🎯 学习目标 (Learning Goals)

通过本仓库的学习，你将能够：

- ✅ 掌握Python和Shell脚本的基础语法
- ✅ 编写规范、可维护的脚本代码
- ✅ 处理文件、文本和数据
- ✅ 理解并应用高级编程概念
- ✅ 进行系统管理和自动化任务
- ✅ 解决实际问题并优化性能

祝学习愉快！Happy Learning! 🎉
