import vision_api as vapi
from console import log, Level
import time

def test_analyzeImage():
    images = [
       r"TestImages\obama.jpg",
       r"TestImages\trump-glasses.jpg",
       r"TestImages\who.jpg",
       r"TestImages\xi.jpg" 
    ]
    for image_path in images:
        result = vapi.analyzeImage(image_path, 'zh')
        log(result['caption'], Level.INFO)
        log(result['tags'], Level.WARNING)
        time.sleep(1)

def test_OcrImage():
    result = vapi.OcrImage(r'TestImages\news.jpg', 'unk')
    log(f'检测出语言为:{result["language"]}')
    for text in result["texts"]:
        log(text,Level.INFO)

def main():
    test_analyzeImage()
    test_OcrImage()

if __name__ == "__main__":
    main()    