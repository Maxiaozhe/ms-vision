# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python
import requests
from os import path,getenv
import sys
# We will need the json library to read the data passed back
# by the web service
import json
import time
from dotenv import load_dotenv

# API KEY
API_KEY = "xxxxx"
# Japan east vision service url
VISION_URL="https://japaneast.api.cognitive.microsoft.com/vision/v2.0/"

"""APIのenv変数を取得する
"""
# .envから環境変数取得する
load_dotenv()

# Subscription key which provides access to this API. 
# Found in your Cognitive Services accounts.
API_KEY = getenv("API_KEY")

# VISION Service URL
# https://japaneast.api.cognitive.microsoft.com/vision/v2.0/
# OR https://{endpoint}/vision/v2.0/
VISION_URL = getenv("VISION_URL")

# Endpoint of vision service
ENDPOINT = getenv("ENDPOINT")
VISION_URL =f'{ENDPOINT}/vision/v2.0/'


def analyzeImage(image_path, lang='en'):
    """画像分析(by microsoft vision)
    - *image_path* 分析したい画像の相対パス
    - *lang* 言語
        en - English, Default.
        es - Spanish.
        ja - Japanese.
        pt - Portuguese.
        zh - Simplified Chinese.
    return {caption,tags}
    """
    # We need the address of our Computer vision service
    vision_service_address = VISION_URL
    # Add the name of the function we want to call to the address
    address = vision_service_address + "analyze"

    # According to the documentation for the analyze image function
    # There are three optional parameterzhs: language, details & visualFeatures
    parameters = {'visualFeatures': 'Description,Color,Categories',
                  'language': lang}

    # We need the key to access our Computer Vision Service
    subscription_key = API_KEY

    # Open the image file to get a file object containing the image to analyze
    basedir = path.dirname(sys.argv[0])
    image_path = path.join(basedir, image_path)
    image_data = open(image_path, 'rb').read()

    # According to the documentation for the analyze image function
    # we need to specify the subscription key and the content type
    # in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}

    # According to the documentation for the analyze image function
    # we use HTTP POST to call this function
    response = requests.post(address, headers=headers,
                             params=parameters, data=image_data)

    # Raise an exception if the call returns an error code
    response.raise_for_status()

    # Display the raw JSON results returned
    results = response.json()
    # print(json.dumps(results))

    # print the value for requestId from the JSON output
    # print()
    # print('requestId')
    # print(results['requestId'])
    captions = results['description']['captions']
    caption = ''
    if len(captions) > 0:
        caption = captions[0]['text']
    tags = results['description']['tags']
    return {
        'caption': caption,
        'tags': tags
    }


def OcrImage(image_path, lang='en'):
    """文字识别
    - *image_path* :画像相对路径
    - *lang* :
        unk（自动检测）
        zh-Hans（简体中文）
        zh-Hant（繁体中文）
        ja 日文
        etc (https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fc)
    return {caption,tags}
    """
    # We need the address of our Computer vision service
    vision_service_address = VISION_URL
    # Add the name of the function we want to call to the address
    address = vision_service_address + "ocr"

    # According to the documentation for the analyze image function
    # There are three optional parameterzhs: language, details & visualFeatures
    parameters = {
        'detectOrientation': 'true',
        'language': lang
    }

    # We need the key to access our Computer Vision Service
    subscription_key = API_KEY

    # Open the image file to get a file object containing the image to analyze
    basedir = path.dirname(sys.argv[0])
    image_path = path.join(basedir, image_path)
    image_data = open(image_path, 'rb').read()

    # According to the documentation for the analyze image function
    # we need to specify the subscription key and the content type
    # in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}

    # According to the documentation for the analyze image function
    # we use HTTP POST to call this function
    response = requests.post(address, headers=headers,
                             params=parameters, data=image_data)

    # Raise an exception if the call returns an error code
    response.raise_for_status()

    # Display the raw JSON results returned
    results = response.json()
    # print(json.dumps(results))

    # print the value for requestId from the JSON output
    # print()
    # print('requestId')
    # print(results['requestId'])
    texts = []  
    for region in results["regions"]:
        lines=[]
        for line in region["lines"]:
            str=""
            for word in line["words"]:
                str = str +  word["text"]            
            lines.append(str)
        texts.append("\n".join(lines))
    result = {
        "texts": texts,
        "language": results["language"]       
    }
    return result
