"""
视频合成测试案例

使用 test/test_data 目录下的测试视频和音频进行合成测试
"""

import sys
import os

# 将 src 目录添加到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from synthesizer import synthesize_video


def test_synthesize_7_segments():
    """
    测试：合成7个视频片段，每个片段都包含音频和字幕
    """
    print("=" * 60)
    print("测试：7个视频片段 + 音频 + 字幕合成")
    print("=" * 60)

    # 构建7个视频片段
    segments = []
    for i in range(1, 8):
        segments.append({
            'video_path': f'test/test_data/{i}.mp4',
            'audio_path': f'test/test_data/{i}.mp3',
            'subtitle_path': f'test/test_data/{i}.srt'
        })

    # 检查文件是否存在
    print("\n检查测试文件...")
    for i, seg in enumerate(segments, 1):
        print(f"\n片段 {i}:")
        
        if not os.path.exists(seg['video_path']):
            print(f"  ✗ 视频文件不存在: {seg['video_path']}")
            return False
        print(f"  ✓ 视频: {seg['video_path']}")

        if seg.get('audio_path') and not os.path.exists(seg['audio_path']):
            print(f"  ✗ 音频文件不存在: {seg['audio_path']}")
            return False
        print(f"  ✓ 音频: {seg['audio_path']}")
        
        if seg.get('subtitle_path') and not os.path.exists(seg['subtitle_path']):
            print(f"  ✗ 字幕文件不存在: {seg['subtitle_path']}")
            return False
        print(f"  ✓ 字幕: {seg['subtitle_path']}")

    # 输出路径
    output_path = 'output/羊群效应_完整版.mp4'
    
    # 确保输出目录存在
    os.makedirs('output', exist_ok=True)

    print("\n" + "=" * 60)
    print("开始合成7个视频片段...")
    print("=" * 60 + "\n")

    # 合成视频（使用0.5秒叠化转场）
    try:
        result_path = synthesize_video(segments, output_path=output_path, transition_duration=0.5)
        
        print("\n" + "=" * 60)
        print("✅ 测试通过！")
        print(f"📁 输出文件: {result_path}")
        print(f"📦 文件大小: {os.path.getsize(result_path) / 1024 / 1024:.2f} MB")
        print("=" * 60)
        print(f"\n可以使用以下命令查看视频:")
        print(f"  open {result_path}\n")
        return True
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = test_synthesize_7_segments()
    sys.exit(0 if success else 1)
