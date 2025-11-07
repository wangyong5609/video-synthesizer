# 测试说明

## 快速测试

使用简化测试脚本（自动生成测试视频和字幕）：

```bash
# 1. 激活虚拟环境
source venv/bin/activate

# 2. 运行测试
cd test
python run_simple_test.py
```

测试成功后会生成 `test/test_output.mp4`

## 查看测试结果

```bash
# Mac 用户
open test/test_output.mp4

# 或者直接双击文件打开
```

## 测试内容

测试脚本会：
1. 自动创建两个测试视频（红色和蓝色）
2. 为每个视频添加字幕
3. 合成为一个完整的视频（约10秒）

## 使用网络资源测试（可选）

如果你有网络访问权限，可以使用 `run_test.py` 下载真实的测试视频：

```bash
python run_test.py
```

这个脚本会使用 Big Buck Bunny 开源视频进行测试。

## 清理测试文件

```bash
rm -rf test/test_data/*.mp4
rm -f test/test_output.mp4
```

