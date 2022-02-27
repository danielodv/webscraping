from typing import List
from bs4 import BeautifulSoup
import requests
import panda as pd

 urlAmazon ="https://www.amazon.com/s?k=pc&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
 pagina = requests.get(urlAmazon)
 soup = BeautifulSoup(pagina.content,'html.parser')
nombrePc = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
 ListaNombrePc = List()
 for x in nombrePc:
     ListaNombrePc.append(item.text)


 preciosPc =soup.find_all("span", class_="a-price-whole")
 ListaPrecioPc = list()
 for y in preciosPc:
     ListaPrecioPc.appendd(item.text)

dataFrame = pd.DataFrame({"nombre de la Pc":ListaNombrePc,"precio":ListaPrecioPc})

print(dataFrame)
