from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd


LasusMouses = "https://lasus.com.co/mouses"
pag = requests.get(LasusMouses)
soup = BeautifulSoup(pag.content,"html.parser")
NombreMouses = soup.find_all("h2",class_="h3 product-title")
ListaNombreMouses = list()
for x in NombreMouses:
    ListaNombreMouses.append(x.text)

PreciosMouses = soup.find_all("span",class_="product-price")
Listapreciosmouses = list()
for y in PreciosMouses:
    Listapreciosmouses.append(y.text)

df = pd.DataFrame({"Nombre Mouses": ListaNombreMouses, "Precio Mouses": Listapreciosmouses})

df.to_excel('Mouses.xlsx')