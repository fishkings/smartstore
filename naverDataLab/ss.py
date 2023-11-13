import requests
import json

cookies = {
    'NNB': '6TTK2RJU3JPWG',
    'autocomplete': 'use',
    'AD_SHP_BID': '23',
    '_ga': 'GA1.2.1198469368.1669035888',
    'NV_WETR_LOCATION_RGN_M': '"MDUxMTAxMTE="',
    'ASID': '6f5bbfa400000184fa368e5f00000067',
    'SHP_BUCKET_ID': '4',
    'NV_WETR_LAST_ACCESS_RGN_M': '"MDUxMTAxMTE="',
    'NID_AUT': 'xDAIttoc1Atdn7rAs4Y+rogecRjh3p1xevXbJnm0Nr0CEioRQ5/hhmRFwExAG7+T',
    'NID_JKL': 'b+0nlz0gwdbCoxClpc3utji+0en89OQHe0BEDbaUv/Y=',
    'nx_ssl': '2',
    'Viking_Rise_visit_time': '1695077035991',
    'page_uid': 'ifYbMdprvTVsse385PlssssssE0-160453',
    'spage_uid': 'ifYbMdprvTVsse385PlssssssE0-160453',
    'NID_SES': 'AAABxneIb+UGNfkjN7HA2gA5OlFQfYJVR367v6fonQYo1gBA+STpwnmSQKvPHCtKl9cSOobgAMZTANOk4CCrBDXAZ+8+xr6VQ9Ezi+8ApV32H/Cwi7PkDkvMuZ3QqwE0RmlD2gBOkdM8F5e33pm7MmNSfpFFusRSCaFir0+c2j3yksaJFDdG9PWn6RxWHTn0JXWu880PKz+pLfdysAibvruAtoxZbtdsvNi3dzUkiI74c14ilruNwmeJ+WmNLRwD79YtsmBgjQd8yEFd2P1MbddwtdfBqqrvIg9mgVAbGhHj86VEjcOAN0a8W84w7vJnGqR5AvPZp6ANSE7LBBYR6BN4RjlHsqne/i39lWovcl8zlv3X//TRlaZFjsdpIdPtHtEPum7wMp0eB+7nLpwAd3Wqz3Ku7eVW9ZH+cwnQwPuLEr3cfZT1scFz3Evmwa4DZWtNXVbACznRMQbUJMYBaN6+kt/PjN932m5O5S1ked50/18fduz9Ga5UzgUJwG86kA2Yj6uX0EJtos8uyYEuUpkHRgKtLkWwSDzI/Qq1281rtR5EslmrYPIicx0eGzIfCGV22q72LUyRwqROGp75LdZlMcC6mJd95X42HzhYacCFvSyx',
    'sus_val': 'oosk3W1yUa/jXC7KKHHcV8KC',
    'ncpa': '5114254|lnq2oiag|6088f8339ff87318d5466310aa33bd3df5f4ee8e|s_21a15037d5896|4a037b7e1ad4f4b2b46b7552bf557d83d6e09c69:4801924|lnq2r5yw|252c45b5b1c89d88d92fb4fd42bf99065652c3d4|s_1aec08c8356c9|4a0769694c3e60ffa7b878ff1e700b5ee7a31a93:95694|lnq2t46o|8f47110d725d91bc72e3083c0376c78965d77ffe|95694|28deee716df4986a1bc2f535eccb8e15165491ff:114|lnrg1u34|6c1e428c1fdcf6109a6e368afd36c2c6547842b5|s_1f0b6dd34481|0d9a8a153a4fd6f9e60247ee72a897423e0d11c7',
}

