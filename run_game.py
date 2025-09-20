#!/usr/bin/env python3
"""
贪吃蛇游戏启动脚本
运行此脚本可以快速启动贪吃蛇游戏
"""

import subprocess
import sys
import os

def main():
    """启动贪吃蛇游戏"""
    print("🐍 正在启动贪吃蛇游戏...")
    print("=" * 50)
    
    # 检查是否安装了依赖
    try:
        import streamlit
        import numpy
        print("✅ 依赖检查通过")
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install -r requirements.txt")
        return
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    game_file = os.path.join(current_dir, "snake_game.py")
    
    if not os.path.exists(game_file):
        print(f"❌ 找不到游戏文件: {game_file}")
        return
    
    print("🚀 启动游戏...")
    print("游戏将在浏览器中自动打开")
    print("如果没有自动打开，请访问: http://localhost:8501")
    print("=" * 50)
    
    try:
        # 启动streamlit应用
        subprocess.run([sys.executable, "-m", "streamlit", "run", game_file], check=True)
    except KeyboardInterrupt:
        print("\n👋 游戏已退出")
    except subprocess.CalledProcessError as e:
        print(f"❌ 启动失败: {e}")
    except Exception as e:
        print(f"❌ 未知错误: {e}")

if __name__ == "__main__":
    main()

