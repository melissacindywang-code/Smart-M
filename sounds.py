import streamlit as st
import base64
import io

def create_beep_sound(frequency=800, duration=0.2):
    """创建简单的蜂鸣声"""
    import numpy as np
    
    # 生成音频数据
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)
    
    # 转换为16位PCM
    audio_data = (wave * 32767).astype(np.int16)
    
    return audio_data, sample_rate

def create_eat_sound():
    """创建吃食物的音效"""
    import numpy as np
    
    sample_rate = 44100
    duration = 0.3
    
    # 创建上升音调
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    frequency = 400 + 200 * t  # 从400Hz上升到600Hz
    wave = np.sin(2 * np.pi * frequency * t)
    
    # 添加衰减
    envelope = np.exp(-t * 3)
    wave = wave * envelope
    
    # 转换为16位PCM
    audio_data = (wave * 32767).astype(np.int16)
    
    return audio_data, sample_rate

def create_game_over_sound():
    """创建游戏结束音效"""
    import numpy as np
    
    sample_rate = 44100
    duration = 0.5
    
    # 创建下降音调
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    frequency = 600 - 400 * t  # 从600Hz下降到200Hz
    wave = np.sin(2 * np.pi * frequency * t)
    
    # 添加衰减
    envelope = np.exp(-t * 2)
    wave = wave * envelope
    
    # 转换为16位PCM
    audio_data = (wave * 32767).astype(np.int16)
    
    return audio_data, sample_rate

def play_sound(audio_data, sample_rate):
    """播放音效"""
    # 将音频数据转换为base64
    audio_bytes = audio_data.tobytes()
    audio_b64 = base64.b64encode(audio_bytes).decode()
    
    # 创建HTML5音频元素
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/wav;base64,{audio_b64}" type="audio/wav">
    </audio>
    """
    
    return audio_html

def get_sound_html(sound_type):
    """获取指定类型的音效HTML"""
    if sound_type == "eat":
        audio_data, sample_rate = create_eat_sound()
    elif sound_type == "game_over":
        audio_data, sample_rate = create_game_over_sound()
    else:  # beep
        audio_data, sample_rate = create_beep_sound()
    
    return play_sound(audio_data, sample_rate)
