import vision_api as vapi
from console import log, Level
import time

def test_analyzeImage(lang='en'):
    images = [
       r"TestImages\obama.jpg",
       r"TestImages\trump.jpg",
       r"TestImages\xi.jpg",
       r"TestImages\Parliament_Hill.jpg"
    ]
    for image_path in images:
        result = vapi.analyzeImage(image_path, lang)
        log(result['caption'], Level.INFO)
        log(result['tags'], Level.WARNING)
        time.sleep(1)

def test_OcrImage():
    result = vapi.OcrImage(r'TestImages\news.jpg', 'unk')
    log(f'检测出语言为:{result["language"]}')
    for text in result["texts"]:
        log(text,Level.INFO)

def main():
    # 画像识别
    test_analyzeImage()
    test_analyzeImage('ja')
    test_analyzeImage('zh')
    
    # OCR
    test_OcrImage()

if __name__ == "__main__":
    main()