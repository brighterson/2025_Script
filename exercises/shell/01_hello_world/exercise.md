# 练习题 1: Hello World

**难度**: ⭐

## 题目描述

编写一个Shell脚本，实现以下功能：

1. 输出 "Hello, World!"
2. 接受一个命令行参数作为名字
3. 如果提供了名字，输出 "Hello, [名字]!"
4. 如果没有提供参数，输出 "Hello, World!"

## 示例

```bash
$ ./hello.sh
Hello, World!

$ ./hello.sh Alice
Hello, Alice!
```

## 要求

- 脚本名称：`hello.sh`
- 需要有执行权限：`chmod +x hello.sh`
- 使用 `#!/bin/bash` 作为脚本开头

## 提示

- 使用 `$1` 获取第一个命令行参数
- 使用 `if` 语句判断参数是否为空
- 使用 `-z` 测试字符串是否为空
