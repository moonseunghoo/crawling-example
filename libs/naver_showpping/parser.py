from bs4 import BeautifulSoup

def getProductInfo(li):
    print(li)
    img = li.find("img")
    return {}



def parse(pageString):
    bsObj = BeautifulSoup(pageString,"html.parser")
    ul = bsObj.find("ul",{"class":"list_basis"})
    lis = ul.findAll("li",)

    products = []
    for li in lis[:1]:
        product = getProductInfo(li)
        products.append(product)

    return products
