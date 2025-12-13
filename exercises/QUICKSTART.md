# 快速开始指南

这个指南将帮助你快速开始使用本练习库。

## 前置要求

### Shell练习
- Linux/macOS 系统（或 Windows WSL）
- Bash shell（通常已预装）

### Python练习
- Python 3.6 或更高版本
- 基本的命令行使用能力

## 第一个Shell练习

### 1. 进入练习目录
```bash
cd exercises/shell/01_hello_world
```

### 2. 阅读练习要求
```bash
cat exercise.md
# 或使用你喜欢的文本编辑器打开
```

### 3. 创建你的解答文件
```bash
# 使用任何文本编辑器创建 hello.sh
nano hello.sh
# 或
vim hello.sh
# 或
code hello.sh
```

### 4. 编写代码

基本框架：
```bash
#!/bin/bash

# 你的代码写在这里
```

### 5. 添加执行权限
```bash
chmod +x hello.sh
```

### 6. 测试你的代码
```bash
# 先手动测试
./hello.sh
./hello.sh Alice

# 运行自动化测试
chmod +x test.sh
./test.sh
```

### 7. 如果遇到困难
```bash
# 查看参考答案
cat solution.sh
```

## 第一个Python练习

### 1. 进入练习目录
```bash
cd exercises/python/01_fizzbuzz
```

### 2. 阅读练习要求
```bash
cat exercise.md
```

### 3. 创建你的解答文件
```bash
# 使用任何文本编辑器创建 fizzbuzz.py
nano fizzbuzz.py
# 或
vim fizzbuzz.py
# 或
code fizzbuzz.py
```

### 4. 编写代码

基本框架：
```python
#!/usr/bin/env python3

import sys

def main():
    # 你的代码写在这里
    pass

if __name__ == "__main__":
    main()
```

### 5. 测试你的代码
```bash
# 先手动测试
python3 fizzbuzz.py 15

# 运行自动化测试
python3 test.py
```

### 6. 如果遇到困难
```bash
# 查看参考答案
cat solution.py
```

## 学习技巧

### 1. 不要急于看答案
先独立思考和尝试，这样学习效果最好。

### 2. 使用官方文档
- Shell: `man bash`, `man <command>`
- Python: `python3 -m pydoc <module>`

### 3. 调试技巧

**Shell调试：**
```bash
# 显示执行的每条命令
bash -x ./your_script.sh

# 或在脚本开头添加
set -x
```

**Python调试：**
```python
# 使用print调试
print(f"变量值: {variable}")

# 或使用pdb调试器
import pdb; pdb.set_trace()
```

### 4. 逐步完善
- 先实现基本功能
- 再添加错误处理
- 最后优化代码

### 5. 举一反三
完成练习后，尝试：
- 添加新功能
- 改进错误处理
- 优化性能
- 修改为不同用途

## 常见问题

### Shell相关

**Q: 为什么我的脚本无法执行？**
A: 确保添加了执行权限：`chmod +x your_script.sh`

**Q: 脚本第一行的 `#!/bin/bash` 是什么？**
A: 这是shebang，告诉系统使用bash解释器执行脚本。

**Q: 如何查看命令的用法？**
A: 使用 `man <command>` 或 `<command> --help`

### Python相关

**Q: 如何检查Python版本？**
A: 运行 `python3 --version`

**Q: 导入模块失败怎么办？**
A: 确保使用Python 3：`python3 script.py`

**Q: 如何查看模块文档？**
A: 使用 `python3 -m pydoc <module>`

## 下一步

完成基础练习后，可以：
1. 挑战更高难度的练习
2. 尝试修改和扩展现有练习
3. 自己设计新的练习题
4. 将所学应用到实际项目中

祝学习愉快！🎉
