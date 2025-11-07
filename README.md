# 视频合成工具 - 使用说明

## 快速开始

### 1. 环境设置

运行自动化设置脚本：

```bash
bash setup.sh
```

或者手动设置：

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 运行测试

```bash
# 激活虚拟环境
source venv/bin/activate

# 运行简化测试（自动生成测试视频）
cd test
python run_simple_test.py

# 查看输出视频
open test/test_output.mp4
```

### 3. 启动 API 服务

```bash
# 激活虚拟环境
source venv/bin/activate

# 启动服务
python api.py
```

服务将运行在 `http://127.0.0.1:5000`

### 4. 调用 API

使用 curl 或 Postman 发送请求：

```bash
curl -X POST http://127.0.0.1:5000/api/synthesize \
  -H "Content-Type: application/json" \
  -d '{
    "segments": [
      {
        "order": 1,
        "video_url": "https://example.com/video1.mp4",
        "audio_url": "https://example.com/audio1.mp3",
        "subtitle_url": "https://example.com/subtitle1.srt"
      },
      {
        "order": 2,
        "video_url": "https://example.com/video2.mp4"
      }
    ],
    "output_filename": "my_video.mp4"
  }'
```

### 5. 下载合成后的视频

```bash
curl -O http://127.0.0.1:5000/api/download/my_video.mp4
```

## 本地文件演示

如果你想使用本地文件测试：

1. 将测试视频放到 `temp/` 目录
2. 运行演示脚本：

```bash
python demo.py
```

## 目录说明

- `src/` - 核心代码模块
- `temp/` - 临时文件（下载的素材）
- `output/` - 输出的视频文件
- `api.py` - Flask API 服务
- `demo.py` - 本地演示脚本

## 注意事项

- 音频和字幕是可选的
- 字幕文件格式为 SRT
- 字幕时间轴针对单个片段
- 提供的音频会替换视频原有音频
