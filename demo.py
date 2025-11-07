"""
演示示例：使用本地文件进行视频合成
这个脚本展示如何使用 synthesizer 模块合成视频
"""

import sys
import os

# 将 src 目录添加到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from synthesizer import synthesize_video


def demo_with_local_files():
    """
    使用本地文件进行演示

    使用前请准备好测试文件：
    1. 将测试视频放在 temp/ 目录下，命名为 video1.mp4, video2.mp4 等
    2. 如有音频，命名为 audio1.mp3, audio2.mp3 等
    3. 如有字幕，命名为 subtitle1.srt, subtitle2.srt 等
    """

    # 示例数据：两个视频片段
    segments = [
        {
            'video_path': 'temp/video1.mp4',
            'audio_path': 'temp/audio1.mp3',      # 如果没有可以设为 None
            'subtitle_path': 'temp/subtitle1.srt'  # 如果没有可以设为 None
        },
        {
            'video_path': 'temp/video2.mp4',
            'audio_path': None,  # 第二个片段不替换音频
            'subtitle_path': 'temp/subtitle2.srt'
        }
    ]

    # 检查文件是否存在
    print("检查测试文件...")
    for i, seg in enumerate(segments, 1):
        if not os.path.exists(seg['video_path']):
            print(f"错误: 找不到视频文件 {seg['video_path']}")
            print("请先将测试视频放到 temp/ 目录下")
            return

    # 开始合成
    output_path = synthesize_video(segments, output_path='output/demo_output.mp4')

    print(f"\n演示完成！输出文件: {output_path}")


if __name__ == '__main__':
    demo_with_local_files()