headers = {
    'authority': 'search.shopping.naver.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'NNB=6TTK2RJU3JPWG; autocomplete=use; AD_SHP_BID=23; _ga=GA1.2.1198469368.1669035888; NV_WETR_LOCATION_RGN_M="MDUxMTAxMTE="; ASID=6f5bbfa400000184fa368e5f00000067; SHP_BUCKET_ID=4; NV_WETR_LAST_ACCESS_RGN_M="MDUxMTAxMTE="; NID_AUT=xDAIttoc1Atdn7rAs4Y+rogecRjh3p1xevXbJnm0Nr0CEioRQ5/hhmRFwExAG7+T; NID_JKL=b+0nlz0gwdbCoxClpc3utji+0en89OQHe0BEDbaUv/Y=; nx_ssl=2; Viking_Rise_visit_time=1695077035991; page_uid=ifYbMdprvTVsse385PlssssssE0-160453; spage_uid=ifYbMdprvTVsse385PlssssssE0-160453; NID_SES=AAABxneIb+UGNfkjN7HA2gA5OlFQfYJVR367v6fonQYo1gBA+STpwnmSQKvPHCtKl9cSOobgAMZTANOk4CCrBDXAZ+8+xr6VQ9Ezi+8ApV32H/Cwi7PkDkvMuZ3QqwE0RmlD2gBOkdM8F5e33pm7MmNSfpFFusRSCaFir0+c2j3yksaJFDdG9PWn6RxWHTn0JXWu880PKz+pLfdysAibvruAtoxZbtdsvNi3dzUkiI74c14ilruNwmeJ+WmNLRwD79YtsmBgjQd8yEFd2P1MbddwtdfBqqrvIg9mgVAbGhHj86VEjcOAN0a8W84w7vJnGqR5AvPZp6ANSE7LBBYR6BN4RjlHsqne/i39lWovcl8zlv3X//TRlaZFjsdpIdPtHtEPum7wMp0eB+7nLpwAd3Wqz3Ku7eVW9ZH+cwnQwPuLEr3cfZT1scFz3Evmwa4DZWtNXVbACznRMQbUJMYBaN6+kt/PjN932m5O5S1ked50/18fduz9Ga5UzgUJwG86kA2Yj6uX0EJtos8uyYEuUpkHRgKtLkWwSDzI/Qq1281rtR5EslmrYPIicx0eGzIfCGV22q72LUyRwqROGp75LdZlMcC6mJd95X42HzhYacCFvSyx; sus_val=oosk3W1yUa/jXC7KKHHcV8KC; ncpa=5114254|lnq2oiag|6088f8339ff87318d5466310aa33bd3df5f4ee8e|s_21a15037d5896|4a037b7e1ad4f4b2b46b7552bf557d83d6e09c69:4801924|lnq2r5yw|252c45b5b1c89d88d92fb4fd42bf99065652c3d4|s_1aec08c8356c9|4a0769694c3e60ffa7b878ff1e700b5ee7a31a93:95694|lnq2t46o|8f47110d725d91bc72e3083c0376c78965d77ffe|95694|28deee716df4986a1bc2f535eccb8e15165491ff:114|lnrg1u34|6c1e428c1fdcf6109a6e368afd36c2c6547842b5|s_1f0b6dd34481|0d9a8a153a4fd6f9e60247ee72a897423e0d11c7',
    'logic': 'PART',
    'referer': 'https://search.shopping.naver.com/search/all?frm=NVSCPRO&origQuery&pagingSize=80&&productSet=total&query=%EC%84%B8%EC%A0%9C&sort=rel&timestamp=&viewType=list',
    'sbth': 'd222b49238bd2b7f29803e2ed2f08d01eedaa3d14d24417197e36287d8d5eae0ca4c01288a05847bfed167eb56487188',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.70", "Google Chrome";v="118.0.5993.70", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

params = {
    'frm': 'NVSCPRO',
    'pagingIndex': '1',
    'pagingSize': '80',
    'productSet': 'total',
    'query': "케이스",
    'sort': 'rel',
    'viewType': 'list',
}

response = requests.get('https://search.shopping.naver.com/api/search/all', params=params, cookies=cookies, headers=headers)
itemlist = json.loads(response.text)

# print(itemlist['shoppingResult']['products'][1]['purchaseCnt'])

sum = 0
for idx,i in enumerate(itemlist['shoppingResult']['products']):
    price = i['purchaseCnt'],
    price =  int(price[0])
    sum += price
    print(price)
print(sum)

# avg = sum / len(itemlist['shoppingResult']['products'])
# print(f"키보드 : {avg}")

