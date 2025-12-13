# 脚本练习库 (Script Practice Library)

一个提供Shell脚本和Python脚本练习题的学习库。

## 📚 项目简介

本项目为学习Shell和Python脚本编程的初学者和进阶者提供系统化的练习题。每个练习都包含：
- 详细的题目描述
- 参考答案
- 自动化测试脚本

## 🗂️ 目录结构

```
exercises/
├── shell/          # Shell脚本练习
│   ├── 01_hello_world/         # ⭐ Hello World
│   ├── 02_variables/           # ⭐⭐ 变量和计算器
│   ├── 03_file_backup/         # ⭐⭐ 文件备份工具
│   └── 04_log_analyzer/        # ⭐⭐⭐ 日志分析器
│
└── python/         # Python脚本练习
    ├── 01_fizzbuzz/            # ⭐ FizzBuzz
    ├── 02_file_organizer/      # ⭐⭐ 文件整理工具
    ├── 03_csv_processor/       # ⭐⭐ CSV数据处理器
    └── 04_web_scraper/         # ⭐⭐⭐ API客户端
```

## 🚀 快速开始

### Shell脚本练习

1. 进入练习目录：
```bash
cd exercises/shell/01_hello_world
```

2. 阅读题目要求：
```bash
cat exercise.md
```

3. 编写你的解答（例如 `hello.sh`）

4. 运行测试验证：
```bash
chmod +x test.sh
./test.sh
```

5. 如果遇到困难，查看参考答案：
```bash
cat solution.sh
```

### Python脚本练习

1. 进入练习目录：
```bash
cd exercises/python/01_fizzbuzz
```

2. 阅读题目要求：
```bash
cat exercise.md
```

3. 编写你的解答（例如 `fizzbuzz.py`）

4. 运行测试验证：
```bash
python3 test.py
```

5. 如果遇到困难，查看参考答案：
```bash
cat solution.py
```

## 📖 练习列表

### Shell脚本练习

| 编号 | 名称 | 难度 | 主要知识点 |
|------|------|------|-----------|
| 01 | Hello World | ⭐ | 基础语法、参数处理 |
| 02 | 计算器 | ⭐⭐ | 条件判断、case语句 |
| 03 | 文件备份 | ⭐⭐ | 文件操作、时间处理 |
| 04 | 日志分析 | ⭐⭐⭐ | 文本处理、awk/sed |

### Python脚本练习

| 编号 | 名称 | 难度 | 主要知识点 |
|------|------|------|-----------|
| 01 | FizzBuzz | ⭐ | 基础语法、循环、条件 |
| 02 | 文件整理 | ⭐⭐ | 文件系统、模块使用 |
| 03 | CSV处理 | ⭐⭐ | CSV处理、数据统计 |
| 04 | API客户端 | ⭐⭐⭐ | 命令行工具、JSON处理 |

## ✅ 测试说明

每个练习都配有自动化测试脚本：
- Shell练习：`test.sh`
- Python练习：`test.py`

测试脚本会验证你的解答是否正确，并给出通过/失败的反馈。

## 🎯 学习建议

1. **循序渐进**：从⭐难度开始，逐步挑战更高难度
2. **独立思考**：先自己尝试解决，遇到困难再查看提示
3. **理解原理**：不要只是复制答案，要理解代码原理
4. **举一反三**：尝试扩展练习，添加新功能
5. **查阅文档**：遇到不懂的命令或函数，查阅官方文档

## 📝 贡献指南

欢迎贡献新的练习题！请确保：
- 题目描述清晰
- 提供完整的测试用例
- 包含参考答案
- 标注难度等级

## 📄 许可证

本项目采用 MIT 许可证。

## 🤝 联系方式

如有问题或建议，欢迎提出 Issue。

---

**Happy Scripting! 🎉**
