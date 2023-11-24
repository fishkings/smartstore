import pandas as pd
import numpy as np

cid = pd.read_csv("primaryCategoryDate/cid_keyword.csv",index_col=0)

# cid를 컬럼으로 넘주고 0부터 오름차순으로 인덱스 생성
cid["cid"] = cid.index 
cid = cid[["cid","title"]]
cid.index = np.arange(0,len(cid["title"]))

top20 = pd.read_csv("primaryCategoryDate/cid_keywords_top20.csv")

# 공통된 cid 부분만 추출 
data = pd.merge(cid,top20,on="cid")

# 공통되지 않은 cid의 title  추출
merged = pd.merge(cid, top20, on="cid", how="left", indicator=True)  # indicator로 병합 작업 확인 가능 
excluded = merged[merged["_merge"] != "both"]

data.to_csv("primaryCategoryDate/cid_keywords_top20.csv",index=False)

