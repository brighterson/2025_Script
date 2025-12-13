# 练习题 4: 简单API客户端

**难度**: ⭐⭐⭐

## 题目描述

编写一个Python脚本，创建一个简单的命令行工具来查询天气信息（模拟）：

1. 接受城市名称作为参数
2. 模拟从API获取天气数据
3. 以友好的格式显示天气信息
4. 支持保存查询历史到JSON文件
5. 可以查看历史记录

## 功能要求

```bash
# 查询天气
$ python weather_cli.py query 北京
查询城市: 北京
温度: 15°C
天气: 晴朗
湿度: 45%
风速: 3 m/s

# 查看历史
$ python weather_cli.py history
查询历史:
1. 北京 - 2025-01-13 10:30:15
2. 上海 - 2025-01-13 11:45:20

# 清除历史
$ python weather_cli.py clear
历史记录已清除
```

## 要求

- 脚本名称：`weather_cli.py`
- 使用 `argparse` 处理命令行参数
- 使用 `json` 模块存储历史记录
- 模拟天气数据（不需要真实API）
- 使用 `datetime` 记录查询时间

## 提示

- 使用 `argparse.ArgumentParser()` 创建命令行解析器
- 使用子命令 `add_subparsers()` 处理不同操作
- 使用 `random` 模块生成随机天气数据
- 历史记录保存为 `.weather_history.json`
