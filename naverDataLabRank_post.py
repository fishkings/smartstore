import requests
from bs4 import BeautifulSoup
import json
import openpyxl

cookies = {
    'NNB': '6TTK2RJU3JPWG',
    '_ga': 'GA1.2.1198469368.1669035888',
    'NV_WETR_LOCATION_RGN_M': '"MDUxMTAxMTE="',
    'ASID': '6f5bbfa400000184fa368e5f00000067',
    'NV_WETR_LAST_ACCESS_RGN_M': '"MDUxMTAxMTE="',
    'NID_AUT': 'xDAIttoc1Atdn7rAs4Y+rogecRjh3p1xevXbJnm0Nr0CEioRQ5/hhmRFwExAG7+T',
    'NID_JKL': 'b+0nlz0gwdbCoxClpc3utji+0en89OQHe0BEDbaUv/Y=',
    'nx_ssl': '2',
    '_datalab_cid': '50000000',
    'NID_SES': 'AAABxny17QsRI7XWjIT82lSlLduWZgRrEWC3JXPZ7deYdXvL/c2PUt1Ud42JJjVFG5cfcZocwetwDbTKM0T8sJafQPaeZs/im79ODtVzYIAPqP3dKeq/LuWtkHGyFQdwG7MhhuyvFj6J6Fjb52dGxkZQdTyw9sDIjJGvuVmNz1ttmJhzOo6FGK9SFy5t+b4ILktWm42H76poEeZCHN1x5JahBU1wpphZyTwI+1KJX/JK1+ns5Y5cDRyAZU//7MRxFOnwxNmqPdxI22TCSewIukKlRgfYtVrlXGVf7YTZhfgbd8P7P0xX6RZ4BDEoyApB9j396AnXLVKffXdfpjrJ+BXwpjObqUB8u/vc0fY0976qptW65Ks1m9/P5PhZq3KxvRObMCt9N4u10a18rL63GeOb/oQuN1EKDcFGEWttGb5tSTb85djotOL1/2inlv2C735F7EvQAqLxPidQygSNLfIFWh/6hUICJbzW8rJpE0bEhrqZi2ljp1moUjsub7bO2hj2/+FXoH4ws1/qxxLNpVugB0fRERY1N+CzrXI3UASpoNaYybe3nsDFVaAtwrnKmwiYk6coDGQHLxd3ZN76Y4pRPqYF+r1iHchZP+TPdu/SMUsI',
}

headers = {
    'authority': 'datalab.naver.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'NNB=6TTK2RJU3JPWG; _ga=GA1.2.1198469368.1669035888; NV_WETR_LOCATION_RGN_M="MDUxMTAxMTE="; ASID=6f5bbfa400000184fa368e5f00000067; NV_WETR_LAST_ACCESS_RGN_M="MDUxMTAxMTE="; NID_AUT=xDAIttoc1Atdn7rAs4Y+rogecRjh3p1xevXbJnm0Nr0CEioRQ5/hhmRFwExAG7+T; NID_JKL=b+0nlz0gwdbCoxClpc3utji+0en89OQHe0BEDbaUv/Y=; nx_ssl=2; _datalab_cid=50000000; NID_SES=AAABxny17QsRI7XWjIT82lSlLduWZgRrEWC3JXPZ7deYdXvL/c2PUt1Ud42JJjVFG5cfcZocwetwDbTKM0T8sJafQPaeZs/im79ODtVzYIAPqP3dKeq/LuWtkHGyFQdwG7MhhuyvFj6J6Fjb52dGxkZQdTyw9sDIjJGvuVmNz1ttmJhzOo6FGK9SFy5t+b4ILktWm42H76poEeZCHN1x5JahBU1wpphZyTwI+1KJX/JK1+ns5Y5cDRyAZU//7MRxFOnwxNmqPdxI22TCSewIukKlRgfYtVrlXGVf7YTZhfgbd8P7P0xX6RZ4BDEoyApB9j396AnXLVKffXdfpjrJ+BXwpjObqUB8u/vc0fY0976qptW65Ks1m9/P5PhZq3KxvRObMCt9N4u10a18rL63GeOb/oQuN1EKDcFGEWttGb5tSTb85djotOL1/2inlv2C735F7EvQAqLxPidQygSNLfIFWh/6hUICJbzW8rJpE0bEhrqZi2ljp1moUjsub7bO2hj2/+FXoH4ws1/qxxLNpVugB0fRERY1N+CzrXI3UASpoNaYybe3nsDFVaAtwrnKmwiYk6coDGQHLxd3ZN76Y4pRPqYF+r1iHchZP+TPdu/SMUsI',
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

data = {
    'cid': '50000000',
    'timeUnit': 'date',
    'startDate': '2023-10-08',
    'endDate': '2023-11-08',
    'age': '',
    'gender': '',
    'device': '',
    'page': '2',
    'count': '20',
}

response = requests.post(
    'https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver',
    cookies=cookies,
    headers=headers,
    data=data,
)

# html = response.text
# soup = BeautifulSoup(html,"html.parser")
# print(type(soup.text))    # 이렇게하면 타입이 str이 됨

# keyword_ranks = json.loads(response.text)
# print(keyword_ranks["ranks"])

# data = {
#     'message': None,
#     'statusCode': 200,
#     'returnCode': 0,
#     'date': '',
#     'datetime': '',
#     'range': '2023.10.08. ~ 2023.11.08.',
#     'ranks': [
#         {'rank': 21, 'keyword': '여성가디건', 'linkId': '여성가디건'},
#         {'rank': 22, 'keyword': '내셔널지오그래픽패딩', 'linkId': '내셔널지오그래픽패딩'},
#         {'rank': 23, 'keyword': '스파오후리스', 'linkId': '스파오후리스'},
#         {'rank': 24, 'keyword': '가죽자켓', 'linkId': '가죽자켓'},
#         {'rank': 25, 'keyword': '트위드원피스', 'linkId': '트위드원피스'},
#         {'rank': 26, 'keyword': '티셔츠', 'linkId': '티셔츠'},
#         {'rank': 27, 'keyword': '트레이닝세트', 'linkId': '트레이닝세트'},
#         {'rank': 28, 'keyword': '몽클레어패딩', 'linkId': '몽클레어패딩'},
#         {'rank': 29, 'keyword': '조거팬츠', 'linkId': '조거팬츠'},
#         {'rank': 30, 'keyword': '여성패딩조끼', 'linkId': '여성패딩조끼'},
#         {'rank': 31, 'keyword': '폴로니트', 'linkId': '폴로니트'},
#         {'rank': 32, 'keyword': '지고트원피스', 'linkId': '지고트원피스'},
#         {'rank': 33, 'keyword': '롱패딩', 'linkId': '롱패딩'},
#         {'rank': 34, 'keyword': '올리비아로렌', 'linkId': '올리비아로렌'},
#         {'rank': 35, 'keyword': '여성패딩', 'linkId': '여성패딩'},
#         {'rank': 36, 'keyword': '듀엘', 'linkId': '듀엘'},
#         {'rank': 37, 'keyword': '청바지', 'linkId': '청바지'},
#         {'rank': 38, 'keyword': '케네스레이디원피스', 'linkId': '케네스레이디원피스'},
#         {'rank': 39, 'keyword': '핸드메이드코트', 'linkId': '핸드메이드코트'},
#         {'rank': 40, 'keyword': '지오다노경량패딩', 'linkId': '지오다노경량패딩'}
#     ]
# }
