link='https://paytmmall.com/branded_smart_watches-llpid-198964?category=283246&use_mw=1&src=store&from=storefront&tracker=%7C%7C%7C%7C%2Fh%2Fmen-clpid-48-Unbeatable%20Deals%7C295908%7C1%7C%7C00000001C80BFC4479E6AD8886953442583850B4%7C%7C&page=1'
from bs4 import BeautifulSoup
import requests,pprint,json

def scrape():
    res=requests.get(link).text

    soup=BeautifulSoup(res,'html.parser')
    main=soup.find(class_="_3RA-").find_all(class_="_1fje")

    li=[]
    for i in main:
        pr=i.find_all(class_="_2i1r")
        for j in pr:
            name=j.find(class_="UGUy").text
            price=j.find(class_="_1kMS").text
            poster=j.find(class_="_3nWP").find('img').get('src')
            dic={'name':name,'price':price,'poster':poster}
            li.append(dic)
    return li
a=scrape()
# pprint.pprint(scrape())
f=open('paytm_smartwatch.json','w')
json.dump(a,f,indent=4)
f.close()

