# 练习题 2: 文件整理工具

**难度**: ⭐⭐

## 题目描述

编写一个Python脚本，根据文件扩展名自动整理文件夹：

1. 接受一个目录路径作为参数
2. 扫描目录中的所有文件
3. 根据文件扩展名创建对应的子文件夹：
   - 图片文件 (.jpg, .png, .gif) → images/
   - 文档文件 (.pdf, .doc, .txt) → documents/
   - 视频文件 (.mp4, .avi, .mkv) → videos/
   - 其他文件 → others/
4. 将文件移动到对应的子文件夹
5. 输出整理结果统计

## 示例

```bash
$ python file_organizer.py ./messy_folder
开始整理文件...

创建目录: ./messy_folder/images
创建目录: ./messy_folder/documents

移动文件:
  photo.jpg → images/
  report.pdf → documents/
  video.mp4 → videos/
  readme.txt → documents/

整理完成！
  图片: 1 个
  文档: 2 个
  视频: 1 个
  其他: 0 个
```

## 要求

- 脚本名称：`file_organizer.py`
- 使用 `os` 和 `shutil` 模块
- 不要移动子目录，只处理文件
- 如果目标文件夹不存在，自动创建

## 提示

- 使用 `os.listdir()` 列出目录内容
- 使用 `os.path.isfile()` 判断是否为文件
- 使用 `os.path.splitext()` 分离文件名和扩展名
- 使用 `shutil.move()` 移动文件
- 使用 `os.makedirs(exist_ok=True)` 创建目录
