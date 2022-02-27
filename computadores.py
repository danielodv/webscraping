from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd


LasusPC = "https://lasus.com.co/all-in-one-aio-todo-en-uno"
pag1 = requests.get(LasusPC)
soup = BeautifulSoup(pag1.content,"html.parser")
nombrePc = soup.find_all("div",class_="product-description-short")
ListaNombresPc = list()
for x in nombrePc:
    ListaNombresPc.append(x.text)

PreciosPc = soup.find_all("span",class_="product-price")
ListaPreciosPc = list()
for y in PreciosPc:
    ListaPreciosPc.append(y.text)

df = pd.DataFrame({"Nombre Pc":ListaNombresPc,"Precio Pc":ListaPreciosPc})

df.to_excel('computadores.xlsx')

