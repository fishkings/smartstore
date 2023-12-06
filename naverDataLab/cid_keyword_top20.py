import requests
from bs4 import BeautifulSoup
import json
import time
import numpy as np
import pandas as pd


cids = pd.read_csv(r"primaryCategoryDate/cid_life_keyword.csv")

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



startDate = '2022-12-06'
endDate = '2023-12-06'

df_keyword = pd.read_csv("primaryCategoryDate/231206_cid_keyword/category_search_top20_231206.csv")
num = 2


# cid를 추출해서 top 20까지 출력
for idx,cid in enumerate(cids["cid"][num-2:]):

    keyword_lst = []

    data = {
        'cid': cid,
        'timeUnit': 'date',
        'startDate': startDate,  
        'endDate': endDate,
        'age': '',
        'gender': '',
        'device': '',
        'page': '1',
        'count': '20',
    }

    time.sleep(np.random.rand())

    response = requests.post(
      'https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    keywords = json.loads(response.text)

    for idx,rank in enumerate(keywords["ranks"]):
        keyword_lst.append(rank['keyword'])

    new_row = pd.Series(keyword_lst)
    print(new_row.to_frame().T)
    df_keyword = pd.concat([df_keyword,new_row.to_frame().T], axis=0,ignore_index=True)
    df_keyword.to_csv("primaryCategoryDate/231206_cid_keyword/category_search_top20_231206.csv",index=False)



# 누락된 cid 추출 확인
# cid = pd.read_csv("primary_category_csv/cid/cid_keyword.csv",index_col=0)
# keyword = pd.read_csv("primary_category_csv/top20_keywords/category_search_top20.csv")
# keyword.index = cid.index

# for cid in keyword[keyword.isnull().any(axis=1)].index:

#     keyword_lst = []

#     data = {
#         'cid': cid,
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


# # getCategoryClickTrend
# # getCategoryKeywordRank
#     response = requests.post(
#       'https://datalab.naver.com/shoppingInsight/getCategoryClickTrend.naver',
#         cookies=cookies,
#         headers=headers,
#         data=data,
#     )

#     keywords = json.loads(response.text)


#     print(keywords["result"][0]["fullTitle"])
#     keyword.dropna(inplace=True)

#     keyword.to_csv("primary_category_csv/top20_keywords/category_search_top20.csv")


"""누락된 값들을 확인해보면 크게 의미없는 것들이므로 누락 행 제거. (인기없는)

    면세점 > 패션/잡화 > 신발
    면세점 > 패션/잡화 > 언더웨어
    면세점 > 패션/잡화 > 우산/양산
    면세점 > 패션/잡화 > 여행소품
    면세점 > 전자제품 > 노트북/주변기기
    면세점 > 시계/기프트 > 라이터
    면세점 > 시계/기프트 > 크리스탈
    면세점 > 시계/기프트 > 수첩/다이어리
    면세점 > 주얼리 > 발찌
    면세점 > 주얼리 > 헤어
    면세점 > 주얼리 > 넥타이핀
    면세점 > 주얼리 > 장식소품
    디지털/가전 > 생활가전 > 스탠드 > 칠파장스탠드
    면세점 > 화장품 > 스킨케어 > 스페셜케어
    면세점 > 화장품 > 메이크업 > 네일메이크업
    면세점 > 패션/잡화 > 가방 > 소품/기타
    면세점 > 패션/잡화 > 지갑 > 소품지갑
    디지털/가전 > PC액세서리 > USB액세서리 > USB토이
    디지털/가전 > 멀티미디어장비 > DVR > DVR카드
    면세점 > 전자제품 > MP3/이어폰/헤드폰 > MP3/PMP
    디지털/가전 > 저장장치 > 공미디어 > 미디어전용라벨
    화장품/미용 > 선케어 > 태닝 > 태닝티슈
    도서 > 사회/정치 > 사회복지 > 여성복지
    도서 > 잡지 > 컴퓨터/게임/그래픽 > 그래픽
    도서 > 잡지 > 컴퓨터/게임/그래픽 > 웹

    """

