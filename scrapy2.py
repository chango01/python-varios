# CREADO POR GITHUB: CHANGO01

# Scrapy 'mercadolibre' a modo práctica, sin fines de lucro.

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

productos=[]            # Creo listas vacías de productos y precios donde se van a guardar los datos.
precios=[] 

driver=webdriver.Chrome(r"C:\Users\Iair\Desktop\chromedriver.exe")      # Ejecuto el .exe de Chrome para luego pasar la página de mercadolibre como atributo y obtener la información de la misma.
driver.get("https://listado.mercadolibre.com.ar/zapatillas-hombre-running#D[A:zapatillas%20hombre%20running]")
content=driver.page_source
soup=BeautifulSoup(content,'html.parser')

for a in soup.findAll('div', {'class':'item__info'}):              # Busco todos los elementos donde está alojada la info que busco y los recorro con el 'for'.
    nombre=a.find('span', {'class':'main-title'})
    precio=a.find('span', {'class':'price__fraction'})
    n=nombre.text.strip()                                          # Guardo los valores en una variable que luego agrego a las listas creadas.
    p=precio.text.strip()
    productos.append(n)
    precios.append(p)

df = pd.DataFrame({'PRODUCTO':productos,'PRECIO':precios})         # Armo un dataframe usando pandas, creo un archivo .csv e imprimo en consola el resultado.
df.to_csv('listaProductos.csv', index=False, encoding='utf-8')
print(df)