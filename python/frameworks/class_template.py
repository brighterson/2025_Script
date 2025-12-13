#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
面向对象编程模板 - Object-Oriented Programming Template

展示了Python中面向对象编程的基本结构和最佳实践
Demonstrates basic OOP structure and best practices in Python

作者 (Author): Your Name
日期 (Date): 2025
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any


class BaseClass(ABC):
    """
    抽象基类示例
    Abstract base class example
    """
    
    def __init__(self, name: str):
        """
        初始化方法
        Initialization method
        
        Args:
            name: 对象名称 (Object name)
        """
        self._name = name
        self._data: List[Any] = []
    
    @property
    def name(self) -> str:
        """获取名称 (Get name)"""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """设置名称 (Set name)"""
        if not value:
            raise ValueError("名称不能为空 (Name cannot be empty)")
        self._name = value
    
    @abstractmethod
    def process(self) -> None:
        """
        抽象方法，子类必须实现
        Abstract method that must be implemented by subclasses
        """
        pass
    
    def add_data(self, item: Any) -> None:
        """
        添加数据
        Add data
        
        Args:
            item: 要添加的数据项 (Data item to add)
        """
        self._data.append(item)
    
    def get_data(self) -> List[Any]:
        """
        获取所有数据
        Get all data
        
        Returns:
            List[Any]: 数据列表 (Data list)
        """
        return self._data.copy()
    
    def __str__(self) -> str:
        """字符串表示 (String representation)"""
        return f"{self.__class__.__name__}(name='{self._name}')"
    
    def __repr__(self) -> str:
        """开发者表示 (Developer representation)"""
        return f"{self.__class__.__name__}(name='{self._name}', data_count={len(self._data)})"


class ConcreteClass(BaseClass):
    """
    具体实现类
    Concrete implementation class
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        """
        初始化具体类
        Initialize concrete class
        
        Args:
            name: 对象名称 (Object name)
            config: 配置字典 (Configuration dictionary)
        """
        super().__init__(name)
        self._config = config or {}
    
    def process(self) -> None:
        """
        实现抽象方法
        Implement abstract method
        """
        print(f"处理 {self._name} 的数据... (Processing {self._name}'s data...)")
        for item in self._data:
            print(f"  - 处理项: {item} (Processing item: {item})")
    
    def configure(self, key: str, value: Any) -> None:
        """
        配置设置
        Configuration setting
        
        Args:
            key: 配置键 (Config key)
            value: 配置值 (Config value)
        """
        self._config[key] = value
    
    def get_config(self, key: str, default: Any = None) -> Any:
        """
        获取配置值
        Get configuration value
        
        Args:
            key: 配置键 (Config key)
            default: 默认值 (Default value)
            
        Returns:
            Any: 配置值 (Config value)
        """
        return self._config.get(key, default)


class ContextManagerExample:
    """
    上下文管理器示例
    Context manager example
    """
    
    def __init__(self, resource_name: str):
        """
        初始化资源
        Initialize resource
        
        Args:
            resource_name: 资源名称 (Resource name)
        """
        self.resource_name = resource_name
        self.resource = None
    
    def __enter__(self):
        """
        进入上下文时调用
        Called when entering context
        """
        print(f"打开资源: {self.resource_name} (Opening resource: {self.resource_name})")
        self.resource = f"Resource<{self.resource_name}>"
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出上下文时调用
        Called when exiting context
        
        Args:
            exc_type: 异常类型 (Exception type)
            exc_val: 异常值 (Exception value)
            exc_tb: 异常追踪 (Exception traceback)
        """
        print(f"关闭资源: {self.resource_name} (Closing resource: {self.resource_name})")
        self.resource = None
        # 返回False表示不抑制异常 (Return False means don't suppress exceptions)
        return False


def main():
    """
    主函数 - 演示用法
    Main function - demonstrate usage
    """
    print("=== 面向对象编程示例 (OOP Example) ===\n")
    
    # 创建对象 (Create object)
    obj = ConcreteClass("示例对象 (Example Object)")
    
    # 添加数据 (Add data)
    obj.add_data("数据1 (Data 1)")
    obj.add_data("数据2 (Data 2)")
    obj.add_data("数据3 (Data 3)")
    
    # 配置对象 (Configure object)
    obj.configure("设置1", "值1")
    obj.configure("设置2", "值2")
    
    # 处理数据 (Process data)
    print(f"\n对象信息: {obj}")
    print(f"详细信息: {repr(obj)}")
    print(f"配置: {obj.get_config('设置1')}\n")
    
    obj.process()
    
    # 使用上下文管理器 (Use context manager)
    print("\n=== 上下文管理器示例 (Context Manager Example) ===\n")
    with ContextManagerExample("文件资源 (File Resource)") as resource:
        print(f"使用资源: {resource} (Using resource: {resource})")


if __name__ == '__main__':
    main()
