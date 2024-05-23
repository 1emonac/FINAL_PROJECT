import requests

from bs4 import BeautifulSoup
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.by import By

import private_file.key as key
import re

url = "https://dapi.kakao.com/v2/local/search/keyword.json"
headers = {
    "Authorization": "KakaoAK "+key.kakao_key,
    "content-type": "application/json;charset=UTF-8"
}
params = {
    "query" : "서울 마포구 웨딩",    
}

data_list = requests.get(url, params=params, headers=headers).json()["documents"]
# print(data_list)

# url = data_list["place_url"]
# print(url)
# data = requests.get(url).json()

def search(address1="서울시", address2="마포", keyword="웨딩홀"):
    data = []
    print(data,"11111111111111111")
    params = {
        "query" : f"{address1} {address2} {keyword}",    
    }
    data_list = requests.get(url, params=params, headers=headers).json()["documents"]
    # for i in data_list:
    #     a_url = i["place_url"]
    #     url1 = a_url[:a_url.rindex("/")]
    #     url2 = a_url[a_url.rindex("/")+1:]
    #     f_url = f"{url1}/main/v/{url2}"
    #     res = requests.get(f_url).json()["basicInfo"]
    #     # img_url = res["mainphotourl"]
        
    #     d = dict()
    #     d["place_url"] = i["place_url"] if i["place_url"] else None
    #     d["place_name"] = i["place_name"]
    #     d["img_url"] = res.get("mainphotourl") if res.get("mainphotourl") != None else "https://png.pngtree.com/png-clipart/20190119/ourmid/pngtree-wedding-marry-newcomer-happy-event-png-image_469605.jpg"
    #     d["x"] = i["y"]
    #     d["y"] = i["x"]
    #     d["phone"] = i["phone"]
    #     data.append(d)
#address_name': '서울 영등포구 여의도동 1', 'category_group_code': '', 'category_group_name': '', 'category_name': '가정,생활 > 결혼 > 예식장
#', 'distance': '', 'id': '19470491', 'phone': '', 'place_name': '국회의사당 사랑재', 'place_url': 'http://place.map.kakao.com/19470491', 'road_address_name': '서울 영등포구 의사당대로 1', 'x': '126.91576078904762', 'y': '37.5331104583031'}, {'address_name': '서울 영등포구 당산동3가 389-2', 'category_group_code': '', 'category_group_name': '', 'category_name': '가정,생활 > 결혼 > 예식장', 'distance': '', 'id': '1647687761', 'phone': '02-6297-7000', 'place_name': '웨스턴 
#베니비스 영등포', 'place_url': 'http://place.map.kakao.com/1647687761', 'road_address_name': '서울 영등포구 국회대로 558', 'x': '126.896066080956', 'y': '37.527767148281'
    
# https://place.map.kakao.com/main/v/1282059086
# http://place.map.kakao.com/1282059086
    # print(data)
    return data_list

def searchGeo(x, y, keyword):  
    
    params = {
        "query" : keyword,
        "x" : x,
        "y" : y,
        "radius" : 5000,
    }
    data_list = requests.get(url, params=params, headers=headers).json()["documents"]

    return data_list

