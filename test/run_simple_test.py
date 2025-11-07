"""
简化版测试脚本
使用本地视频文件进行测试，不需要网络下载
"""

import sys
import os

# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from synthesizer import synthesize_video


def create_test_video():
    """
    使用 moviepy 创建简单的测试视频
    """
    from moviepy.editor import ColorClip, AudioClip
    import numpy as np

    print("创建测试视频...")

    # 创建一个5秒的红色视频
    video1 = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

    # 创建一个简单的音频（440Hz 正弦波）
    def make_frame(t):
        return np.sin(440 * 2 * np.pi * t)

    audio1 = AudioClip(make_frame, duration=5, fps=44100)
    video1 = video1.set_audio(audio1)

    # 保存第一个测试视频
    video1.write_videofile(
        "test/test_data/test_video1.mp4",
        codec='libx264',
        audio_codec='aac',
        fps=24,
        verbose=False,
        logger=None
    )

    # 创建一个5秒的蓝色视频
    video2 = ColorClip(size=(640, 480), color=(0, 0, 255), duration=5)
    audio2 = AudioClip(lambda t: np.sin(880 * 2 * np.pi * t), duration=5, fps=44100)
    video2 = video2.set_audio(audio2)

    # 保存第二个测试视频
    video2.write_videofile(
        "test/test_data/test_video2.mp4",
        codec='libx264',
        audio_codec='aac',
        fps=24,
        verbose=False,
        logger=None
    )

    video1.close()
    video2.close()

    print("✓ 测试视频创建完成")


def run_simple_test():
    """
    运行简化的测试流程
    """
    print("=" * 60)
    print("视频合成工具 - 简化测试")
    print("=" * 60)
    print()

    # 确保测试目录存在
    os.makedirs("test/test_data", exist_ok=True)

    try:
        # 检查测试视频是否存在
        video1_path = "test/test_data/test_video1.mp4"
        video2_path = "test/test_data/test_video2.mp4"

        if not os.path.exists(video1_path) or not os.path.exists(video2_path):
            print("测试视频不存在，正在创建...")
            create_test_video()
            print()

        # 准备测试数据（使用绝对路径）
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        subtitle1_path = os.path.join(base_dir, 'test/test_data/subtitle1.srt')
        subtitle2_path = os.path.join(base_dir, 'test/test_data/subtitle2.srt')

        segments = [
            {
                'video_path': video1_path,
                'audio_path': None,
                'subtitle_path': subtitle1_path
            },
            {
                'video_path': video2_path,
                'audio_path': None,
                'subtitle_path': subtitle2_path
            }
        ]

        print("开始合成视频...")
        print("-" * 60)

        output_path = "test/test_output.mp4"
        result = synthesize_video(segments, output_path=output_path)

        print()
        print("=" * 60)
        print("✓ 测试完成！")
        print(f"✓ 输出文件: {result}")
        print(f"✓ 文件大小: {os.path.getsize(result) / 1024 / 1024:.2f} MB")
        print("=" * 60)
        print()
        print("你可以打开视频查看效果：")
        print(f"  open {result}")

        return True

    except Exception as e:
        print()
        print("=" * 60)
        print(f"✗ 测试失败: {str(e)}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_simple_test()
    sys.exit(0 if success else 1)
