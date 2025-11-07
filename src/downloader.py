"""
文件下载模块
负责从URL下载视频、音频和字幕文件到本地临时目录
"""

import os
import requests
from urllib.parse import urlparse


def download_file(url, save_dir="temp"):
    """
    从URL下载文件到指定目录

    参数:
        url (str): 文件的URL地址
        save_dir (str): 保存目录，默认为 "temp"

    返回:
        str: 下载后的本地文件路径

    异常:
        如果下载失败会抛出异常
    """
    # 确保保存目录存在
    os.makedirs(save_dir, exist_ok=True)

    # 从URL中提取文件名
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # 如果URL中没有文件名，使用时间戳作为文件名
    if not filename:
        import time
        filename = f"file_{int(time.time())}"

    # 完整的本地文件路径
    local_path = os.path.join(save_dir, filename)

    print(f"正在下载: {url}")

    # 发送HTTP GET请求下载文件
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 如果HTTP状态码不是200，抛出异常

    # 将文件内容写入本地
    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"下载完成: {local_path}")
    return local_path


def download_segment_files(segment, save_dir="temp"):
    """
    下载单个视频片段的所有素材文件（视频、音频、字幕）

    参数:
        segment (dict): 包含视频片段信息的字典
            - video_url: 视频URL（必填）
            - audio_url: 音频URL（可选）
            - subtitle_url: 字幕URL（可选）
        save_dir (str): 保存目录

    返回:
        dict: 包含本地文件路径的字典
            - video_path: 视频文件路径
            - audio_path: 音频文件路径（如果有）
            - subtitle_path: 字幕文件路径（如果有）
    """
    result = {}

    # 下载视频文件（必需）
    result['video_path'] = download_file(segment['video_url'], save_dir)

    # 下载音频文件（可选）
    if segment.get('audio_url'):
        result['audio_path'] = download_file(segment['audio_url'], save_dir)
    else:
        result['audio_path'] = None

    # 下载字幕文件（可选）
    if segment.get('subtitle_url'):
        result['subtitle_path'] = download_file(segment['subtitle_url'], save_dir)
    else:
        result['subtitle_path'] = None

    return result
