"""
Flask API 服务
提供视频合成的 HTTP API 接口
"""

from flask import Flask, request, jsonify, send_file
import os
import sys

# 将 src 目录添加到 Python 路径，以便导入模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from downloader import download_segment_files
from synthesizer import synthesize_video


app = Flask(__name__)


@app.route('/api/synthesize', methods=['POST'])
def synthesize():
    """
    视频合成 API 接口

    请求格式 (JSON):
    {
        "segments": [
            {
                "order": 1,
                "video_url": "https://example.com/video1.mp4",
                "audio_url": "https://example.com/audio1.mp3",  // 可选
                "subtitle_url": "https://example.com/subtitle1.srt"  // 可选
            },
            ...
        ],
        "output_filename": "my_video.mp4"  // 可选，默认为 final_video.mp4
    }

    返回格式 (JSON):
    {
        "success": true,
        "output_path": "output/final_video.mp4",
        "message": "视频合成成功"
    }
    """
    try:
        # 获取请求数据
        data = request.get_json()

        if not data or 'segments' not in data:
            return jsonify({
                'success': False,
                'message': '请求数据格式错误，需要提供 segments 数组'
            }), 400

        segments = data['segments']

        # 按 order 字段排序
        segments.sort(key=lambda x: x.get('order', 0))

        # 输出文件名
        output_filename = data.get('output_filename', 'final_video.mp4')
        output_path = os.path.join('output', output_filename)

        # 下载所有素材文件
        print("开始下载素材文件...")
        downloaded_segments = []

        for segment in segments:
            files = download_segment_files(segment)
            downloaded_segments.append(files)

        # 合成视频
        result_path = synthesize_video(downloaded_segments, output_path)

        return jsonify({
            'success': True,
            'output_path': result_path,
            'message': '视频合成成功'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'视频合成失败: {str(e)}'
        }), 500


@app.route('/api/download/<filename>', methods=['GET'])
def download(filename):
    """
    下载合成后的视频文件

    参数:
        filename: 文件名

    返回:
        视频文件
    """
    file_path = os.path.join('output', filename)

    if not os.path.exists(file_path):
        return jsonify({
            'success': False,
            'message': '文件不存在'
        }), 404

    return send_file(file_path, as_attachment=True)


@app.route('/api/health', methods=['GET'])
def health():
    """
    健康检查接口

    返回:
        服务状态信息
    """
    return jsonify({
        'status': 'ok',
        'message': '视频合成服务运行正常'
    })


if __name__ == '__main__':
    # 确保必要的目录存在
    os.makedirs('temp', exist_ok=True)
    os.makedirs('output', exist_ok=True)

    # 启动 Flask 服务
    print("启动视频合成 API 服务...")
    print("访问 http://127.0.0.1:5000/api/health 检查服务状态")
    app.run(host='0.0.0.0', port=5000, debug=True)
