from libs.naver_showpping.crawler import crawl
from libs.naver_showpping.parser import parse


pageString = crawl('')
products = parse(pageString)
print(products)