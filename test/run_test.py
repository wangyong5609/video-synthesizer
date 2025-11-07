"""
自动化测试脚本
使用免费的公共测试资源进行视频合成测试
"""

import sys
import os

# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from downloader import download_segment_files
from synthesizer import synthesize_video


def run_test():
    """
    运行完整的测试流程

    使用的测试资源：
    1. 视频：来自 sample-videos.com 的免费测试视频（Big Buck Bunny）
    2. 音频：来自 freesound.org 的免费音效
    3. 字幕：本地创建的测试字幕文件
    """

    print("=" * 60)
    print("视频合成工具 - 自动化测试")
    print("=" * 60)
    print()

    # 测试数据：使用免费公共资源
    # Big Buck Bunny 是一个开源的动画短片，可以自由使用
    test_segments = [
        {
            "order": 1,
            "video_url": "https://sample-videos.com/video321/mp4/240/big_buck_bunny_240p_1mb.mp4",
            "audio_url": None,  # 第一个片段保持原音频
            "subtitle_url": None  # 使用本地字幕文件路径
        },
        {
            "order": 2,
            "video_url": "https://sample-videos.com/video321/mp4/240/big_buck_bunny_240p_2mb.mp4",
            "audio_url": None,
            "subtitle_url": None
        }
    ]

    # 本地字幕文件路径
    subtitle1_path = "test/test_data/subtitle1.srt"
    subtitle2_path = "test/test_data/subtitle2.srt"

    try:
        # 步骤 1: 下载视频素材
        print("步骤 1: 下载视频素材...")
        print("-" * 60)

        downloaded_segments = []

        for i, segment in enumerate(test_segments, 1):
            print(f"\n下载第 {i} 个片段的素材...")
            files = download_segment_files(segment, save_dir="test/test_data")

            # 添加本地字幕文件路径
            if i == 1 and os.path.exists(subtitle1_path):
                files['subtitle_path'] = subtitle1_path
            elif i == 2 and os.path.exists(subtitle2_path):
                files['subtitle_path'] = subtitle2_path

            downloaded_segments.append(files)
            print(f"✓ 第 {i} 个片段下载完成")

        print("\n✓ 所有素材下载完成！")
        print()

        # 步骤 2: 合成视频
        print("步骤 2: 开始合成视频...")
        print("-" * 60)

        output_path = "test/test_output.mp4"
        result = synthesize_video(downloaded_segments, output_path=output_path)

        print()
        print("=" * 60)
        print("✓ 测试完成！")
        print(f"✓ 输出文件: {result}")
        print(f"✓ 文件大小: {os.path.getsize(result) / 1024 / 1024:.2f} MB")
        print("=" * 60)

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
    # 确保测试目录存在
    os.makedirs("test/test_data", exist_ok=True)

    # 运行测试
    success = run_test()

    # 退出代码
    sys.exit(0 if success else 1)
