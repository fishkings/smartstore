import requests
from bs4 import BeautifulSoup
import json
import time
import numpy as np


cookies = {
    'NNB': '6TTK2RJU3JPWG',
    '_ga': 'GA1.2.1198469368.1669035888',
    'NV_WETR_LOCATION_RGN_M': '"MDUxMTAxMTE="',
    'ASID': '6f5bbfa400000184fa368e5f00000067',
    'NV_WETR_LAST_ACCESS_RGN_M': '"MDUxMTAxMTE="',
    'NID_AUT': 'xDAIttoc1Atdn7rAs4Y+rogecRjh3p1xevXbJnm0Nr0CEioRQ5/hhmRFwExAG7+T',
    'NID_JKL': 'b+0nlz0gwdbCoxClpc3utji+0en89OQHe0BEDbaUv/Y=',
    'nx_ssl': '2',
    'NID_SES': 'AAABxW96fmGBkYLgQP7XsDZmXQS4ITPynaSB0/RQ8Prr3Iob25o6H0eNLg4e0YNj8iARRCjdtzpdDnd32ITPTYyenrUb9MrUpirj+uo8bRrQHndYomWvU1x3libSu1ezIltql4cBAMBNpvYYbkj2eBCX7NzKtiCpt4I1+jl+nlM7CCcScrHaWdq7KeLFdLOhL3OsxGeCvDo3L2HOyhZvnqjACF9o02WkxvtBqDT0gTG6mbTBSQ0774hm3rTu9bBvIYdadFB41VGCtnKqA9qDWamzdm3NaUrcMuMVqEwNz3UJWTOerP/UdG1gxO6MvvNSvGbcUWNZ4zYAqFosY2oCBAiBz4zSYNIlOyyvkjpDDb8sCKg9Engwsm/Jr9A9iHgjXkBFEeOfNyrdSjqcot7x/6watRyvryn1CyOdd2poOn1sPsiVPBOKsGPW5VeOia32l0IcP3ZrfbD3L52lSmD1WFT0Ql0ACJUFlh5eYHeCrzt2q5CUoWmId+p81CsKqEQ0rnIa0GURF0EN9eo7bniTU/Yjq1da6Lostm32N69c4kkCADeRMTM+PuVhB097FRxmt2ZunoWMVIRHEeBj5MkMrGv+dhy9QhphQKXslvQ7yCtGfExR',
    '_datalab_cid': '50000000',
}

headers = {
    'authority': 'datalab.naver.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'NNB=6TTK2RJU3JPWG; _ga=GA1.2.1198469368.1669035888; NV_WETR_LOCATION_RGN_M="MDUxMTAxMTE="; ASID=6f5bbfa400000184fa368e5f00000067; NV_WETR_LAST_ACCESS_RGN_M="MDUxMTAxMTE="; NID_AUT=xDAIttoc1Atdn7rAs4Y+rogecRjh3p1xevXbJnm0Nr0CEioRQ5/hhmRFwExAG7+T; NID_JKL=b+0nlz0gwdbCoxClpc3utji+0en89OQHe0BEDbaUv/Y=; nx_ssl=2; NID_SES=AAABxW96fmGBkYLgQP7XsDZmXQS4ITPynaSB0/RQ8Prr3Iob25o6H0eNLg4e0YNj8iARRCjdtzpdDnd32ITPTYyenrUb9MrUpirj+uo8bRrQHndYomWvU1x3libSu1ezIltql4cBAMBNpvYYbkj2eBCX7NzKtiCpt4I1+jl+nlM7CCcScrHaWdq7KeLFdLOhL3OsxGeCvDo3L2HOyhZvnqjACF9o02WkxvtBqDT0gTG6mbTBSQ0774hm3rTu9bBvIYdadFB41VGCtnKqA9qDWamzdm3NaUrcMuMVqEwNz3UJWTOerP/UdG1gxO6MvvNSvGbcUWNZ4zYAqFosY2oCBAiBz4zSYNIlOyyvkjpDDb8sCKg9Engwsm/Jr9A9iHgjXkBFEeOfNyrdSjqcot7x/6watRyvryn1CyOdd2poOn1sPsiVPBOKsGPW5VeOia32l0IcP3ZrfbD3L52lSmD1WFT0Ql0ACJUFlh5eYHeCrzt2q5CUoWmId+p81CsKqEQ0rnIa0GURF0EN9eo7bniTU/Yjq1da6Lostm32N69c4kkCADeRMTM+PuVhB097FRxmt2ZunoWMVIRHEeBj5MkMrGv+dhy9QhphQKXslvQ7yCtGfExR; _datalab_cid=50000000',
    'origin': 'https://datalab.naver.com',
    'referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


# for i in range(10000):

#     data = {
#         'cid': str(50000000 + i),
#         'timeUnit': 'date',
#         'startDate': '2023-10-09',
#         'endDate': '2023-11-09',
#         'age': '',
#         'gender': '',
#         'device': '',
#         'page': '1',
#         'count': '20',
#     }

#     time.sleep(np.random.rand())

#     response = requests.post(
#       'https://datalab.naver.com/shoppingInsight/getCategoryClickTrend.naver',
#         cookies=cookies,
#         headers=headers,
#         data=data,
#     )

#     data = json.loads(response.text)

#     print(f"{data['result'][0]['title']}")


data = {
        'cid': "50000035",
        'timeUnit': 'date',
        'startDate': '2023-10-09',
        'endDate': '2023-11-09',
        'age': '',
        'gender': '',
        'device': '',
        'page': '1',
        'count': '20',
    }

response = requests.post(
    'https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver',
    cookies=cookies,
    headers=headers,
    data=data,
)

keyword_ranks = json.loads(response.text)
print(f"{keyword_ranks}")
    

# response = requests.post(
#     'https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver',
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )
# keyword_ranks = json.loads(response.text)

# print(f"{keyword_ranks}")


   

# page = 25 
# num = 1
# for i in range(1,26):
#     data = {
#         'cid': '50000393',
#         'timeUnit': 'date',
#         'startDate': '2023-10-09',
#         'endDate': '2023-11-09',
#         'age': '',
#         'gender': '',
#         'device': '',
#         'page': i,
#         'count': '20',
#     }

#     time.sleep(np.random.rand())

#     response = requests.post(
#         'https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver',
#         cookies=cookies,
#         headers=headers,
#         data=data,
#     )
#     # print(response.text)

#     keyword_ranks = json.loads(response.text)

#     for idx,keyword_rank in enumerate(keyword_ranks["ranks"]):
#         print(f"{num}. {keyword_rank['keyword']}")
#         num += 1





