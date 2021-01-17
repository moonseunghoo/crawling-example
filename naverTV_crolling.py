# 패키지 import
import requests
from bs4 import BeautifulSoup

# 1. 웹에서 데이터 가져오기 : naverTv
raw = requests.get("https://tv.naver.com/r")

# 2. 웹사이트의 HTML 소스코드 Parsing
html = BeautifulSoup(raw.text,"html.parser")

# 3. 컨테이너 선택 : select 함수
container = html.select('div.inner')

# 4. 각 컨테이너별 데이터 수집 : select_one 함수
# 반복문을 이용해 각 컨테이너별로 데이터를 수집한다.

# 5. 각 데이터를 담을 list 생성
title = []
chn = []
hit = []
like = []


for con in container:
    t = con.select_one('dt.title').text.strip()
    c = con.select_one('dd.chn').text.strip()
    h = con.select_one('span.hit').text.strip()
    l = con.select_one('span.like').text.strip()

    title.append(t)
    chn.append(c)
    hit.append(h)
    like.append(l)

print(title)
print(chn)
print(hit)
print(like)


