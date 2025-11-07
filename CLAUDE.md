# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a video synthesis tool built with Python that combines multiple video segments with audio and subtitles into a final output video file.

**Core Functionality:**
- Accepts multiple video segments as input
- Supports video and audio output
- Supports subtitle file input
- Outputs MP4 format videos
- Designed to be invoked via API to compose video materials into final video files

## Development Setup

**Installation:**
```bash
pip install -r requirements.txt
```

**Dependencies:**
- Python 3.8+
- moviepy 1.0.3 (video processing)
- requests 2.31.0 (file downloading)
- flask 3.0.0 (API service)

## Project Structure

```
video-synthesizer/
├── src/
│   ├── downloader.py    # 文件下载模块
│   └── synthesizer.py   # 视频合成核心模块
├── temp/                # 临时文件目录（下载的素材）
├── output/              # 输出视频目录
├── api.py              # Flask API 服务
├── demo.py             # 演示脚本
└── requirements.txt    # 项目依赖
```

## How to Run

**Start API Service:**
```bash
python api.py
```
API will run on http://127.0.0.1:5000

**Run Demo (with local files):**
```bash
python demo.py
```

## Architecture

**Core Modules:**

1. **downloader.py** - 文件下载模块
   - `download_file()`: 从 URL 下载单个文件
   - `download_segment_files()`: 下载一个片段的所有素材（视频、音频、字幕）

2. **synthesizer.py** - 视频合成核心模块
   - `parse_srt_file()`: 解析 SRT 字幕文件
   - `add_subtitles_to_video()`: 为视频添加字幕
   - `process_single_segment()`: 处理单个片段（替换音频、添加字幕）
   - `synthesize_video()`: 合成最终视频（主函数）

3. **api.py** - Flask API 服务
   - `POST /api/synthesize`: 视频合成接口
   - `GET /api/download/<filename>`: 下载合成后的视频
   - `GET /api/health`: 健康检查

**Data Flow:**
1. API 接收请求（包含视频片段数组）
2. downloader 下载所有素材到 temp/ 目录
3. synthesizer 处理每个片段：
   - 如果有 audio_url，替换视频原有音频
   - 如果有 subtitle_url，添加字幕到视频
4. synthesizer 按 order 顺序拼接所有片段
5. 输出最终视频到 output/ 目录

## Input Data Format

```json
{
  "segments": [
    {
      "order": 1,
      "video_url": "https://example.com/video1.mp4",
      "audio_url": "https://example.com/audio1.mp3",
      "subtitle_url": "https://example.com/subtitle1.srt"
    }
  ],
  "output_filename": "final_video.mp4"
}
```

**Field Descriptions:**
- `order` (required): 视频片段的播放顺序
- `video_url` (required): 视频素材 URL
- `audio_url` (optional): 音频 URL，如果提供则替换视频原有音频
- `subtitle_url` (optional): 字幕文件 URL (SRT格式)，字幕时间轴针对单个片段

## Implementation Notes

- Uses MoviePy for video processing (simple API, suitable for demos)
- Subtitle format: SRT only (can be extended to support VTT)
- Audio replacement: completely replaces original video audio
- Subtitle timing: each subtitle file's timeline starts from 0 for its segment
- Video concatenation: direct concatenation without transitions

## Language Note

The requirements document is in Chinese. Key terms:
- 视频合成 (shìpín héchéng) = Video synthesis/composition
- 视频素材 (shìpín sùcái) = Video materials/footage
- 字幕文件 (zìmù wénjiàn) = Subtitle files