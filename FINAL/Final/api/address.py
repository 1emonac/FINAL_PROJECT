import requests
import selenium

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
    "query" : "서울 마포구 정신과",    
}

data_list = requests.get(url, params=params, headers=headers).json()["documents"]

def search(address1="서울시", address2="마포", keyword="정신과"):
    params = {
        "query" : f"{address1} {address2} {keyword}",    
    }
    data_list = requests.get(url, params=params, headers=headers).json()["documents"]
    
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

