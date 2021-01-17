import requests

def crawl(keyword):
    url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=숨셔바요&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%88%A8%EC%85%94%EB%B0%94%EC%9A%94&sort=rel&timestamp=&viewType=list"
    data = requests.get(url)
    print(data.status_code,url)
    return data.content
