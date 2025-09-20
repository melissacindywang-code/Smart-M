import streamlit as st
import numpy as np
import time
import random
from typing import List, Tuple, Optional
import json

class SnakeGame:
    def __init__(self, width: int = 20, height: int = 20):
        self.width = width
        self.height = height
        self.reset_game()
    
    def reset_game(self):
        """重置游戏状态"""
        # 蛇的初始位置（从中心开始）
        center_x, center_y = self.width // 2, self.height // 2
        self.snake = [(center_x, center_y), (center_x - 1, center_y), (center_x - 2, center_y)]
        self.direction = (1, 0)  # 向右移动
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.paused = False
    
    def generate_food(self) -> Tuple[int, int]:
        """生成食物位置"""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def move_snake(self):
        """移动蛇"""
        if self.game_over or self.paused:
            return
        
        # 计算新的头部位置
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # 检查碰撞
        if (new_head[0] < 0 or new_head[0] >= self.width or 
            new_head[1] < 0 or new_head[1] >= self.height or 
            new_head in self.snake):
            self.game_over = True
            return
        
        # 添加新头部
        self.snake.insert(0, new_head)
        
        # 检查是否吃到食物
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            # 如果没有吃到食物，移除尾部
            self.snake.pop()
    
    def change_direction(self, new_direction: Tuple[int, int]):
        """改变蛇的移动方向"""
        # 防止蛇反向移动
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def toggle_pause(self):
        """暂停/继续游戏"""
        self.paused = not self.paused
    
    def get_game_state(self) -> dict:
        """获取游戏状态"""
        return {
            'snake': self.snake,
            'food': self.food,
            'score': self.score,
            'game_over': self.game_over,
            'paused': self.paused,
            'width': self.width,
            'height': self.height
        }

def render_game_board(game_state: dict) -> str:
    """渲染游戏板为HTML"""
    width = game_state['width']
    height = game_state['height']
    snake = game_state['snake']
    food = game_state['food']
    game_over = game_state['game_over']
    paused = game_state['paused']
    
    # 创建游戏板
    board = [['' for _ in range(width)] for _ in range(height)]
    
    # 放置食物
    board[food[1]][food[0]] = '🍎'
    
    # 放置蛇
    for i, (x, y) in enumerate(snake):
        if i == 0:  # 蛇头
            board[y][x] = '🐍'
        else:  # 蛇身
            board[y][x] = '🟢'
    
    # 生成HTML表格
    html = '<div style="display: flex; justify-content: center; margin: 20px 0;">'
    html += '<table style="border-collapse: collapse; border: 3px solid #333; background-color: #2d5016;">'
    
    for row in board:
        html += '<tr>'
        for cell in row:
            if cell:
                html += f'<td style="width: 30px; height: 30px; border: 1px solid #555; text-align: center; font-size: 20px;">{cell}</td>'
            else:
                html += '<td style="width: 30px; height: 30px; border: 1px solid #555; background-color: #2d5016;"></td>'
        html += '</tr>'
    
    html += '</table></div>'
    
    # 添加游戏状态信息
    if game_over:
        html += '<div style="text-align: center; color: #ff4444; font-size: 24px; font-weight: bold; margin: 20px 0;">游戏结束！</div>'
    elif paused:
        html += '<div style="text-align: center; color: #ffaa00; font-size: 20px; font-weight: bold; margin: 20px 0;">游戏暂停</div>'
    
    return html

