import streamlit as st

st.title("键盘控制测试页面")

st.markdown("### 测试键盘输入")

# 测试键盘输入
key_input = st.text_input("按键盘测试", placeholder="按WASD键测试", key="test_input")

if key_input:
    st.write(f"检测到输入: {key_input}")
    if key_input.lower() == 'w':
        st.success("✅ W键检测成功 - 向上")
    elif key_input.lower() == 's':
        st.success("✅ S键检测成功 - 向下")
    elif key_input.lower() == 'a':
        st.success("✅ A键检测成功 - 向左")
    elif key_input.lower() == 'd':
        st.success("✅ D键检测成功 - 向右")

# 测试按钮
st.markdown("### 测试按钮控制")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("W - 上", key="test_w"):
        st.success("W按钮点击成功")

with col2:
    col_up, col_down = st.columns(2)
    with col_up:
        if st.button("A - 左", key="test_a"):
            st.success("A按钮点击成功")
    with col_down:
        if st.button("S - 下", key="test_s"):
            st.success("S按钮点击成功")

with col3:
    if st.button("D - 右", key="test_d"):
        st.success("D按钮点击成功")

# 添加键盘监听
st.markdown("### 键盘监听测试")
st.markdown("""
<script>
document.addEventListener('keydown', function(event) {
    const key = event.key.toLowerCase();
    console.log('按键:', key);
    
    if (key === 'w') {
        const btn = document.querySelector('button[kind="secondary"][data-testid*="test_w"]');
        if (btn) {
            btn.click();
            console.log('W按钮被点击');
        }
    } else if (key === 's') {
        const btn = document.querySelector('button[kind="secondary"][data-testid*="test_s"]');
        if (btn) {
            btn.click();
            console.log('S按钮被点击');
        }
    } else if (key === 'a') {
        const btn = document.querySelector('button[kind="secondary"][data-testid*="test_a"]');
        if (btn) {
            btn.click();
            console.log('A按钮被点击');
        }
    } else if (key === 'd') {
        const btn = document.querySelector('button[kind="secondary"][data-testid*="test_d"]');
        if (btn) {
            btn.click();
            console.log('D按钮被点击');
        }
    }
});
</script>
""", unsafe_allow_html=True)

st.markdown("### 使用说明")
st.markdown("""
1. 点击输入框，然后按WASD键测试键盘输入
2. 直接按WASD键测试按钮自动点击
3. 查看浏览器控制台(F12)查看调试信息
""")
