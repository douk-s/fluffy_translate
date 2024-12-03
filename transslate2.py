import http.client
import urllib.parse
import re
import json
conn = http.client.HTTPSConnection("api.jaxing.cc")
payload = ''
headers = {
   'devId': '66729f8bcceec4b449b7a646',
   'devToken': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
}


def fy(text):
    encoded_text = urllib.parse.quote(text)
    conn.request("GET", f"/v2/Translate/CloudFlare?Text={encoded_text}&Source_lang=en&Target_lang=zh", payload, headers)
    res = conn.getresponse()
    data = res.read()
    map=json.loads(data)
    return map['data']['response']['translated_text']
def fy2(text):
    conn.request("GET", f"/v2/Translate/CloudFlare?Text={text}&Source_lang=en&Target_lang=zh", payload, headers)
    res = conn.getresponse()
    data = res.read()
    map=json.loads(data)
    return map['data']['response']['translated_text']


def split_sentence(text):
    # 定义要匹配的符号
    pattern = r"[.,!?\"]"
    
    # 使用正则表达式拆分句子
    words = re.split(pattern, text)
    
    # 去除空字符串
    words = [word for word in words if word.strip()]
    
    return words

def transslate(text):
    string=""
    for i in split_sentence(text) :
        string+=fy(i)
    return string
