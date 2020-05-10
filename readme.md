## 安装依赖项
```bash
pip install -r "requirement.txt"
```

## Microsoft Computer Vision API 
调用Microsoft Computer Vison API需要在Azure账号上创建Computer Vison API的服务。
创建后在面板上创建Key 和 EndPoint。
创建完成后将Key与EndPoint保存.env文件中。

.env文件
```ini
# VISION API
API_KEY={your vision api key}
ENDPOINT={your end point}
```

## 关于vison_api
|函数名           |功能                 |
|----------------|---------------------|
|analyzeImage    |画像分析              |
|OcrImage        |OCR 文字识别　　　　　  |　

## 使用说明
1. **analyzeImage** 画像分析

函数调用：   
```python
import vision_api as vapi

result = vapi.analyzeImage(r'TestImages\PolarBear.jpg', 'zh')
print(result)
    
```
  函数返回结果
```json
{
  "caption": "白色的熊",
  "tags": ["熊", "北极", "动物", "户外", "水", "白色", "大", "走", "雪", "站"]
}
```
从ms vision api返回的完整结果会自动保存在result文件夹里，可以根据需要扩展。

PolarBear.json内容
```json
{
  "categories": [{ "name": "动物_狗", "score": 0.99609375 }],
  "color": {
    "dominantColorForeground": "White",
    "dominantColorBackground": "White",
    "dominantColors": ["White"],
    "accentColor": "595144",
    "isBwImg": false,
    "isBWImg": false
  },
  "description": {
    "tags": [
      "熊",
      "北极",
      "动物",
      "户外",
      "水",
      "白色",
      "大",
      "走",
      "雪",
      "站"
    ],
    "captions": [{ "text": "白色的熊", "confidence": 0.8161250527510224 }]
  },
  "requestId": "4b90c6a6-9580-4bff-b639-d5276cfb865a",
  "metadata": { "width": 220, "height": 221, "format": "Jpeg" }
}
```

2. **OcrImage**     OCR 文字识别
函数调用：   
```python
import vision_api as vapi
#语言设定为unk可以自动识别
result = vapi.OcrImage(r'TestImages\test.jpg', 'unk')  
print(result)
```
  函数返回结果
```json
{
  "texts": ["更好地记录\n成为更好的自己"],
  "language": "zh-Hans"
}
```
从ms vision api返回的完整结果会自动保存在result文件夹里，可以根据需要扩展。


