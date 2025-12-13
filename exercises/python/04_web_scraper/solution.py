#!/usr/bin/env python3
"""
练习题 4: 简单API客户端 参考答案
"""

import argparse
import json
import os
import random
from datetime import datetime

HISTORY_FILE = '.weather_history.json'

# 模拟天气数据
WEATHER_CONDITIONS = ['晴朗', '多云', '阴天', '小雨', '大雨', '雪']
CITIES_DATA = {
    '北京': {'temp_range': (0, 30), 'humidity_range': (30, 70)},
    '上海': {'temp_range': (5, 35), 'humidity_range': (40, 80)},
    '广州': {'temp_range': (10, 38), 'humidity_range': (50, 90)},
    '深圳': {'temp_range': (12, 36), 'humidity_range': (50, 85)},
}

def get_weather(city):
    """模拟获取天气数据"""
    # 使用预设范围或默认范围
    city_data = CITIES_DATA.get(city, {'temp_range': (-10, 40), 'humidity_range': (20, 90)})
    
    weather_data = {
        'city': city,
        'temperature': random.randint(*city_data['temp_range']),
        'condition': random.choice(WEATHER_CONDITIONS),
        'humidity': random.randint(*city_data['humidity_range']),
        'wind_speed': round(random.uniform(0, 10), 1),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return weather_data

def display_weather(weather_data):
    """显示天气信息"""
    print(f"\n查询城市: {weather_data['city']}")
    print(f"温度: {weather_data['temperature']}°C")
    print(f"天气: {weather_data['condition']}")
    print(f"湿度: {weather_data['humidity']}%")
    print(f"风速: {weather_data['wind_speed']} m/s")
    print()

def save_to_history(weather_data):
    """保存查询历史"""
    history = []
    
    # 读取现有历史
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except:
            pass
    
    # 添加新记录
    history.append({
        'city': weather_data['city'],
        'timestamp': weather_data['timestamp']
    })
    
    # 保存历史
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def show_history():
    """显示查询历史"""
    if not os.path.exists(HISTORY_FILE):
        print("暂无查询历史")
        return
    
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            history = json.load(f)
        
        if not history:
            print("暂无查询历史")
            return
        
        print("\n查询历史:")
        for i, record in enumerate(history, 1):
            print(f"{i}. {record['city']} - {record['timestamp']}")
        print()
    
    except Exception as e:
        print(f"读取历史记录出错: {e}")

def clear_history():
    """清除查询历史"""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("历史记录已清除")
    else:
        print("没有历史记录需要清除")

def main():
    parser = argparse.ArgumentParser(description='天气查询命令行工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # query 子命令
    query_parser = subparsers.add_parser('query', help='查询城市天气')
    query_parser.add_argument('city', help='城市名称')
    
    # history 子命令
    subparsers.add_parser('history', help='查看查询历史')
    
    # clear 子命令
    subparsers.add_parser('clear', help='清除查询历史')
    
    args = parser.parse_args()
    
    if args.command == 'query':
        weather_data = get_weather(args.city)
        display_weather(weather_data)
        save_to_history(weather_data)
    
    elif args.command == 'history':
        show_history()
    
    elif args.command == 'clear':
        clear_history()
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