def main():
    st.set_page_config(
        page_title="贪吃蛇游戏",
        page_icon="🐍",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    # 页面标题
    st.title("🐍 贪吃蛇游戏")
    st.markdown("---")
    
    # 初始化游戏状态
    if 'game' not in st.session_state:
        st.session_state.game = SnakeGame()
    
    if 'game_running' not in st.session_state:
        st.session_state.game_running = False  # 需要手动开始游戏
    
    if 'last_move_time' not in st.session_state:
        st.session_state.last_move_time = 0
    
    game = st.session_state.game
    
    # 侧边栏控制
    with st.sidebar:
        st.header("游戏控制")
        
        # 显示分数
        st.metric("分数", game.score)
        
        # 游戏状态
        if game.game_over:
            st.error("游戏结束")
        elif game.paused:
            st.warning("游戏暂停")
        else:
            st.success("游戏进行中")
        
        st.markdown("---")
        
        # 控制按钮
        col1, col2 = st.columns(2)
        with col1:
            if st.button("开始游戏", disabled=st.session_state.game_running):
                st.session_state.game_running = True
                st.session_state.last_move_time = time.time()
                st.rerun()
        
        with col2:
            if st.button("暂停/继续", disabled=not st.session_state.game_running):
                game.toggle_pause()
                st.rerun()
        
        if st.button("重新开始"):
            game.reset_game()
            st.session_state.game_running = False
            st.rerun()
        
        st.markdown("---")
        
        # 方向控制
        st.subheader("方向控制")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("⬅️", key="left"):
                game.change_direction((-1, 0))
        
        with col2:
            col_up, col_down = st.columns(2)
            with col_up:
                if st.button("⬆️", key="up"):
                    game.change_direction((0, -1))
            with col_down:
                if st.button("⬇️", key="down"):
                    game.change_direction((0, 1))
        
        with col3:
            if st.button("➡️", key="right"):
                game.change_direction((1, 0))
        
        st.markdown("---")
        
        # 游戏说明
        st.subheader("游戏说明")
        st.markdown("""
        - 使用方向键或按钮控制蛇的移动
        - 吃到🍎可以增加分数
        - 避免撞墙或撞到自己
        - 点击暂停/继续可以暂停游戏
        """)
    
    # 主游戏区域
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # 渲染游戏板
        game_state = game.get_game_state()
        game_html = render_game_board(game_state)
        st.markdown(game_html, unsafe_allow_html=True)
        
        # 游戏统计
        st.markdown("---")
        col_score, col_length = st.columns(2)
        with col_score:
            st.metric("当前分数", game.score)
        with col_length:
            st.metric("蛇的长度", len(game.snake))
    
    # 自动移动逻辑
    if st.session_state.game_running and not game.game_over and not game.paused:
        current_time = time.time()
        if current_time - st.session_state.last_move_time >= 0.5:  # 每0.5秒移动一次
            game.move_snake()
            st.session_state.last_move_time = current_time
            st.rerun()
    
    # 添加自动刷新机制
    if st.session_state.game_running and not game.game_over and not game.paused:
        # 使用st.empty()创建占位符，然后自动刷新
        placeholder = st.empty()
        with placeholder.container():
            st.markdown("🔄 游戏正在运行中...")
        
        # 延迟后自动刷新页面
        time.sleep(0.5)
        st.rerun()
    
    # 键盘控制说明
    st.markdown("### 🎮 键盘控制")
    st.markdown("""
    **使用键盘控制游戏：**
    - **↑** 或 **W** - 向上移动
    - **↓** 或 **S** - 向下移动  
    - **←** 或 **A** - 向左移动
    - **→** 或 **D** - 向右移动
    - **空格键** - 暂停/继续游戏
    """)
    
    # 使用Streamlit的键盘输入组件
    key_input = st.text_input("键盘控制 (点击这里然后按方向键)", 
                              placeholder="点击这里，然后使用键盘方向键控制游戏", 
                              key="keyboard_input")
    
    # 处理键盘输入
    if key_input:
        # 检测按键
        if '↑' in key_input or 'w' in key_input.lower() or 'W' in key_input:
            game.change_direction((0, -1))
            st.rerun()
        elif '↓' in key_input or 's' in key_input.lower() or 'S' in key_input:
            game.change_direction((0, 1))
            st.rerun()
        elif '←' in key_input or 'a' in key_input.lower() or 'A' in key_input:
            game.change_direction((-1, 0))
            st.rerun()
        elif '→' in key_input or 'd' in key_input.lower() or 'D' in key_input:
            game.change_direction((1, 0))
            st.rerun()
        elif ' ' in key_input:
            game.toggle_pause()
            st.rerun()
    
    # 添加JavaScript键盘监听
    st.markdown("""
    <script>
    // 让输入框获得焦点
    const input = document.querySelector('input[placeholder*="键盘控制"]');
    if (input) {
        input.focus();
        input.addEventListener('keydown', function(event) {
            // 阻止默认行为
            event.preventDefault();
            
            // 根据按键设置输入值
            const key = event.key;
            if (key === 'ArrowUp') {
                input.value = '↑';
            } else if (key === 'ArrowDown') {
                input.value = '↓';
            } else if (key === 'ArrowLeft') {
                input.value = '←';
            } else if (key === 'ArrowRight') {
                input.value = '→';
            } else if (key === ' ') {
                input.value = ' ';
            } else if (key.toLowerCase() === 'w') {
                input.value = 'w';
            } else if (key.toLowerCase() === 's') {
                input.value = 's';
            } else if (key.toLowerCase() === 'a') {
                input.value = 'a';
            } else if (key.toLowerCase() === 'd') {
                input.value = 'd';
            }
            
            // 触发输入事件
            input.dispatchEvent(new Event('input', { bubbles: true }));
        });
    }
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

