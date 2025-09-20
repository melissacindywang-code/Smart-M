# 🐍 贪吃蛇游戏 (Snake Game)

一个基于Streamlit开发的经典贪吃蛇游戏，可以在网页浏览器中直接运行。

## 🎮 游戏特色

- **经典玩法**: 经典的贪吃蛇游戏体验
- **现代化界面**: 使用Streamlit构建的美观网页界面
- **响应式设计**: 支持多种屏幕尺寸
- **实时控制**: 支持键盘和按钮控制
- **游戏统计**: 实时显示分数和蛇的长度

## 🚀 快速开始

### 环境要求

- Python 3.7+
- Streamlit
- NumPy

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行游戏

```bash
streamlit run snake_game.py
```

游戏将在浏览器中自动打开，默认地址为 `http://localhost:8501`

## 🎯 游戏玩法

1. **目标**: 控制蛇移动，吃掉食物(🍎)来获得分数
2. **控制方式**:
   - 使用侧边栏的方向按钮
   - 使用键盘方向键 (↑↓←→)
   - 使用WASD键 (W↑S↓A←D→)
   - 空格键暂停/继续游戏
3. **游戏规则**:
   - 每吃掉一个食物获得10分
   - 蛇会随着吃食物而变长
   - 撞墙或撞到自己身体游戏结束
   - 可以随时暂停和重新开始游戏

## 🎨 游戏界面

- **游戏板**: 20x20的绿色网格，蛇和食物用emoji表示
- **侧边栏**: 包含游戏控制、分数显示、方向控制按钮
- **实时统计**: 显示当前分数和蛇的长度

## 📁 项目结构

```
Smart-M/
├── snake_game.py          # 主游戏文件
├── requirements.txt       # 依赖包列表
└── README.md             # 项目说明文档
```

## 🌐 部署到Streamlit Cloud

### 方法1：通过Streamlit Cloud网站部署

1. **推送代码到GitHub**：
   ```bash
   git push origin main
   ```

2. **访问Streamlit Cloud**：
   - 打开 [Streamlit Cloud](https://share.streamlit.io/)
   - 使用GitHub账号登录

3. **部署应用**：
   - 点击 "New app"
   - 选择仓库：`melissacindywang-code/Smart-M`
   - 选择分支：`main`
   - 主文件路径：`snake_game.py`
   - 点击 "Deploy!"

### 方法2：使用GitHub CLI部署

```bash
# 安装GitHub CLI (如果未安装)
# brew install gh  # macOS
# 或访问 https://cli.github.com/

# 登录GitHub
gh auth login

# 推送代码
git push origin main

# 部署到Streamlit Cloud
gh repo create melissacindywang-code/Smart-M --public
```

### 部署后访问

部署成功后，您将获得一个类似这样的URL：
`https://smart-m-snake-game.streamlit.app/`

### 部署配置说明

- **主文件**: `snake_game.py`
- **依赖文件**: `requirements.txt`
- **配置文件**: `.streamlit/config.toml`
- **系统包**: `packages.txt` (空文件，无需额外包)

## 🛠️ 技术栈

- **Streamlit**: Web应用框架
- **NumPy**: 数值计算
- **Python**: 编程语言

## 📝 开发说明

游戏使用面向对象设计，主要类包括：

- `SnakeGame`: 游戏核心逻辑类
- `render_game_board()`: 游戏界面渲染函数
- `main()`: Streamlit应用主函数

## 🎉 享受游戏！

现在就开始你的贪吃蛇之旅吧！看看你能获得多高的分数！
